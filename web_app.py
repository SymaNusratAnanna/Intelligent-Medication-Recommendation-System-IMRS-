# web_app.py - Enhanced Web Interface for Medicine Recommender
import streamlit as st
import pandas as pd
from medicine_recommender import MedicineRecommender
from streamlit_option_menu import option_menu

# Page configuration
st.set_page_config(
    page_title="MediMatch - AI Medicine Advisor",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .medicine-card {
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        background-color: #f0f8ff;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .symptom-input {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
    }
    .success-box {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #28a745;
    }
</style>
""", unsafe_allow_html=True)

# Initialize your recommender system
@st.cache_resource
def load_recommender():
    return MedicineRecommender()

recommender = load_recommender()

# Header with logo and title
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<h1 class="main-header">💊 MediMatch</h1>', unsafe_allow_html=True)
    st.markdown("### AI-Powered Medicine Recommendation System")

# Sidebar navigation with enhanced menu
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2069/2069571.png", width=100)
    selected = option_menu(
        menu_title="🔧 Navigation",
        options=["🏠 Home", "🔍 Symptom Checker", "📊 Medicine Database", "ℹ️ About"],
        icons=['house', 'search-heart', 'capsule', 'info-circle'],
        default_index=0,
    )

# Home Page
if selected == "🏠 Home":
    st.markdown("---")
    
    # Hero Section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("## Welcome to MediMatch! 🩺")
        st.markdown("""
        Your intelligent AI-powered medicine recommendation system. 
        Get personalized medication suggestions based on your symptoms with safety ratings and detailed information.
        """)
    
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/2964/2964516.png", width=150)
    
    # Quick Symptom Checker
    st.markdown("---")
    st.markdown("## 🔍 Quick Symptom Check")
    
    with st.container():
        symptoms = st.text_input(
            "Enter your symptoms (comma separated):",
            placeholder="fever, headache, pain...",
            help="Separate multiple symptoms with commas"
        )
        
        if symptoms:
            with st.spinner("🔍 Analyzing your symptoms..."):
                results = recommender.recommend_by_symptoms(symptoms)
                
            if results:
                st.markdown(f'<div class="success-box">✅ Found {len(results)} recommendation(s) for your symptoms</div>', unsafe_allow_html=True)
                
                # Display results in beautiful cards
                for i, medicine in enumerate(results, 1):
                    with st.expander(f"💊 {medicine['name']} - ⭐ {medicine['safety_rating']}/5.0", expanded=True):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**Treats:** {medicine['for_symptoms']}")
                            st.write(f"**Type:** {medicine['category']}")
                        with col2:
                            st.write(f"**Safety Rating:** ⭐ {medicine['safety_rating']}/5.0")
                            safety_percent = (medicine['safety_rating'] / 5.0) * 100
                            st.progress(safety_percent / 100)
            else:
                st.warning("❌ No medications found for these symptoms. Please try different symptoms.")

# Symptom Checker Page
elif selected == "🔍 Symptom Checker":
    st.markdown("## 🔍 Detailed Symptom Analysis")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Enter Your Symptoms")
        user_symptoms = st.text_area(
            "Describe all your symptoms in detail:",
            placeholder="fever, headache, body pain, inflammation...",
            height=100
        )
        
        # Additional filters
        st.markdown("### 🔧 Filters")
        min_safety = st.slider("Minimum Safety Rating", 1.0, 5.0, 3.5, 0.1)
    
    with col2:
        if user_symptoms:
            st.markdown("### 💡 Recommendations")
            
            with st.spinner("🔍 Finding the best medications..."):
                results = recommender.recommend_by_symptoms(user_symptoms)
            
            if results:
                # Apply safety filter
                filtered_results = [med for med in results if med['safety_rating'] >= min_safety]
                
                if filtered_results:
                    st.success(f"🎯 Found {len(filtered_results)} suitable medication(s)")
                    
                    for medicine in filtered_results:
                        with st.container():
                            st.markdown(f'<div class="medicine-card">', unsafe_allow_html=True)
                            st.markdown(f"### 💊 {medicine['name']}")
                            
                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.write(f"**Type:** {medicine['category']}")
                                st.write(f"**Treats:** {medicine['for_symptoms']}")
                            with col2:
                                st.write(f"**Safety:** ⭐ {medicine['safety_rating']}/5.0")
                                st.progress(medicine['safety_rating']/5.0)
                            with col3:
                                st.write(f"**ID:** {medicine.get('medicine_id', 'N/A')}")
                            
                            st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.warning("❌ No medications meet your safety criteria.")
            else:
                st.error("❌ No medications found for these symptoms.")

# Medicine Database Page
elif selected == "📊 Medicine Database":
    st.markdown("## 📊 Complete Medicine Database")
    
    # Search functionality
    search_col1, search_col2 = st.columns([2, 1])
    with search_col1:
        search_term = st.text_input("🔍 Search medicines by name or category:")
    
    # Get all medicines
    all_medicines = recommender.get_all_medicines()
    
    if all_medicines:
        # Filter if search term exists
        if search_term:
            filtered_meds = [med for med in all_medicines 
                           if search_term.lower() in med['name'].lower() 
                           or search_term.lower() in med['category'].lower()]
        else:
            filtered_meds = all_medicines
        
        # Create a beautiful dataframe
        df = pd.DataFrame(filtered_meds)
        if not df.empty:
            # Enhanced dataframe display
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "name": "Medicine Name",
                    "category": "Category",
                    "for_symptoms": "Treats Symptoms",
                    "safety_rating": st.column_config.ProgressColumn(
                        "Safety Rating",
                        help="Safety rating out of 5",
                        format="%.1f",
                        min_value=0,
                        max_value=5,
                    ),
                }
            )
            
            # Statistics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Medicines", len(filtered_meds))
            with col2:
                avg_safety = df['safety_rating'].mean()
                st.metric("Average Safety", f"{avg_safety:.1f}/5.0")
            with col3:
                st.metric("Categories", df['category'].nunique())
        else:
            st.warning("No medicines found matching your search.")
    else:
        st.error("No medicines found in the database.")

# About Page
elif selected == "ℹ️ About":
    st.markdown("## ℹ️ About MediMatch")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### 🎓 Master's Project - Intelligent Medicine Recommendation System
        
        **MediMatch** is an AI-powered medicine recommendation system developed as part of a Master's degree project.
        
        ### ✨ Features:
        - **Symptom-based medicine recommendations**
        - **Safety rating system** (1-5 stars)
        - **Advanced filtering options**
        - **Professional medical database**
        - **Machine Learning powered suggestions**
        
        ### 🛠️ Technologies Used:
        - **Python** with Streamlit for the web interface
        - **Pandas** for data management
        - **Scikit-learn** for ML algorithms
        - **Professional UI/UX design**
        
        ### ⚕️ Important Notice:
        This system is for **educational purposes only**. Always consult a healthcare professional before taking any medication.
        """)
    
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/2000/2000860.png", width=200)
        st.info("""
        **For Educational Use Only**
        
        Developed as part of academic research in medical informatics and AI applications.
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>⚕️ <strong>MediMatch</strong> - AI Medicine Recommendation System | 🎓 Master's Project</p>
    <p>💡 <em>Always consult a healthcare professional for medical advice</em></p>
</div>
""", unsafe_allow_html=True)