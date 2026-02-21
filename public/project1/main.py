import streamlit as st
import pyPDF2
import io
import os 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.write("HELLOW WORLD")
st.set_page_config(page_title = "AI Resume Analyzer", page_icon = "📄", layout = "centered")
st.title("AI Resume Analyzer")
st.markdown("Upload your resume in PDF format and let our AI analyze it for you! The AI will provide insights on the strengths and weaknesses of your resume, as well as suggestions for improvement. This tool is designed to help you create a more effective resume that stands out to potential employers. Try it out now and take the first step towards landing your dream job!")
