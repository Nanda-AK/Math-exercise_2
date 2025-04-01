cfrom langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
import streamlit as st
import os
import json

from typing_extensions import Annotated, TypedDict

# Importing API Key 
os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

#Initiation the LLM Model 
llm = init_chat_model("ft:gpt-4o-mini-2024-07-18:personal:my-math-llm-26th-1st:BFD9gRWW", model_provider="openai")


### Streamlit ###
st.header(" Math Exercise ")
st.subheader(" Generate Math Exercise for practice 🤖 ")


Math_topic = st.selectbox("Choose a Math topic for today's Exercise : ", ["LCM", "HCF", "Percentage", "Fractions", "Decimals", "Division", "Multiples", "Long addition", "Long subtraction", "Long multiples", "Long division"])    

messages = [
    {"role": "system", "content": "You are an AI tutor generating multiple-choice math questions with step-by-step explanations."},
    {"role": "user", "content": f"Generate a math question involving {Math_topic} for 6th grade with Challenge level moderate."}
]

#============================
    
# Initialize session state variables if they don't exist
if "llm_response" not in st.session_state:
    st.session_state.llm_response = None
if "selected_answer" not in st.session_state:
    st.session_state.selected_answer = None
    
# Generate question when button is clicked
if st.button(f"Generate {Math_topic} Math Problem"):
    st.session_state.llm_response = llm.invoke(messages)
    #st.write(st.session_state.llm_response.content)
    #st.write(type(st.session_state.llm_response.content))
    #st.session_state.response_dict = st.session_state.llm_response.content
    st.session_state.response_dict = json.loads(st.session_state.llm_response.content)
    
    st.write(st.session_state.response_dict["Question"])
    if st.button(f"Select a Answer"):
        options = [st.session_state.response_dict["Choices"]["A"], st.session_state.response_dict["Choices"]["D"], st.session_state.response_dict["Choices"]["C"], st.session_state.response_dict["Choices"]["D"]]
        choice = st.radio("Select an option:", options)
    
# Display user selection
st.write(f"✅ You selected: **{choice}**")
   
    
    
    
    
    
    
"""    
    
    st.write(st.session_state.llm_response.content)
    st.write("*"*50)
    st.write(st.session_state.response_dict["Question"])
    st.write("*"*50)
    st.write(st.session_state.response_dict["Choices"]["A"])
    st.write("*"*50)
    st.write(st.session_state.response_dict["Choices"]["B"])
    st.write("*"*50)
    st.write(st.session_state.response_dict["Answer"])
    st.write("*"*50)
    st.write(st.session_state.response_dict["Explanation"])
    st.write("*"*50)
    
"""
