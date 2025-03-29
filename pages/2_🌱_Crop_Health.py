import streamlit as st
from utils.api_client import get_crop_health, analyze_leaf_image
from utils.helpers import set_page_config
import datetime

set_page_config()

st.title("🌱 Crop Health Analysis")
st.markdown("Monitor your crops' health using satellite data and AI analysis")

# Tab layout
tab1, tab2 = st.tabs(["Satellite Analysis", "Disease Detection"])

with tab1:
    st.subheader("Field Health from Satellite")
    
    # Date selection
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start date", 
                                  datetime.date.today() - datetime.timedelta(days=30))
    with col2:
        end_date = st.date_input("End date", datetime.date.today())
    
    if st.button("Analyze Field Health"):
        with st.spinner("Processing satellite data..."):
            health_data = get_crop_health(start_date, end_date)
            
            st.success("Analysis complete!")
            st.json(health_data)
            
            # Visualizations
            st.subheader("NDVI Analysis")
            st.line_chart({
                "Healthy": health_data["healthy_areas"],
                "Moderate": health_data["moderate_areas"],
                "Stressed": health_data["stressed_areas"]
            })

with tab2:
    st.subheader("Leaf Disease Detection")
    st.markdown("Upload images of plant leaves to detect diseases")
    
    uploaded_file = st.file_uploader("Choose a leaf image", 
                                   type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", width=300)
        
        if st.button("Analyze for Diseases"):
            with st.spinner("Analyzing image..."):
                result = analyze_leaf_image(uploaded_file)
                
                st.subheader("Results")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Disease Detected", result["disease"])
                with col2:
                    st.metric("Confidence", f"{result['confidence']*100:.1f}%")
                
                st.subheader("Recommended Treatment")
                st.info(result["treatment"])
                
                st.markdown("---")
                st.markdown("**Prevention Tips**")
                st.write("""
                - Rotate crops regularly
                - Ensure proper spacing between plants
                - Monitor field humidity levels
                - Remove infected plants immediately
                """)