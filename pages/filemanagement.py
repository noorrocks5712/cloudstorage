import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  # Your cloud storage backend API URL

def app():
    st.title("📁 Cloud File Management")
    action = st.selectbox("Action", ["Upload File", "View All Files", "Get File by ID", "Update File", "Delete File"])

    if action == "Upload File":
        uploaded_file = st.file_uploader("Choose a file to upload")
        if uploaded_file is not None:
            if st.button("Upload"):
                r = requests.post(f"{API_URL}/files/upload/", files={"file": uploaded_file})
                if r.status_code == 200:
                    st.success("File uploaded successfully!")
                else:
                    st.error("Failed to upload file")

    elif action == "View All Files":
        r = requests.get(f"{API_URL}/files/")
        if r.status_code == 200:
            [st.json(i) for i in r.json()]  # Display all files stored in the cloud
        else:
            st.error("Failed to fetch files")

    elif action == "Get File by ID":
        file_id = st.text_input("File ID")
        if st.button("Fetch File"):
            r = requests.get(f"{API_URL}/files/{file_id}")
            if r.status_code == 200:
                st.json(r.json())  # Show file details
            else:
                st.error("File not found")

    elif action == "Update File":
        file_id = st.text_input("File ID")
        new_file_name = st.text_input("New File Name")
        new_file = st.file_uploader("Choose a new file")
        if st.button("Update"):
            files = {"file": new_file} if new_file else None
            data = {"file_name": new_file_name} if new_file_name else {}
            r = requests.put(f"{API_URL}/files/{file_id}", files=files, data=data)
            if r.status_code == 200:
                st.success("File updated successfully!")
            else:
                st.error("Failed to update file")

    elif action == "Delete File":
        file_id = st.text_input("File ID")
        if st.button("Delete"):
            r = requests.delete(f"{API_URL}/files/{file_id}")
            if r.status_code == 200:
                st.success("File deleted successfully!")
            else:
                st.error("Failed to delete file")

    # Back to Home Button
    if st.button("Back to Home"):
        st.session_state.current_page = "home"
        st.rerun()  # Trigger rerun to go back to the home page

