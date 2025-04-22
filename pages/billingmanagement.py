import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  # Your cloud storage backend API URL

def app():
    st.title("💳 Billing & Payments")
    action = st.selectbox("Action", ["View Billing", "Make Payment", "Billing History"])

    if action == "View Billing":
        r = requests.get(f"{API_URL}/billing/")
        if r.status_code == 200:
            st.json(r.json())  # Show current billing details
        else:
            st.error("Failed to fetch billing details")

    elif action == "Make Payment":
        amount = st.number_input("Amount to Pay", min_value=0.0, format="%.2f")
        payment_method = st.selectbox("Payment Method", ["Credit Card", "PayPal", "Bank Transfer"])
        if st.button("Make Payment"):
            r = requests.post(f"{API_URL}/billing/pay", json={
                "amount": amount, "payment_method": payment_method
            })
            if r.status_code == 200:
                st.success("Payment successful!")
            else:
                st.error("Payment failed")

    elif action == "Billing History":
        r = requests.get(f"{API_URL}/billing/history/")
        if r.status_code == 200:
            st.json(r.json())  # Show billing history
        else:
            st.error("Failed to fetch billing history")

    # Back to Home Button
    if st.button("Back to Home"):
        st.session_state.current_page = "home"
        st.rerun()  # Trigger rerun to go back to the home page
