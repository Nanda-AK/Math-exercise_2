#from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain import LLMChain
#from langchain import PromptTemplate

from langchain.chat_models import init_chat_model
import streamlit as st
import os

#Need to Check if these are required
from typing import Optional, Dict
#from pydantic import BaseModel, Field
from typing_extensions import Annotated, TypedDict

# Importing API Key 
os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

#Initiation the LLM Model 
llm = init_chat_model("gpt-4o-mini", model_provider="openai")

# TypedDict
class Joke(TypedDict):
    """Math problem for Grade 6th student"""

    Question: Annotated[str, ..., "Simple Math question on persentage problem"]

    #Answers: Annotated[str, ..., "Provide 4 answer in MCQ"]
    #Answers: Annotated[list[str, str],...,"Provide 4 answer in MCQ"] Working
    A: Annotated[str,..., "Provide Option A answer"]
    B: Annotated[str,..., "Provide Option B Answer"]
    C: Annotated[str,..., "Provide Option C Answer"]
    D: Annotated[str,..., "Provide Option D Answer"]
    #Explanation: Annotated[str, ..., "Explain the answer"
    Explanation: Annotated[str, ..., "Explain the answer in Kids frindly and easy way"]
    #rating: Annotated[Optional[int], None, "How funny the joke is, from 1 to 10"]

structured_llm = llm.with_structured_output(Joke)

#llm_response = structured_llm.invoke("Provide a math percentage Problem")


### Streamlit ###

st.header(" Math Exercise ")
st.subheader(" Generate Math Exercise for practice 🤖 ")

Math_topic = st.selectbox("Choose a Math topic for today's Exercise : ", ["Percentage", "LCM", "HCF"])
st.write("You selected:", Math_topic)

if st.button("Generate"):
    #Math_Q = Math_chain.invoke({"Math_topic" : Math_topic})
    #st.write(Math_Q.content)
    llm_response = structured_llm.invoke("Provide a math percentage Problem")
    st.write(llm_response["Question"])

    options = [
    f"A) {llm_response['A']}",
    f"B) {llm_response['B']}",
    f"C) {llm_response['C']}",
    f"D) {llm_response['D']}"
    ]
    
    answer = st.radio("Select one option:", options)
   
    """
    #st.write(f"{llm_response["A"]} \n{llm_response["B"]}\n{llm_response["C"]}\n{llm_response["D"]}  ")
    st.write(f"A: {llm_response['A']} \n B: {llm_response['B']} \n C: {llm_response['C']} \n D: {llm_response['D']}")
    #st.write(f"B:  {llm_response["B"]}")   
    """ 
