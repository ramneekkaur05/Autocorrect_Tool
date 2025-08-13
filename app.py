from textblob import TextBlob as tb
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

def correction_using_textblob(text)-> str:
    blob = tb(text)
    return str(blob.correct())

def correction_using_llm(text)-> str:
    llm = GoogleGenerativeAI(google_api_key= os.getenv("GOOGLE_API_KEY"), model="gemini-1.5-flash", temperature=0.6)
    prompt = f"Correct the grammar and spelling of the following text without changing its meaning: \n{text}"
    response = llm.invoke(prompt)
    return response

# def main():
#     text = input("enter your text: ")
#     corrected_text = correction(text)
#     #print(f"Your original text is: {text}")
#     #print(f"Your corected text is: {corrected_text}")

# if __name__ =="__main__":
#     main()

# Streamlit UI
st.set_page_config(page_title= "Autocorrect tool", layout="centered")
st.title("AUTOCORRECT TOOL")
user_input = ""
user_input = st.text_area("Enter text to correct: ")
if user_input!= "":
    corrected_text= correction_using_llm(user_input)
    st.subheader("Corrected text is: ")
    st.write(corrected_text)

else:
    st.warning("Please firstly enter the text")