 import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  # Your cloud storage backend API URL

def storage_management():
    st.title("☁️ Cloud Storage Management")
    
    action = st.selectbox("Action", ["View Storage Info", "Increase Storage", "Check Usage"])

    # View current storage information
    if action == "View Storage Info":
        r = requests.get(f"{API_URL}/storage/")
        if r.status_code == 200:
            st.json(r.json())  # Display current storage information (used, total, available)
        else:
            st.error("Failed to fetch storage information")

    # Increase storage capacity
    elif action == "Increase Storage":
        additional_storage = st.number_input("Additional Storage (GB)", min_value=1, step=1)
        if st.button("Increase Storage"):
            r = requests.post(f"{API_URL}/storage/increase", json={"additional_storage": additional_storage})
            if r.status_code == 200:
                st.success(f"Storage increased by {additional_storage} GB!")
            else:
                st.error("Failed to increase storage")

    # Check current storage usage
    elif action == "Check Usage":
        r = requests.get(f"{API_URL}/storage/usage/")
        if r.status_code == 200:
            usage_info = r.json()
            st.write(f"Total Storage: {usage_info['total_storage']} GB")
            st.write(f"Used Storage: {usage_info['used_storage']} GB")
            st.write(f"Available Storage: {usage_info['available_storage']} GB")
            st.write(f"Usage Percentage: {usage_info['usage_percentage']}%")
        else:
            st.error("Failed to fetch storage usage")

    # Back to Home Button
    if st.button("Back to Home"):
        st.session_state.current_page = "home"
        st.rerun()  # Trigger rerun to go back to the home page
