from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os 
from dotenv import load_dotenv 

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an IT assistence who is responsible for assistance IT and coding related query. If the query is not relate to IT or Coding, just respond with 'out of knowledge question'."),
        ("user","Question:{question}")
    ]
)

st.title('Langchain Demo with Ollama')
input_text = st.text_input("Ask Queries related to IT.")

model = "llama3.2"
llm = Ollama(model = model)
output_parser = StrOutputParser()


chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))

