import streamlit as st

def authenticate():
    """Simple authentication check"""
    if 'authenticated' not in st.session_state:
        show_login()
        return False
    return True

def show_login():
    """Display login form"""
    with st.form("login"):
        st.subheader("FarmAI Login")
        
        username = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")
        remember = st.checkbox("Remember me")
        
        if st.form_submit_button("Login"):
            # Simple demo authentication
            if username and password:
                st.session_state.authenticated = True
                st.session_state.user = {"phone": username}
                st.experimental_rerun()
            else:
                st.error("Please enter both phone number and password")

def logout():
    """Clear session and logout"""
    st.session_state.clear()