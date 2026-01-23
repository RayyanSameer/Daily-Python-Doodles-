import streamlit as st
import requests

# The URL of your AWS Backend (Replace with YOUR IP)
# IMPORTANT: Use the internal docker network name if running locally, 
# but for now let's use the public IP so you understand the connection.
API_URL = "http://13.234.30.53:8001" 

st.title("☁️ Cloud Diary Vault")

# 1. READ DIARY
st.header(" Your Entries")
if st.button("Refresh List"):
    try:
        response = requests.get(f"{API_URL}/list")
        if response.status_code == 200:
            files = response.json().get("files", [])
            selected_file = st.selectbox("Select a file to read:", files)
            
            if st.button(f"Read {selected_file}"):
                res = requests.get(f"{API_URL}/read/{selected_file}")
                if res.status_code == 200:
                    content = res.json().get("content")
                    st.text_area("Content:", content, height=200)
                else:
                    st.error("Could not read file.")
        else:
            st.error("API is down.")
    except Exception as e:
        st.error(f"Connection Error: {e}")

# 2. WRITE DIARY
st.header(" New Entry")
filename = st.text_input("Filename (e.g., day1.txt)")
password = st.text_input("Master Password", type="password")
content = st.text_area("Dear Diary...")

if st.button("Save to Cloud"):
    payload = {
        "filename": filename,
        "content": content,
        "password": password
    }
    try:
        res = requests.post(f"{API_URL}/save", json=payload)
        if res.status_code == 200:
            st.success(f"Saved {filename} successfully!")
        elif res.status_code == 401:
            st.error("Wrong Password!")
        else:
            st.error("Save failed.")
    except Exception as e:
        st.error(f"Connection Error: {e}")