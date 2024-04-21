import streamlit as st
import openai 
import os
import dotenv


# Load environment variables
dotenv.load_dotenv()

#import with dotenc
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print(GROQ_API_KEY)