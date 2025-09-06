import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.title("📬 AI Email Assistant")

if st.button("Fetch Real Emails"):
    try:
        response = requests.post(f"{BACKEND_URL}/fetch_emails")
        st.write(response.json())
    except Exception as e:
        st.error(f"Error fetching emails: {e}")

st.markdown("---")

email_id = st.number_input("Email ID to reply", min_value=1, step=1)
draft_text = st.text_area("Your Draft Reply")

if st.button("Send Draft"):
    if draft_text:
        try:
            response = requests.post(
                f"{BACKEND_URL}/send_draft/{email_id}", 
                data=draft_text
            )
            st.write(response.json())
        except Exception as e:
            st.error(f"Error sending draft: {e}")
