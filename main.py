from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os

from typing_extensions import Annotated, TypedDict

# Importing API Key 
os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

#Initiation the LLM Model 
llm = init_chat_model("ft:gpt-4o-mini-2024-07-18:personal:my-math-llm:BEvcGaoy", model_provider="openai")
#llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-lite") 





### Streamlit ###

st.header(" Math Exercise ")
st.subheader(" Generate Math Exercise for practice 🤖 ")


Math_topic = st.selectbox("Choose a Math topic for today's Exercise : ", ["Percentage", "LCM", "HCF", "Division", "Long Division"])    
    
#============================
    
# Initialize session state variables if they don't exist
if "llm_response" not in st.session_state:
    st.session_state.llm_response = None
if "selected_answer" not in st.session_state:
    st.session_state.selected_answer = None
    
# Generate question when button is clicked
if st.button(f"Generate {Math_topic} Math Problem"):
    st.session_state.llm_response = llm.invoke("Generate Word percentage Math problem with difficult question for grade 10 student? response in json format")
    st.write(st.session_state.llm_response.content)
    #st.write(st.session_state.llm_response["Question"])
    #st.write(st.session_state.llm_response["Choices"]["A"])
    #st.write(st.session_state.llm_response["Answer"])
    #st.write(st.session_state.llm_response["Explanation"])
