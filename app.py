from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import requests

from cortex_agents import run_cortex_agents
import asyncio


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
from cortex_agents import run_cortex_agents
import asyncio

@app.post("/chat")
async def chat(agent: str, message: str):
    try:
        # Call the Cortex agent async function
        result = await run_cortex_agents(message)
        # Return the main text response (you can add more fields if you want)
        return {"response": result.get("text", "No response from Cortex agent")}
    except Exception as e:
        return {"error": str(e)}
