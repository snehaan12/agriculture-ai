import requests
import streamlit as st
import os

BASE_URL = os.getenv("API_BASE_URL", "https://your-api-url.com")

def get_crop_health(start_date, end_date):
    """Get crop health data from API"""
    try:
        response = requests.post(
            f"{BASE_URL}/crop-health",
            json={
                "start_date": str(start_date),
                "end_date": str(end_date)
            }
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching crop health data: {str(e)}")
        return None

def analyze_leaf_image(image_file):
    """Send leaf image for disease analysis"""
    try:
        files = {"file": image_file.getvalue()}
        response = requests.post(f"{BASE_URL}/analyze-leaf", files=files)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error analyzing leaf image: {str(e)}")
        return {
            "disease": "Unknown",
            "confidence": 0,
            "treatment": "Unable to analyze image. Please try again."
        }

def get_irrigation_recommendation(field_name):
    """Get irrigation recommendations"""
    try:
        response = requests.post(
            f"{BASE_URL}/irrigation",
            json={"field": field_name}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error getting irrigation recommendation: {str(e)}")
        return {
            "action": "Unable to generate recommendation",
            "water_amount": 0,
            "optimal_time": "Unknown",
            "details": {}
        }