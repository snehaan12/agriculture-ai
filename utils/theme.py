import streamlit as st

def get_theme():
    """Get the current theme from session state or default to light"""
    return st.session_state.get("theme", "light")

def toggle_theme():
    """Toggle between light and dark theme"""
    current_theme = get_theme()
    st.session_state.theme = "dark" if current_theme == "light" else "light"

def get_theme_colors():
    """Return color scheme based on current theme"""
    if get_theme() == "dark":
        return {
            "primary": "#4CAF50",
            "background": "#0E1117",
            "secondary_background": "#262730",
            "text": "#FAFAFA",
            "border": "#434358"
        }
    else:
        return {
            "primary": "#4CAF50",
            "background": "#FFFFFF",
            "secondary_background": "#F0F2F6",
            "text": "#31333F",
            "border": "#DCDCDC"
        }