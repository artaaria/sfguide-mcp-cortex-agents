from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

# Chat endpoint
@app.post("/chat")
def chat(agent: str, message: str):
    # Replace with actual agent logic
    return {"response": f"Agent {agent} received: {message}"}
