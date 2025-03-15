from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Initializing Google Gemini AI Model 
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

#response = gemini_model.invoke("Give me one math percentage problem for 6th gread indian student in Multipe Choice Option, also provide correct answer")
#print(response.content)

###########################################################################
Math_template ="""
'Can you generate one Math problem for grade 6th student on math topic {Math_topic} with multiple choise answer and also provide answer with explanation'

Format e.g.: 
Math {Math_topic} Problem:
Find the least common multiple (LCM) of 12 and 18.
(a) 6 
(b) 36 
(c) 72 
(d) 216

Answer: (b) 36

Explanation:
There are two main ways to find the LCM of 12 and 18:

Method 1: Listing Multiples
List the multiples of 12: 12, 24, 36, 48, 60, ... List the multiples of 18: 18, 36, 54, 72, ...
The smallest number that appears in both lists is 36. Therefore, the LCM of 12 and 18 is 36.

Method 2: Prime Factorization
Find the prime factorization of each number: 12 = 2 x 2 x 3 = 2² x 3 18 = 2 x 3 x 3 = 2 x 3²
Identify the highest power of each prime factor present in either factorization: The highest power of 2 is 2² = 4 The highest power of 3 is 3² = 9
Multiply these highest powers together: 2² x 3² = 4 x 9 = 36
Therefore, the LCM of 12 and 18 is 36.


Math {Math_topic} Problem:
Sarah bought a bicycle that was originally priced at $250. She received a 15% discount. How much did Sarah pay for the bicycle?

a) 187.50
b) 187.50
b) 212.50 
c) 37.50
d) 37.50
d)287.50

Answer: a) $187.50

Explanation:
To find the discount amount, calculate 15% of $250:
15% of 250 = (15/100)∗250 = $37.50
This means the discount was $37.50. To find the final price Sarah paid, subtract the discount from the original price:
250−37.50 = $187.50
Therefore, Sarah paid $187.50 for the bicycle.

"""
Math_prompt = PromptTemplate(template = Math_template, input_variables =['Math_topic'])

#Create LLM Chain using theprompt template and Model
Math_chain = Math_prompt | gemini_model




### Streamlit ###

st.header(" Math Exercise ")
st.subheader(" Generate Math Exercise for practice 🤖 ")

Math_topic = st.selectbox("Choose a topic for the tweet:", ["Percentage", "LCM", "HCF"])
st.write("You selected:", Math_topic)
count = 1

if st.button("Generate"):
    Math_Q = Math_chain.invoke({"Math_topic" : Math_topic})
    st.write(Math_Q.content)

