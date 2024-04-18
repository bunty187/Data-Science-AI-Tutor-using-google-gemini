import google.generativeai as genai
import streamlit as st 


st.title("💬 Data Science AI ChatBot")
# st.snow()
## Read the API Key
f= open("keys/.gemini_api_key.txt")
key = f.read()

## Configure the API Key
genai.configure(api_key=key) 

## Init a gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                system_instruction=""" You are a helpful Data Science AI Tutor.
                                In which you can answer the Data Science related questions. If the questionn is beyond the Data Science topic then response should be in politetly "That is beyond my knowledge you can ask me about Data science topics." 
                                """)

## If there is no chat_history in session, init one
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

st.chat_message('ai').write("Hi, How may I help you today?")
## Init the chat object
chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)


user_prompt = st.chat_input()

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response = chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state["chat_history"] = chat.history

