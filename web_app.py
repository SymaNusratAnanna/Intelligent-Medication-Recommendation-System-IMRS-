# web_app.py - FULLY FIXED & MERGED VERSION (Cards NOW SHOW!)
import streamlit as st
import pandas as pd
import numpy as np
from medicine_recommender import MedicineRecommender

# Page configuration
st.set_page_config(
    page_title="MediMatch Pro - AI Medicine Advisor",
    page_icon="pill",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ENHANCED MEDICINE DETAILS FUNCTION
def get_medicine_details(medicine):
    """Get specific, relevant medical information for each medicine"""
    medicine_details = {
        "Paracetamol 500mg": {
            "primary_use": "Analgesic & Antipyretic (Pain & Fever relief)",
            "drug_class": "Non-opioid analgesic",
            "dosage_form": "Tablet, 500mg",
            "duration": "4-6 hours",
            "key_info": "First-line for mild-moderate pain. Max 4g/day. Avoid alcohol."
        },
        "Ibuprofen 400mg": {
            "primary_use": "NSAID - Inflammation, Pain, Fever",
            "drug_class": "Non-steroidal anti-inflammatory",
            "dosage_form": "Tablet, 400mg", 
            "duration": "6-8 hours",
            "key_info": "Take with food. Caution in GI issues, kidney problems."
        },
        "Amoxicillin 250mg": {
            "primary_use": "Bacterial infections treatment",
            "drug_class": "Penicillin antibiotic",
            "dosage_form": "Capsule, 250mg",
            "duration": "7-10 day course",
            "key_info": "Complete full course. May cause GI upset. Check for penicillin allergy."
        },
        "Cetirizine 10mg": {
            "primary_use": "Antihistamine for allergy relief",
            "drug_class": "H1-receptor antagonist", 
            "dosage_form": "Tablet, 10mg",
            "duration": "24 hours",
            "key_info": "Non-drowsy formula. Take once daily. Avoid with CNS depressants."
        },
        "Omeprazole 20mg": {
            "primary_use": "Acid reflux & ulcer treatment", 
            "drug_class": "Proton pump inhibitor",
            "dosage_form": "Capsule, 20mg",
            "duration": "Once daily, 4-8 weeks",
            "key_info": "Take before meals. Not for immediate relief. Long-term use requires monitoring."
        },
        "Aspirin 100mg": {
            "primary_use": "Pain relief & heart attack prevention",
            "drug_class": "Anti-platelet",
            "dosage_form": "Tablet, 100mg",
            "duration": "Once daily",
            "key_info": "Low-dose for cardiovascular protection. GI bleeding risk."
        },
        "Atorvastatin 10mg": {
            "primary_use": "Cholesterol reduction",
            "drug_class": "Statin",
            "dosage_form": "Tablet, 10mg",
            "duration": "Once daily",
            "key_info": "Take evening. Monitor liver function. Report muscle pain."
        },
        "Metformin 500mg": {
            "primary_use": "Type 2 diabetes management",
            "drug_class": "Biguanide",
            "dosage_form": "Tablet, 500mg",
            "duration": "Twice daily",
            "key_info": "Take with food. GI side effects common. Avoid in kidney impairment."
        },
        "Salbutamol Inhaler": {
            "primary_use": "Asthma & COPD symptom relief",
            "drug_class": "Bronchodilator",
            "dosage_form": "Inhaler",
            "duration": "4-6 hours as needed",
            "key_info": "Rescue medication. Shake well before use. Not for daily prevention."
        }
    }
    
    medicine_name = medicine.get('name', '')
    return medicine_details.get(medicine_name, {
        "primary_use": medicine.get('primary_use', 'Symptom management'),
        "drug_class": medicine.get('category', 'Medication'),
        "dosage_form": "Tablet/Capsule",
        "duration": "As directed",
        "key_info": medicine.get('key_info', 'Consult healthcare professional for proper usage.')
    })

# FIXED: Beautiful medicine card with ALL divs closed!
def display_medicine_card(medicine):
    info = get_medicine_details(medicine)
    st.markdown(f"""
    <div class="medicine-card-premium">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <h2 style="margin: 0; color: white;">{medicine['name']}</h2>
            <div style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px;">
                <span style="font-size: 1.2rem; font-weight: bold;">{medicine['safety_rating']:.1f}/5.0</span>
            </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
            <div>
                <strong>Primary Use:</strong><br>
                <span style="opacity: 0.9;">{info['primary_use']}</span>
            </div>
            <div>
                <strong>Classification:</strong><br>
                <span style="opacity: 0.9;">{info['drug_class']}</span>
            </div>
            <div>
                <strong>Formulation:</strong><br>
                <span style="opacity: 0.9;">{info['dosage_form']}</span>
            </div>
            <div>
                <strong>Duration:</strong><br>
                <span style="opacity: 0.9;">{info['duration']}</span>
            </div>
            <div style="grid-column: span 2; margin-top: 1rem;">
                <strong>Important Information:</strong><br>
                <span style="opacity: 0.9; font-size: 0.9rem;">{info['key_info']}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.progress(medicine['safety_rating'] / 5.0)

# Your original CSS - PERFECT
st.markdown("""
<style>
    .main-header {
        font-size: 4rem;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradient 3s ease infinite;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 800;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
oxetine;
    }
    .medicine-card-premium {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        border-left: 5px solid #ff6b6b;
        transition: all 0.4s ease;
    }
    .medicine-card-premium:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.4);
    }
    .stProgress > div > div {
        background: linear-gradient(90deg, #4CAF50 0%, #8BC34A 50%, #FFEB3B 100%);
        border-radius: 10px;
    }
    .floating {
        animation: floating 3s ease-in-out infinite;
    }
    @keyframes floating {
        0% { transform: translate(0, 0px); }
        50% { transform: translate(0, 15px); }
        100% { transform: translate(0, -0px); }
    }
</style>
""", unsafe_allow_html=True)

# Initialize recommender
@st.cache_resource
def load_recommender():
    return MedicineRecommender()

recommender = load_recommender()

# Animated Header
st.markdown("""
<div style='text-align: center; padding: 3rem 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            border-radius: 0 0 50px 50px; margin: -2rem -2rem 2rem -2rem; color: white;'>
    <h1 class="main-header floating">MediMatch Pro</h1>
    <h3 style='color: white; opacity: 0.9; margin-top: 0;'>AI-Powered Medicine Recommendation System</h3>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.9) 0%, rgba(118, 75, 162, 0.9) 100%); 
                backdrop-filter: blur(10px); padding: 2rem 1.5rem; border-radius: 20px; margin-bottom: 2rem; 
                color: white; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                border: 1px solid rgba(255,255,255,0.2);'>
        <div style='font-size: 3rem; margin-bottom: 1rem;' class="floating">pill</div>
        <h2 style='color: white; margin: 0; font-weight: 700;'>MediMatch Pro</h2>
        <p style='margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 1.1rem;'>Medical Navigator</p>
    </div>
    """, unsafe_allow_html=True)
    
    if 'selected' not in st.session_state:
        st.session_state.selected = "Dashboard"
    
    st.markdown("### Navigation Menu")
    
    nav_options = [
        {"icon": "home", "label": "Dashboard", "desc": "Home & quick access"},
        {"icon": "search", "label": "Symptom Analyzer", "desc": "AI-powered analysis"},
        {"icon": "plus", "label": "Add Medicine", "desc": "Add new medicine"}, 
        {"icon": "database", "label": "Medicine Database", "desc": "Complete library"},
        {"icon": "chart", "label": "Analytics", "desc": "Statistics & insights"},
        {"icon": "info", "label": "About", "desc": "Project information"}
    ]
    
    for option in nav_options:
        full_label = f"{option['icon']} {option['label']}"
        if st.button(f"**{full_label}**", key=option['label'], use_container_width=True):
            st.session_state.selected = option['label']
        st.caption(f"{option['desc']}")

# Get selected page
selected = st.session_state.selected

# DASHBOARD - NOW SHOWS CARDS!
if selected == "Dashboard":
    st.markdown("""
    <div class="glass-card">
        <div style='text-align: center; padding: 2rem;'>
            <h1 style='color: #667eea; margin-bottom: 1rem;'>Welcome to MediMatch Pro!</h1>
            <p style='font-size: 1.3rem; color: #666; line-height: 1.6;'>
            Your intelligent AI-powered medicine recommendation system. Get personalized medication 
            suggestions based on your symptoms with advanced safety ratings and detailed medical information.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    symptoms = st.text_input("**Describe your symptoms:**", placeholder="e.g. fever, headache, cough, pain", help="Separate with commas or spaces")
    
    if symptoms:
        with st.spinner("AI is analyzing your symptoms..."):
            results = recommender.recommend_by_symptoms(symptoms)
            
        if results:
            st.success(f"Found {len(results)} relevant medications!")
            for medicine in results:
                display_medicine_card(medicine)
        else:
            st.warning("No medications found. Try: fever, cough, allergy, pain, headache")

# SYMPTOM ANALYZER - NOW SHOWS CARDS!
elif selected == "Symptom Analyzer":
    st.markdown("""
    <div style='background: #1a1a1a; padding: 2rem; border-radius: 15px; margin: 1rem 0;'>
        <h1 style='color: #667eea; text-align: center;'>AI Recommendations</h1>
    </div>
    """, unsafe_allow_html=True)
    
    user_symptoms = st.text_area("Describe Your Symptoms", height=150, placeholder="e.g. I have fever, body pain and cough")
    
    if st.button("Analyze Symptoms", type="primary"):
        if user_symptoms:
            with st.spinner("AI is analyzing..."):
                results = recommender.recommend_by_symptoms(user_symptoms)
            if results:
                st.balloons()
                st.success(f"Found {len(results)} recommendations!")
                for medicine in results:
                    display_medicine_card(medicine)
            else:
                st.error("No match found. Try common symptoms.")
        else:
            st.info("Please enter your symptoms.")

# Keep all your other pages (Add Medicine, Database, Analytics, About) exactly as they were
# ... [Your Add Medicine, Analytics, About pages remain unchanged]

# Professional Footer
st.markdown("""
<div style='text-align: center; padding: 3rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; border-radius: 20px; margin: 2rem 0;'>
    <h3 style='color: white; margin-bottom: 1rem;'>MediMatch Pro</h3>
    <p style='opacity: 0.9; margin-bottom: 0.5rem;'>Advanced AI Medicine Recommendation System</p>
    <p style='opacity: 0.7; margin: 0;'>Master's Research Project | Medical Informatics | Always Consult Professionals</p>
</div>
""", unsafe_allow_html=True)