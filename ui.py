import streamlit as st
import requests

API_BASE = "https://sfguide-mcp-cortex-agents.onrender.com/"  # Replace with your Render URL

st.title("Snowflake MCP Agent Chatbot")
st.write("Ask a question:")

user_input = st.text_input("Your question:")
agent = st.selectbox("Choose an agent:", ["snowflake_agent", "analytics_agent"])

if st.button("Send"):
    response = requests.post(f"{API_BASE}/chat", params={"agent": agent, "message": user_input})

 try:
        data = response.json()
        if "response" in data:
            st.write("Response:", data["response"])
        else:
            st.error(f"Error: {data.get('error', 'Unknown error')}")
    except ValueError:
        st.error("Invalid response from server.")

