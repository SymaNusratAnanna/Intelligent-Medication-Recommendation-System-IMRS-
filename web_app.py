# web_app.py - FINAL 100% WORKING VERSION (Cards SHOW UP!)
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
    medicine_details = {
        "Paracetamol 500mg": {"primary_use": "Analgesic & Antipyretic (Pain & Fever relief)", "drug_class": "Non-opioid analgesic", "dosage_form": "Tablet, 500mg", "duration": "4-6 hours", "key_info": "First-line for mild-moderate pain. Max 4g/day. Avoid alcohol."},
        "Ibuprofen 400mg": {"primary_use": "NSAID - Inflammation, Pain, Fever", "drug_class": "Non-steroidal anti-inflammatory", "dosage_form": "Tablet, 400mg", "duration": "6-8 hours", "key_info": "Take with food. Caution in GI issues, kidney problems."},
        "Amoxicillin 250mg": {"primary_use": "Bacterial infections treatment", "drug_class": "Penicillin antibiotic", "dosage_form": "Capsule, 250mg", "duration": "7-10 day course", "key_info": "Complete full course. May cause GI upset. Check for penicillin allergy."},
        "Cetirizine 10mg": {"primary_use": "Antihistamine for allergy relief", "drug_class": "H1-receptor antagonist", "dosage_form": "Tablet, 10mg", "duration": "24 hours", "key_info": "Non-drowsy formula. Take once daily. Avoid with CNS depressants."},
        "Omeprazole 20mg": {"primary_use": "Acid reflux & ulcer treatment", "drug_class": "Proton pump inhibitor", "dosage_form": "Capsule, 20mg", "duration": "Once daily, 4-8 weeks", "key_info": "Take before meals. Not for immediate relief. Long-term use requires monitoring."},
        "Aspirin 100mg": {"primary_use": "Pain relief & heart attack prevention", "drug_class": "Anti-platelet", "dosage_form": "Tablet, 100mg", "duration": "Once daily", "key_info": "Low-dose for cardiovascular protection. GI bleeding risk."},
        "Atorvastatin 10mg": {"primary_use": "Cholesterol reduction", "drug_class": "Statin", "dosage_form": "Tablet, 10mg", "duration": "Once daily", "key_info": "Take evening. Monitor liver function. Report muscle pain."},
        "Metformin 500mg": {"primary_use": "Type 2 diabetes management", "drug_class": "Biguanide", "dosage_form": "Tablet, 500mg", "duration": "Twice daily", "key_info": "Take with food. GI side effects common. Avoid in kidney impairment."},
        "Salbutamol Inhaler": {"primary_use": "Asthma & COPD symptom relief", "drug_class": "Bronchodilator", "dosage_form": "Inhaler", "duration": "4-6 hours as needed", "key_info": "Rescue medication. Shake well before use. Not for daily prevention."},
    }
    name = medicine.get('name', '')
    return medicine_details.get(name, {
        "primary_use": medicine.get('primary_use', 'Symptom management'),
        "drug_class": medicine.get('category', 'Medication'),
        "dosage_form": "Tablet/Capsule",
        "duration": "As directed",
        "key_info": medicine.get('key_info', 'Consult healthcare professional for proper usage.')
    })

# FIXED & BEAUTIFUL MEDICINE CARD - ALL DIVS CLOSED!
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
            <div><strong>Primary Use:</strong><br><span style="opacity: 0.9;">{info['primary_use']}</span></div>
            <div><strong>Classification:</strong><br><span style="opacity: 0.9;">{info['drug_class']}</span></div>
            <div><strong>Formulation:</strong><br><span style="opacity: 0.9;">{info['dosage_form']}</span></div>
            <div><strong>Duration:</strong><br><span style="opacity: 0.9;">{info['duration']}</span></div>
        </div>
        <div style="margin-top: 1rem; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 12px;">
            <strong>Important Information:</strong><br>
            <span style="opacity: 0.9; font-size: 0.9rem;">{info['key_info']}</span>
        </div>
        <div style="margin-top: 0.8rem; text-align: right; opacity: 0.8; font-size: 0.9rem;">
            {medicine['price_category']} • {medicine['category']}
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.progress(medicine['safety_rating'] / 5.0)

# Your original CSS - PERFECT
st.markdown("""
<style>
    .main-header {font-size: 4rem; background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4);
                  -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; font-weight: 800;}
    @keyframes gradient {0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; }}
    .glass-card {background: rgba(255,255,255,0.25); backdrop-filter: blur(10px); border-radius: 20px; padding: 2rem; margin: 1rem 0; box-shadow: 0 8px 32px rgba(0,0,0,0.1);}
    .glass-card:hover {transform: translateY(-5px); box-shadow: 0 15px 40px rgba(0,0,0,0.2);}
    .medicine-card-premium {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white; padding: 2rem; border-radius: 20px; margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3); border-left: 5px solid #ff6b6b;
        transition: all 0.4s ease;
    }
    .medicine-card-premium:hover {transform: translateY(-8px); box-shadow: 0 20px 40px rgba(102, 126, 234, 0.4);}
    .stProgress > div > div {background: linear-gradient(90deg, #4CAF50 0%, #8BC34A 50%, #FFEB3B 100%); border-radius: 10px;}
    .floating {animation: floating 3s ease-in-out infinite;}
    @keyframes floating {0% { transform: translate(0, 0px); } 50% { transform: translate(0, 15px); } 100% { transform: translate(0, -0px); }}
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

selected = st.session_state.selected

# DASHBOARD - CARDS NOW SHOW!
if selected == "Dashboard":
    st.markdown("""
    <div class="glass-card">
        <div style='text-align: center; padding: 2rem;'>
            <h1 style='color: #667eea; margin-bottom: 1rem;'>Welcome to MediMatch Pro!</h1>
            <p style='font-size: 1.3rem; color: #666; line-height: 1.6;'>
            Your intelligent AI-powered medicine recommendation system.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    symptoms = st.text_input("**Describe your symptoms:**", placeholder="fever, headache, pain, cough, allergy")
    
    if symptoms:
        with st.spinner("Analyzing..."):
            results = recommender.recommend_by_symptoms(symptoms)
        if results:
            st.success(f"Found {len(results)} matching medicines!")
            for med in results:
                display_medicine_card(med)
        else:
            st.warning("No medicine found. Try: fever, cough, pain, allergy")

# SYMPTOM ANALYZER - CARDS NOW SHOW!
elif selected == "Symptom Analyzer":
    st.markdown("""
    <div style='background: #1a1a1a; padding: 2rem; border-radius: 15px; margin: 1rem 0;'>
        <h1 style='color: #667eea; text-align: center;'>AI Recommendations</h1>
    </div>
    """, unsafe_allow_html=True)
    
    user_symptoms = st.text_area("Describe Your Symptoms", height=150, placeholder="e.g. I have fever, body pain and cough")
    
    col1, col2 = st.columns(2)
    with col1:
        min_safety = st.slider("**Safety**", 1.0, 5.0, 3.5, 0.1)
    with col2:
        price_filter = st.selectbox("**Price**", ["Any", "Economy", "Standard", "Premium"])
    
    if st.button("Analyze Symptoms", type="primary"):
        if user_symptoms:
            with st.spinner("Analyzing..."):
                results = recommender.recommend_by_symptoms(user_symptoms)
                filtered = [m for m in results if m['safety_rating'] >= min_safety]
                if price_filter != "Any":
                    filtered = [m for m in filtered if price_filter in m['price_category']]
            if filtered:
                st.balloons()
                st.success(f"Found {len(filtered)} recommendations!")
                for med in filtered:
                    display_medicine_card(med)
            else:
                st.error("No match found.")
        else:
            st.info("Please enter symptoms.")

# Your other pages (Add Medicine, Database, Analytics, About) remain unchanged
elif selected == "Add Medicine":
    st.markdown("""
    <div class="glass-card">
        <h1 style='color: #667eea; text-align: center;'>Add New Medicine</h1>
    </div>
    """, unsafe_allow_html=True)
    with st.form("add_medicine_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Medicine Name*", placeholder="e.g., Paracetamol 500mg")
            category = st.selectbox("Category*", ["Analgesic", "NSAID", "Antibiotic", "Antihistamine", "Other"])
            safety = st.slider("Safety Rating*", 1.0, 5.0, 4.0)
        with col2:
            price = st.selectbox("Price Category*", ["Economy", "Standard", "Premium"])
            dosage = st.text_input("Dosage Form")
            duration = st.text_input("Duration")
        symptoms = st.text_area("Symptoms Treated*")
        key_info = st.text_area("Key Information")
        submitted = st.form_submit_button("Add Medicine")
        if submitted:
            if name and symptoms:
                success, msg = recommender.add_medicine({
                    'name': name, 'for_symptoms': symptoms, 'category': category,
                    'safety_rating': safety, 'price_category': price, 'key_info': key_info
                })
                st.success("Added!") if success else st.error(msg)

elif selected == "Medicine Database":
    st.markdown("<h2>Medicine Database</h2>", unsafe_allow_html=True)
    df = pd.DataFrame(recommender.get_all_medicines())
    st.dataframe(df[['name', 'category', 'safety_rating']], use_container_width=True)

elif selected == "Analytics":
    st.markdown("<h2>Analytics</h2>", unsafe_allow_html=True)
    df = pd.DataFrame(recommender.get_all_medicines())
    col1, col2 = st.columns(2)
    with col1:
        st.bar_chart(df['category'].value_counts())
    with col2:
        st.line_chart(df['safety_rating'].value_counts().sort_index())

elif selected == "About":
    st.markdown("""
    <div style='background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%); padding: 3rem 2rem; border-radius: 20px; color: white;'>
        <h1 style='color: #667eea; text-align: center;'>Master's Research Project</h1>
        <p style='font-size: 1.2rem; text-align: center; color: #ccc;'>
            MediMatch Pro is an AI-powered medicine recommendation system developed for educational and research purposes.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='text-align: center; padding: 3rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; border-radius: 20px; margin: 2rem 0;'>
    <h3>MediMatch Pro</h3>
    <p>Advanced AI Medicine Recommendation System</p>
    <p>Master's Research Project | Always Consult Professionals</p>
</div>
""", unsafe_allow_html=True)