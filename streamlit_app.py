import streamlit as st
import os
from pyterminal.engine import run_command
from pyterminal.nlp import parse_nlp

# Keep track of current directory
if "current_dir" not in st.session_state:
    st.session_state.current_dir = os.getcwd()

st.title("💻 AI-Powered Python Terminal")
st.caption("Hackathon Project – Built with AI")

# Input box
user_input = st.text_input("Enter a command:", key="input")

if st.button("Run"):
    if user_input.strip():
        # Pass through NLP
        parsed_command = parse_nlp(user_input)
        output, st.session_state.current_dir = run_command(parsed_command, st.session_state.current_dir)

        if output == "exit":
            st.warning("Session ended. Please close the tab.")
        else:
            st.code(output)
