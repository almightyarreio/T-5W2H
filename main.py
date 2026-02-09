import streamlit as st
import requests
from src.services.apis.trello_api import TrelloService
from src.services.llm.llm_service import LLMService
from src.config.config import Config

st.set_page_config(page_title="T-5W2H Debugger", layout="wide")
st.title("🔧 System Health Check")

col1, col2, col3 = st.columns(3)

# --- TEST 1: CONFIGURATION ---
with col1:
    st.header("1. Config")
    if Config.API_KEY and Config.TOKEN:
        st.success("✅ Keys Found")
        st.write(f"Model: `{Config.AI_MODEL}`")
    else:
        st.error("❌ Missing .env keys")

# --- TEST 2: OLLAMA CONNECTION ---
with col2:
    st.header("2. Ollama (AI)")
    try:
        # Simple ping to see if Ollama is running
        r = requests.get("http://localhost:11434", timeout=2)
        if r.status_code == 200:
            st.success("✅ Ollama Online")
        else:
            st.warning(f"⚠️ Status: {r.status_code}")
    except Exception as e:
        st.error("❌ Ollama Offline")
        st.caption("Run `ollama serve` in terminal")

# --- TEST 3: TRELLO CONNECTION ---
with col3:
    st.header("3. Trello API")
    try:
        trello = TrelloService()
        # Try to fetch your own member data to test the token
        url = f"https://api.trello.com/1/members/me"
        r = requests.get(url, params=trello.auth, timeout=5)
        if r.status_code == 200:
            user = r.json()
            st.success(f"✅ Connected as: {user['fullName']}")
        else:
            st.error(f"❌ Auth Failed: {r.status_code}")
    except Exception as e:
        st.error(f"❌ Connection Error: {e}")

st.divider()

# --- MANUAL TEST AREA ---
st.subheader("🚀 Manual Test")
card_input = st.text_input("Paste Trello Card URL here to test full flow:")

if st.button("Run Diagnostics"):
    if not card_input:
        st.warning("Paste a URL first.")
    else:
        st.write("---")
        # Step A: Fetch Trello
        st.write("1️⃣ Fetching Trello Data...")
        try:
            data = trello.get_card_data(card_input)
            if "error" in data:
                st.error(f"Failed: {data['error']}")
            else:
                st.success(f"Got Card: {data['name']}")
                st.json(data) # Show exactly what we got

                # Step B: Call AI
                st.write("2️⃣ Sending to TinyLlama...")
                ai = LLMService()
                with st.spinner("Waiting for AI... (This can take 30s)"):
                    # We use the raw prompt method to see raw output
                    result = ai.analyze_5w2h(data['name'], data['desc'])
                    
                st.success("AI Responded!")
                st.code(result) # Show RAW output

        except Exception as e:
            st.error(f"CRITICAL ERROR: {str(e)}")