
import streamlit as st

st.title("Snowflake MCP Agent Chatbot")
user_input = st.text_input("Ask a question:")

if user_input:
    # Here you would call your MCP agent logic
    st.write(f"You asked: {user_input}")
    # st.write(agent_response)
