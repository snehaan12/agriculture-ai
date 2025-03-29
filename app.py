import streamlit as st
from utils.auth import authenticate
from utils.helpers import set_page_config, apply_theme
from utils.theme import toggle_theme

def main():
    # Set page configuration with theme support
    set_page_config()
    
    # Apply the selected theme
    apply_theme()
    
    # Check authentication
    if not authenticate():
        return
    
    # Theme toggle in sidebar
    with st.sidebar:
        st.title("FarmAI Navigation")
        st.image("assets/images/logo.png", width=150)
        if st.button("🌙/☀️ Toggle Theme"):
            toggle_theme()
            st.experimental_rerun()
    
    # Main content with theme-aware styling
    st.title("🌾 FarmAI - Precision Agriculture")
    st.markdown("""
    <div class="text-content">
    Welcome to FarmAI, your AI-powered agricultural assistant providing real-time, 
    localized insights for better farming decisions.
    </div>
    """, unsafe_allow_html=True)
    
    # Display key metrics with theme-aware cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Field Health", "Good", "5% ↑", 
                 help="Overall health of your crops")
    with col2:
        st.metric("Soil Moisture", "62%", "-3% ↓", 
                 help="Current soil moisture level")
    with col3:
        st.metric("Pest Risk", "Low", "2% ↓", 
                 help="Risk of pest infestation")
    
    # Quick actions with theme-aware buttons
    st.subheader("Quick Actions")
    action_col1, action_col2, action_col3 = st.columns(3)
    with action_col1:
        st.button("🌱 Check Crop Health", 
                 help="Analyze crop health using satellite data")
    with action_col2:
        st.button("💧 Get Irrigation Advice", 
                 help="Get AI-powered watering recommendations")
    with action_col3:
        st.button("🛠️ Account Settings", 
                 help="Update your profile and preferences")
    
    # Recent alerts with theme-aware styling
    st.subheader("Recent Alerts")
    with st.expander("View Alerts", expanded=True):
        st.warning("⚠️ Low soil moisture detected in North field")
        st.info("ℹ️ Fertilizer application recommended next week")
    
    # Field map placeholder with theme border
    st.subheader("Field Map")
    st.image("assets/images/field-map-placeholder.jpg", 
             caption="Your field overview", 
             use_column_width=True)

if __name__ == "__main__":
    main()