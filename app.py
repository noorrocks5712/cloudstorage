import streamlit as st
import pages.UserManagement as user_management  # Cloud user management
import pages.FileManagement as file_management  # Cloud file handling
import pages.StorageManagement as storage_management  # Cloud storage management
import pages.BillingManagement as billing_management  # Cloud billing
import pages.UsageAnalytics as usage_analytics  # Cloud usage reports

st.set_page_config(page_title="Cloud Storage Dashboard", layout="wide")

# Set default page
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Page mapping
page_map = {
    "Home": "home",
    "User Management": "UserManagement",
    "File Management": "FileManagement",
    "Storage Management": "StorageManagement",
    "Billing & Payments": "BillingManagement",
    "Usage Analytics": "UsageAnalytics"
}

reverse_page_map = {v: k for k, v in page_map.items()}  # e.g., "home": "Home"

# Sidebar Navigation
page_selection = st.sidebar.selectbox(
    "Navigate to",
    list(page_map.keys()),
    index=list(page_map.keys()).index(reverse_page_map[st.session_state.current_page])
)
st.session_state.current_page = page_map[page_selection]

# Home page with clickable cards
def show_home():
    st.title("☁️ Cloud Storage Management System")
    st.markdown("Welcome! Choose a module to manage different aspects of the cloud storage system.")

    st.markdown("### Quick Access Modules")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("👤 User Management"):
            st.session_state.current_page = "UserManagement"
            st.rerun()
        if st.button("📁 File Management"):
            st.session_state.current_page = "FileManagement"
            st.rerun()

    with col2:
        if st.button("📊 Storage Management"):
            st.session_state.current_page = "StorageManagement"
            st.rerun()
        if st.button("💳 Billing & Payments"):
            st.session_state.current_page = "BillingManagement"
            st.rerun()

    with col3:
        if st.button("📈 Usage Analytics"):
            st.session_state.current_page = "UsageAnalytics"
            st.rerun()

# Page loader
def load_page():
    if st.session_state.current_page == "home":
        show_home()
    elif st.session_state.current_page == "UserManagement":
        user_management.app()  # User management (cloud accounts, permissions)
    elif st.session_state.current_page == "FileManagement":
        file_management.app()  # File operations (upload, download, organization in cloud)
    elif st.session_state.current_page == "StorageManagement":
        storage_management.app()  # Storage management (allocation, capacity, cloud storage)
    elif st.session_state.current_page == "BillingManagement":
        billing_management.app()  # Billing (invoicing, payments for cloud storage)
    elif st.session_state.current_page == "UsageAnalytics":
        usage_analytics.app()  # Usage reports (storage consumption, activity logs)

# Run selected page
load_page()
