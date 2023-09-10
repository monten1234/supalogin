# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
# import os
from supabase import create_client
from gotrue.errors import AuthApiError
import sys

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
st.title("Supabase Login")
print(sys.version)
email = st.text_input("Email")
password = st.text_input("Password")
supabase = create_client(url, key)
# user = supabase.auth.sign_up({ "email": email, "password": password })

# try:
if st.button("Insert Data"):
    if email:
        try:
            session = supabase.auth.sign_in_with_password({ "email": email, "password": password })
        except AuthApiError:
            print("login failed")
    if session:
        st.success("Data uploaded successfully!")  
