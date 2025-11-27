# web_app.py - Web Interface for Medicine Recommender
import streamlit as st
import pandas as pd
from medicine_recommender import MedicineRecommender

# Configure the page
st.set_page_config(
    page_title="MediMatch - Medicine Recommender",
    page_icon="💊",
    layout="wide"
)

# Title
st.title("💊 MediMatch - Medicine Recommendation System")
st.markdown("### AI-Powered Medicine Suggestions Based on Symptoms")

# Initialize your recommender system
@st.cache_resource
def load_recommender():
    return MedicineRecommender()

recommender = load_recommender()

# Sidebar navigation
st.sidebar.header("🔧 Navigation")
option = st.sidebar.radio(
    "Choose what you want to do:",
    ["🏠 Home", "🔍 Check Symptoms", "📚 View All Medicines"]
)

if option == "🏠 Home":
    st.header("Welcome to MediMatch!")
    st.write("""
    This intelligent system helps you find appropriate medications based on your symptoms.
    Enter your symptoms to get personalized recommendations.
    """)
    
    # Quick symptom check
    st.subheader("Quick Symptom Check")
    symptoms = st.text_input("What symptoms are you experiencing? (e.g., fever, headache, pain)")
    
    if symptoms:
        with st.spinner("🔍 Finding the best medications for you..."):
            results = recommender.recommend_by_symptoms(symptoms)
            
        if results:
            st.success(f"✅ Found {len(results)} recommendation(s) for: **{symptoms}**")
            
            for i, medicine in enumerate(results, 1):
                with st.expander(f"{i}. 💊 {medicine['name']}", expanded=True):
                    st.write(f"**Treats:** {medicine['for_symptoms']}")
                    st.write(f"**Type:** {medicine['category']}")
                    st.write(f"**Safety Rating:** ⭐ {medicine['safety_rating']}/5.0")
                    
                    # Visual safety rating
                    safety_percent = (medicine['safety_rating'] / 5.0) * 100
                    st.progress(safety_percent / 100)
        else:
            st.warning("❌ No medications found for these symptoms. Please try different symptoms.")

elif option == "🔍 Check Symptoms":
    st.header("🔍 Detailed Symptom Analysis")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Enter Your Symptoms")
        user_symptoms = st.text_area(
            "Describe all your symptoms (separate with commas):",
            placeholder="fever, headache, body pain, inflammation",
            height=100
        )
        
        # Additional options
        st.subheader("🔧 Filters")
        min_safety = st.slider("Minimum Safety Rating", 1.0, 5.0, 3.5)
        
    with col2:
        if user_symptoms:
            st.subheader("💡 Recommendations")
            results = recommender.recommend_by_symptoms(user_symptoms)
            
            if results:
                # Apply safety filter
                filtered_results = [med for med in results if med['safety_rating'] >= min_safety]
                
                if filtered_results:
                    st.success(f"🎯 Found {len(filtered_results)} suitable medication(s)")
                    
                    for medicine in filtered_results:
                        st.markdown(f"### 💊 {medicine['name']}")
                        st.write(f"**For:** {medicine['for_symptoms']}")
                        st.write(f"**Category:** {medicine['category']}")
                        st.write(f"**Safety:** {medicine['safety_rating']}/5.0 ⭐")
                        st.markdown("---")
                else:
                    st.warning("No medications meet your safety criteria.")
            else:
                st.error("No medications found for these symptoms.")

elif option == "📚 View All Medicines":
    st.header("📚 Medicine Database")
    
    # Show all medicines in a nice table
    all_medicines = recommender.get_all_medicines()
    
    if all_medicines:
        st.write(f"**Total medicines in database:** {len(all_medicines)}")
        
        # Create a pandas DataFrame for better display
        df = pd.DataFrame(all_medicines)
        st.dataframe(df, use_container_width=True)
    else:
        st.error("No medicines found in the database.")

# Footer
st.markdown("---")
st.markdown("⚕️ **Important:** This system is for educational purposes. Always consult a healthcare professional before taking any medication.")
st.markdown("🔬 **MediMatch - Master's Project - Intelligent Medicine Recommendation System**")