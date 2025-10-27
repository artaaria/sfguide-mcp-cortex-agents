from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import requests

app = FastAPI()

# Allow Streamlit frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
def health():
    return {"status": "ok"}

# Agents listing endpoint (mock example)
@app.get("/agents")
def list_agents():
    return [
        {"name": "snowflake_agent", "status": "active", "description": "Handles Snowflake queries"},
        {"name": "analytics_agent", "status": "active", "description": "Performs analytics"}
    ]

# Chat endpoint with Mistral integration
@app.post("/chat")
def chat(agent: str, message: str):
    mistral_api_url = "https://api.mistral.ai/v1/chat/completions"
    mistral_api_key = os.getenv("MISTRAL_API_KEY")

    if not mistral_api_key:
        return {"error": "MISTRAL_API_KEY not set in environment variables"}

    headers = {
        "Authorization": f"Bearer {mistral_api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistral-medium",  # You can change to mistral-large or mistral-small
        "messages": [
            {"role": "system", "content": f"You are {agent}, an MCP agent."},
            {"role": "user", "content": message}
        ]
    }

    try:
        response = requests.post(mistral_api_url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return {"response": data["choices"][0]["message"]["content"]}
    except Exception as e:
        return {"error": str(e)}
