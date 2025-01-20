import streamlit as st


st.title("AI Web Scraping")
url = st.text_input("Enter a Website URL: ")
if st.button("Scrape Site"):
    st.write("scraping the website")
