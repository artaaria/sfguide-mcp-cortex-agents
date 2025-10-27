
import streamlit as st
import requests

API_BASE = "https://mcp-fastapi-backend.onrender.com"  # Replace with your Render URL

st.title("Snowflake MCP Agent Chatbot")
st.write("Ask a question:")

user_input = st.text_input("Your question:")
agent = st.selectbox("Choose an agent:", ["snowflake_agent", "analytics_agent"])

if st.button("Send"):
    try:
        response = requests.post(
            f"{API_BASE}/chat",
            params={"agent": agent, "message": user_input},
            timeout=30
        )

        data = response.json()

        if "response" in data:
            st.success("Response:")
            st.write(data["response"])
        else:
            st.error(f"Error: {data.get('error', 'Unknown error')}")

    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {str(e)}")
    except ValueError:
        st.error("Invalid response from server (not JSON).")
