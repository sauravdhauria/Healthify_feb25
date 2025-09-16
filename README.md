# 🧘 Healthify - AI Powered Personal Health Assistant  

Healthify is an AI-powered virtual wellness assistant built using Streamlit and Google Gemini.  
It provides personalized fitness, diet, mental health, and lifestyle recommendations based on user details like age, gender, height, weight, BMI, and fitness level.  

🌐 Live App: [healthaisaurav.streamlit.app](https://healthaisaurav.streamlit.app/)  

---

## 🚀 Features
- 🧑‍⚕️ AI-powered personal health guidance  
- 📊 Personalized BMI calculation  
- 🏋️ Custom fitness and diet plans  
- 🧠 Mental health & wellness tips  
- 🛌 Sleep and lifestyle recommendations  
- 🎤 Conversational health assistant (text-based)  

---

## 🎯 Target Users
- Working professionals with limited time for wellness planning  
- People with chronic conditions needing regular support  
- Fitness beginners or enthusiasts looking for personalized plans  
- Corporates & startups aiming to promote employee health  

---

## 🛠️ Tech Stack
- Frontend: Streamlit (Python)  
- Backend: Google Gemini 2.5 Flash Lite API  
- Libraries:  
  - `streamlit`  
  - `pandas`  
  - `google-generativeai`  
  - `dotenv`, `requests`, `langchain_google_genai`  

---

## 🏗️ Architecture
```mermaid
flowchart TD
    A[User Inputs: name, age, gender, height, weight, fitness level] --> B[Streamlit UI]
    B --> C[LangChain + Gemini API]
    C --> D[Generative AI Model]
    D --> E[Personalized Health Recommendations]
    E --> F[Streamlit Output Display]
