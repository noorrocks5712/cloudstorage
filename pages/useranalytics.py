import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  # Your cloud storage backend API URL

def app():
    st.title("📈 Usage Analytics")
    action = st.selectbox("Action", ["View Usage Report", "View File Access Stats"])

    if action == "View Usage Report":
        r = requests.get(f"{API_URL}/usage/report/")
        if r.status_code == 200:
            st.json(r.json())  # Show usage report
        else:
            st.error("Failed to fetch usage report")

    elif action == "View File Access Stats":
        r = requests.get(f"{API_URL}/usage/file_access/")
        if r.status_code == 200:
            st.json(r.json())  # Show file access stats
        else:
            st.error("Failed to fetch file access stats")

    # Back to Home Button
    if st.button("Back to Home"):
        st.session_state.current_page = "home"
        st.rerun()  # Trigger rerun to go back to the home page
