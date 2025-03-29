import streamlit as st
from utils.helpers import set_page_config
from utils.auth import logout

set_page_config()

st.title("🛠️ Account Settings")

# User profile section
st.subheader("Profile Information")
name = st.text_input("Full Name", "Ramesh Kumar")
phone = st.text_input("Phone Number", "+91 9876543210")
language = st.selectbox("Language", ["Hindi", "English", "Tamil", "Telugu", "Marathi"])
farm_size = st.number_input("Farm Size (acres)", min_value=0.1, value=2.5)

if st.button("Update Profile"):
    st.success("Profile updated successfully!")

# Notification settings
st.subheader("Notification Preferences")
col1, col2 = st.columns(2)
with col1:
    sms_alerts = st.checkbox("SMS Alerts", value=True)
    push_notifications = st.checkbox("Push Notifications", value=True)
with col2:
    email_alerts = st.checkbox("Email Alerts", value=False)
    alert_frequency = st.selectbox("Alert Frequency", 
                                 ["Immediate", "Daily Summary", "Weekly Summary"])

# Location settings
st.subheader("Farm Location")
state = st.selectbox("State", ["Maharashtra", "Uttar Pradesh", "Punjab", "Karnataka", "Others"])
district = st.text_input("District", "Nashik")
village = st.text_input("Village", "Shindegaon")

# Logout button
st.markdown("---")
if st.button("Logout", type="primary"):
    logout()
    st.success("You have been logged out successfully!")
    st.experimental_rerun()