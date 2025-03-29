import streamlit as st
from utils.api_client import get_irrigation_recommendation
from utils.helpers import set_page_config

set_page_config()

st.title("💧 Irrigation Recommendations")
st.markdown("Get AI-powered irrigation advice for your fields")

# Field selection
field = st.selectbox("Select Field", 
                    ["North Field", "South Field", "East Field", "West Field"])

# Get current conditions
st.subheader("Current Conditions")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Soil Moisture", "58%", "-5% from ideal")
with col2:
    st.metric("Temperature", "32°C", "2°C above average")
with col3:
    st.metric("Rain Forecast", "20% chance", "next 3 days")

# Get recommendation
if st.button("Get Irrigation Recommendation"):
    with st.spinner("Analyzing field conditions..."):
        recommendation = get_irrigation_recommendation(field)
        
        st.success("Recommendation generated!")
        st.subheader("Irrigation Plan")
        
        st.markdown(f"""
        **Recommended Action:** {recommendation['action']}
        
        **Water Amount:** {recommendation['water_amount']} liters/hectare
        
        **Optimal Time:** {recommendation['optimal_time']}
        """)
        
        st.markdown("---")
        st.subheader("Detailed Analysis")
        st.json(recommendation["details"])
        
        # Save as PDF option
        st.download_button(
            label="Download Recommendation as PDF",
            data=generate_pdf(recommendation),
            file_name=f"irrigation_plan_{field.replace(' ', '_')}.pdf",
            mime="application/pdf"
        )

def generate_pdf(data):
    # This would be replaced with actual PDF generation logic
    return "PDF content would be generated here".encode()