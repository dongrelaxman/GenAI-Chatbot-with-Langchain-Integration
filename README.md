# GenAI-Chatbot-with-Langchain-Integration
## Overview
This project is a Generative AI Chatbot built using LangChain and Streamlit. The chatbot leverages OpenAI’s gpt-3.5-turbo model to provide real-time responses to user queries. It integrates LangChain's powerful prompt templates and OpenAI's LLM to create a seamless conversation experience.

## Features
Generative AI Chatbot: Interacts with users, answering queries based on the prompt provided.
Conversation History: Displays a scrollable conversation log to keep track of past interactions.
User-friendly Interface: Built using Streamlit for a clean and simple user interface.
Real-time Responses: Uses OpenAI's API to generate responses on the fly.

## Requirements
Python 3.7+
Streamlit: For building the web application.
LangChain: For managing prompts and models.
OpenAI API: To access OpenAI’s language models. If you dont have acces use opensource models like Ollama

# Setup Instructions
## Clone the repository:

**bash**

`git clone https://github.com/your-repository/chatbot-app.git`
`cd chatbot-app`
Install the required Python libraries:

**bash**

`pip install streamlit langchain_openai langchain_core python-dotenv`
Create a .env file in the root directory and add your OpenAI and LangChain API keys:

**bash**

OPENAI_API_KEY=your-openai-api-key
LANGCHAIN_API_KEY=your-langchain-api-key
Run the Streamlit app:

**bash**

`streamlit run app.py`

# Frontend Overview
**Streamlit Interface**

The interface consists of a title, a conversation history, and a text input field where users can ask questions.
The conversation history is managed in the Streamlit session state to preserve previous interactions.
User input triggers the handle_input function, which updates the conversation and generates responses using the LangChain pipeline.

**Code Breakdown:**

Environment Setup: The API keys are loaded using dotenv and stored in environment variables for secure access.

**LangChain Pipeline:**

ChatPromptTemplate provides the prompt structure.
The OpenAI model (gpt-3.5-turbo) generates responses.
The output parser extracts the text response from the model.

**Streamlit User Interface:**
Displays the conversation history in a scrollable text area.New queries are entered in a text input field.
On submitting a query, the handle_input function processes it, sends it to the model, and displays the response.
Future Enhancements
Multi-turn Dialog: Expand the chatbot to handle more complex, multi-turn conversations.
User Authentication: Add user login to preserve conversation history across sessions.
Model Customization: Allow users to select different models (like GPT-4) for varied performance.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any questions or suggestions, feel free to reach out via:

Email: dongrei481@gmail.com

GitHub: https://github.com/dongrelaxman