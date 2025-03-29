import streamlit as st
from utils.theme import get_theme, get_theme_colors

def set_page_config():
    """Set common page configuration with theme support"""
    theme = get_theme()
    st.set_page_config(
        page_title="FarmAI",
        page_icon="🌾",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Inject custom CSS with theme variables
    colors = get_theme_colors()
    custom_css = f"""
    <style>
        :root {{
            --primary: {colors['primary']};
            --background: {colors['background']};
            --secondary-background: {colors['secondary_background']};
            --text: {colors['text']};
            --border: {colors['border']};
        }}
        {open("assets/styles.css").read()}
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def apply_theme():
    """Apply theme-specific Streamlit configurations"""
    theme = get_theme()
    colors = get_theme_colors()
    
    # Set Streamlit theme config (for native components)
    st._config.set_option("theme.primaryColor", colors["primary"])
    st._config.set_option("theme.backgroundColor", colors["background"])
    st._config.set_option("theme.secondaryBackgroundColor", colors["secondary_background"])
    st._config.set_option("theme.textColor", colors["text"])
    
    # Apply custom theme to matplotlib/plotly if needed
    try:
        import matplotlib.pyplot as plt
        plt.style.use('dark_background' if theme == "dark" else 'default')
    except:
        pass