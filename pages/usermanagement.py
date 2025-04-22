import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  # Your cloud storage backend API URL

def app():
    st.title("👤 User Management")
    action = st.selectbox("Action", ["Add User", "View All Users", "Get User by ID", "Update User", "Delete User"])

    if action == "Add User":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        role = st.selectbox("Role", ["Admin", "User"])
        if st.button("Add User"):
            r = requests.post(f"{API_URL}/users/", json={
                "username": username, "password": password, "role": role
            })
            st.success("User added successfully!") if r.status_code == 200 else st.error("Failed to add user")

    elif action == "View All Users":
        r = requests.get(f"{API_URL}/users/")
        if r.status_code == 200:
            [st.json(i) for i in r.json()]  # Display all users
        else:
            st.error("Failed to fetch users")

    elif action == "Get User by ID":
        user_id = st.text_input("User ID")
        if st.button("Fetch User"):
            r = requests.get(f"{API_URL}/users/{user_id}")
            if r.status_code == 200:
                st.json(r.json())  # Show user details
            else:
                st.error("User not found")

    elif action == "Update User":
        user_id = st.text_input("User ID")
        username = st.text_input("New Username")
        password = st.text_input("New Password", type="password")
        role = st.selectbox("New Role", ["Admin", "User"])
        if st.button("Update User"):
            r = requests.put(f"{API_URL}/users/{user_id}", json={
                "username": username, "password": password, "role": role
            })
            st.success("User updated successfully!") if r.status_code == 200 else st.error("Failed to update user")

    elif action == "Delete User":
        user_id = st.text_input("User ID")
        if st.button("Delete User"):
            r = requests.delete(f"{API_URL}/users/{user_id}")
            st.success("User deleted successfully!") if r.status_code == 200 else st.error("Failed to delete user")

    # Back to Home Button
    if st.button("Back to Home"):
        st.session_state.current_page = "home"
        st.rerun()  # Trigger rerun to go back to the home page
