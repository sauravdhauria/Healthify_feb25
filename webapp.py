import streamlit as st
import google.generativeai as genai
import pandas as pd
import os 

api = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api)
model =genai.GenerativeModel('gemini-2.5-flash-lite')


# Lets Create the UI
st.title(":orange[HEALTHIFY] :blue[AI POWERED PERSONAL HEALTH ASSISTANT]")
st.markdown('''##### This is an AI-powered personal health assistant that can help you with various health-related tasks.''')

tips = '''Follow the steps
* Enter your details in the side bar,
* Enter your gender ,age,height(cms), weight(kgs).
* Select the number on the fitness scale from (0-5). 5-Fittest and 0-No fitness at all.
* After filling the details write your promy here and customized response.'''
st.write(tips)


# lets consider the sidebar
st.sidebar.title(":blue[🅴🅽🆃🅴🆁 🆈🅾🆄🆁] :green[🅳🅴🆃🅰🅸🅻🆂]")
name = st.sidebar.text_input("Enter your name")
gender = st.sidebar.selectbox("Select your gender", ["male","female"])
age = st.sidebar.text_input("Enter your age in yrs")
weight = st.sidebar.text_input("Enter your weight in kgs")
height = st.sidebar.text_input("Enter your height in cms")
bmi = pd.to_numeric(weight)/(pd.to_numeric(height)/100)**2
fitness = st.sidebar.slider("Rate your fitness between 0-5",0,5,step=1)
st.sidebar.write(f'{name}Your BMI:{round(bmi,2)} kg/m^2')


# lets use genai model to get the output
user_query = st.text_area("Enter your health related query here")
promt = f'''Assume you are a health expert expert .You are required to
answer the question asked by the user .Use the details the following details provided by
the user.
name of user is {name}
gender is {gender}
age is {age} yrs
weight is {weight} kgs
height is {height} cms
BMI is {round(bmi,2)} kg/m^2
fitness level is {fitness} on scale of 0-5.

Your output should be in following formate
* It should start by giving one two line comment on the details that have been
* It should explain what the real problem is based on query asked by user
* What could be the possible solutions for the  problem.
* You can also mention what doctor to see (specialization) if required.
* Strictly avoid any kind of suggestions related to medicines.
* output should be in bullet points and usertable wherever required.

here is the  query from the user {user_query}'''


if user_query:
    response = model.generate_content(promt)
    st.write(response.text)
