from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set API keys
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Initialize LangChain prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to user queries."),
    ("user", "Question: {question}")
])

# Initialize OpenAI model (using gpt-3.5-turbo for now)
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Streamlit framework
st.title("LangChain Demo with OpenAI API")

# Initialize conversation history in Streamlit session state
if "history" not in st.session_state:
    st.session_state.history = []

# Display conversation history in a scrollable text area
conversation_display = ""
for i in range(0, len(st.session_state.history), 2):
    user_entry = st.session_state.history[i]
    assistant_entry = st.session_state.history[i + 1]
    conversation_display += f"You: {user_entry['content']}\n\n"
    conversation_display += f"Assistant: {assistant_entry['content']}\n\n"

# Use text_area to make the conversation scrollable
st.text_area("Conversation History", conversation_display, height=300, max_chars=None)

# Function to handle input and response
def handle_input():
    input_text = st.session_state.input
    if input_text:
        # Add user question to the history
        st.session_state.history.append({"role": "user", "content": input_text})

        # Invoke the chain to get the response
        response = chain.invoke({"question": input_text})

        # Add AI response to the history
        st.session_state.history.append({"role": "assistant", "content": response})

        # Clear input field
        st.session_state.input = ""

# Input field for new queries at the bottom, with on_change callback to handle input
st.text_input("Search the topic you want", key="input", on_change=handle_input)


