import streamlit as st
import pandas as pd
from medicine_recommender import MedicineRecommender

# Page configuration
st.set_page_config(
    page_title="MediMatch - Medicine Recommender",
    page_icon="💊",
    layout="wide"
)

# Title and description
st.title("💊 MediMatch - Intelligent Medicine Recommendation System")
st.markdown("### Your AI-powered assistant for medication suggestions")

# Initialize recommender
@st.cache_resource
def load_recommender():
    return MedicineRecommender()

recommender = load_recommender()

# Sidebar
st.sidebar.header("🔧 Navigation")
option = st.sidebar.selectbox(
    "Choose an option:",
    ["🏠 Home", "🔍 Symptom Checker", "📚 Medicine Database", "ℹ️ About"]
)

if option == "🏠 Home":
    st.header("Welcome to MediMatch!")
    st.write("""
    This system helps you find appropriate medications based on your symptoms.
    Please consult a healthcare professional before taking any medication.
    """)