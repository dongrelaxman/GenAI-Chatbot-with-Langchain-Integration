from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

#Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [ 
        ("system"," you are a helpfuol aiistant. please respond to user queries" ),
        ("user"," Question:{question}")
    ]
)

#Streamlit Framework 
st.title(" LAngchain demo with OPENAI API")
input_text=st.text_input(" search the topic you want")

#Olamma Lamma2 llm model 
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)