import time
import google.generativeai as genai
import os
import streamlit as st

apikey = os.environ.get("GENAI_API_KEY")
genai.configure(api_key=apikey)
st.title("Gemini Email Writer")
model =      genai.GenerativeModel('gemini-2.5-flash')
user = st.text_input("Enter the subject of the email:")
tone=st.text_input("Enter the tone of the email:")
st.write("example: formal, informal, friendly, professional, etc.")
length=st.text_input("Enter the length of the email in words:")
st.write("leave 0 if you don't want to specify the length")
if st.button("Submit"):
  promtp=f"You are a professional content writer at amazon , write a email on behalf of user for the subject {user} and the tone should be {tone} keep the email in standard format with the subject line and the body of the email"
  if int(length)!=0:
    promtp+=f" and the length of the email should be {length} words"
  r = model.generate_content(promtp)
  def stream_response(r):
    for i in r.text:
      yield i
      time.sleep(0.02)
  st.subheader("Email:")

  st.write_stream(stream_response(r))
if st.button("exit"):
  st.stop()