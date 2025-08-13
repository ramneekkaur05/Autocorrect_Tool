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
# st.set_page_config(page_title= "Autocorrect tool", layout="centered")
# col1, col2 = st.columns([0.5,3])  # First column bigger for title

# with col1:
#     st.image("autocorrect.png", width=120) 

# with col2:
#     st.markdown("<h1 style='display: inline;'>AUTOCORRECT TOOL ✏️</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 6])

with col1:
    st.image("autocorrect.png", width=100)

with col2:
    st.markdown(
        """
        <div style='display: flex; align-items: center; height: 100%;'>
            <h1 style='margin: 0;'>AUTOCORRECT TOOL ✏️</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
user_input = ""
user_input = st.text_area("Enter text to correct: ")
if user_input!= "":
    corrected_text= correction_using_llm(user_input)
    st.subheader("Corrected text is: 📃 ")
    st.write(corrected_text)

# else:
#     st.warning("Please firstly enter the text")
