import streamlit as st
import os
import subprocess

# Streamlit framework
st.title("Ollama Llama 2 Chatbot Demo")

# Initialize conversation history in Streamlit session state
if "history" not in st.session_state:
    st.session_state.history = []

# Function to generate a response using Ollama
def generate_response(prompt):
    # Run the Ollama command to get the model's response
    result = subprocess.run(['ollama', 'run', 'llama2', prompt], capture_output=True, text=True)
    return result.stdout.strip()

# Display conversation history in a scrollable text area
conversation_display = ""
for entry in st.session_state.history:
    conversation_display += f"You: {entry['user']}\nAssistant: {entry['assistant']}\n\n"

# Use text_area to make the conversation scrollable
st.text_area("Conversation History", conversation_display, height=300, max_chars=None, disabled=True)

# Function to handle input and response
def handle_input():
    input_text = st.session_state.input
    if input_text:
        # Add user question to the history
        st.session_state.history.append({"user": input_text, "assistant": ""})

        # Generate response using Ollama
        response = generate_response(input_text)

        # Update the last entry in history with the assistant's response
        st.session_state.history[-1]["assistant"] = response

        # Clear input field
        st.session_state.input = ""

# Input field for new queries at the bottom, with on_change callback to handle input
st.text_input("Search the topic you want", key="input", on_change=handle_input)
