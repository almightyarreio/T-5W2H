cat > README.md <<EOF
# 📋 T-5W2H: AI Card Refiner

> **Transform vague Trello cards into structured 5W2H Action Plans.**
> *Powered by Debian, Python & Local LLM (Ollama).*

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red.svg)
![AI](https://img.shields.io/badge/AI-Ollama%20Local-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 💡 What is this?
**T-5W2H** is a "Local-First" productivity tool. It connects your Trello board to an Artificial Intelligence running on your own machine (no third-party API costs).

The tool reads a card description, analyzes the context, and rewrites everything using the **5W2H Framework**:
* **What** (What will be done?)
* **Why** (Why?)
* **Where** (Where?)
* **When** (When?)
* **Who** (Who?)
* **How** (How?)
* **How Much** (Cost/Effort?)

## 🚀 Tech Stack
This project was developed and tested in a **Debian 13** environment, focused on performance and privacy.

* **Language:** Python 3
* **Interface:** Streamlit (Web UI)
* **AI Engine:** Ollama (Model: TinyLlama or Llama3)
* **Integration:** Trello REST API
* **Environment:** Linux (Debian/Ubuntu recommended)

## 📦 Installation

### 1. Clone the repository
\`\`\`bash
git clone https://github.com/almightyarreio/T-5W2H.git
cd T-5W2H
\`\`\`

### 2. Prepare Virtual Environment
\`\`\`bash
# Install venv (Debian/Ubuntu)
sudo apt update && sudo apt install python3-venv -y

# Create and activate environment
python3 -m venv venv
source venv/bin/activate
\`\`\`

### 3. Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Setup Local AI (Ollama)
The project uses Ollama to run LLMs locally. Install it and pull a lightweight model (TinyLlama):
\`\`\`bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull the model (use 'llama3' if you have 8GB+ RAM)
ollama pull tinyllama

# Start the server (in a separate terminal)
ollama serve
\`\`\`

## 🔑 Configuration (.env)
Create a \`.env\` file in the root directory and add your Trello keys:

\`\`\`ini
# Trello API (https://trello.com/app-key)
TRELLO_API_KEY=your_api_key_here
TRELLO_TOKEN=your_token_here
TRELLO_BOARD_ID=optional_board_id

# AI Config
AI_MODEL=tinyllama
\`\`\`

## 🏃‍♂️ Usage
With the venv active and Ollama running, execute