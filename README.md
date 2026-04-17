
# Pydantic Project Setup - Chatbot with gradio
Portfolio - Simple Chatbot

## Prerequisites
Ensure you have Python installed on your system.
Python 3.9+
OpenaAI API Key

## Setup Instructions

### 1. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the project root and add necessary environment variables:
```
# Example configuration
OPENAI_API_KEY=sk-....
(Note: '`gpt-5.4-nano` requires access to this specific model. If you don't have access, change the model name in `main.py` to whatever works for you')
```

### 4. Run the Application
```bash
python main.py
```

### 5. Access the Application
Once running, open your browser and navigate to:
URL shown might change
```
http://127.0.0.1:7860
```

## Requirements Explanation
The `requirements.txt` file lists all Python dependencies needed for this project. It specifies:
- **Package names** and versions required
- Run `pip install -r requirements.txt` to install all listed packages automatically

This ensures consistent environments across development, testing, and production.
