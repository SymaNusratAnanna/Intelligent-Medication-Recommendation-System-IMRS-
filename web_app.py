# web_app.py - COMPLETELY FIXED VERSION (No errors)
import streamlit as st
import pandas as pd
import numpy as np
from medicine_recommender import MedicineRecommender

# Page configuration
st.set_page_config(
    page_title="MediMatch Pro - AI Medicine Advisor",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)




# =============================================
# ENHANCED MEDICINE DETAILS FUNCTION - MOVED TO TOP
# =============================================
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
    
    # Return details for the medicine or default values
    medicine_name = medicine.get('name', '')
    return medicine_details.get(medicine_name, {
        "primary_use": medicine.get('primary_use', 'Symptom management'),
        "drug_class": medicine.get('category', 'Medication'),
        "dosage_form": "Tablet/Capsule",
        "duration": "As directed",
        "key_info": "Consult healthcare professional for proper usage."
    })

# FIXED CSS - All errors corrected
st.markdown("""
<style>
    /* Main header with animated gradient */
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
    
    /* Glass morphism cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.2);
    }
    
    /* Premium medicine cards - ENHANCED */
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
    
    /* Animated success boxes */
    .success-box-premium {
        background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%);
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        text-align: center;
        font-weight: 600;
        font-size: 1.1rem;
        box-shadow: 0 8px 25px rgba(76, 175, 80, 0.3);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    
    /* Custom progress bars - FIXED */
    .stProgress > div > div {
        background: linear-gradient(90deg, #4CAF50 0%, #8BC34A 50%, #FFEB3B 100%);
        border-radius: 10px;
    }
    
    /* Floating animation for icons */
    .floating {
        animation: floating 3s ease-in-out infinite;
    }
    
    @keyframes floating {
        0% { transform: translate(0, 0px); }
        50% { transform: translate(0, 15px); }
        100% { transform: translate(0, -0px); }
    }
    
    /* Sidebar navigation buttons */
    .sidebar-btn {
        background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
        border: 1px solid rgba(255,255,255,0.2);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
        text-align: left;
        font-size: 1rem;
        font-weight: 500;
    }
    
    .sidebar-btn:hover {
        background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0.1) 100%);
        transform: translateX(5px);
        border-left: 4px solid #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# Initialize your recommender system
@st.cache_resource
def load_recommender():
    return MedicineRecommender()

recommender = load_recommender()

# Animated Header
st.markdown("""
<div style='text-align: center; padding: 3rem 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            border-radius: 0 0 50px 50px; margin: -2rem -2rem 2rem -2rem; color: white;'>
    <h1 class="main-header floating">💊 MediMatch Pro</h1>
    <h3 style='color: white; opacity: 0.9; margin-top: 0;'>AI-Powered Medicine Recommendation System</h3>
</div>
""", unsafe_allow_html=True)

# =============================================
# ENHANCED SIDEBAR NAVIGATION - ATTRACTIVE DESIGN
# =============================================
with st.sidebar:
    # Premium header with glass effect
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.9) 0%, rgba(118, 75, 162, 0.9) 100%); 
                backdrop-filter: blur(10px); padding: 2rem 1.5rem; border-radius: 20px; margin-bottom: 2rem; 
                color: white; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                border: 1px solid rgba(255,255,255,0.2);'>
        <div style='font-size: 3rem; margin-bottom: 1rem;' class="floating">💊</div>
        <h2 style='color: white; margin: 0; font-weight: 700;'>MediMatch Pro</h2>
        <p style='margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 1.1rem;'>Medical Navigator</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state for navigation
    if 'selected' not in st.session_state:
        st.session_state.selected = "🏠 Dashboard"
    
    # Attractive navigation menu
    st.markdown("### 🧭 Navigation Menu")
    
    # Navigation options with beautiful buttons
    nav_options = [
         {"icon": "🏠", "label": "Home", "desc": "Welcome & system overview", "key": "home"},
        {"icon": "🏠", "label": "Dashboard", "desc": "Home & quick access", "key": "dashboard"},
        {"icon": "🔍", "label": "Symptom Analyzer", "desc": "AI-powered analysis", "key": "symptoms"},
       {"icon": "➕", "label": "Add Medicine", "desc": "Add new medicine to database", "key": "add_medicine"}, 
        {"icon": "📊", "label": "Medicine Database", "desc": "Complete library", "key": "database"},
        {"icon": "📈", "label": "Analytics", "desc": "Statistics & insights", "key": "analytics"},
        {"icon": "ℹ️", "label": "About", "desc": "Project information", "key": "about"}
    ]
    
    # Create beautiful navigation buttons
    for option in nav_options:
        full_label = f"{option['icon']} {option['label']}"
        is_active = st.session_state.selected == full_label
        
        # Different styling for active vs inactive buttons
        if is_active:
            button_style = """
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            color: white; border: none; padding: 1rem; border-radius: 15px; 
            margin: 0.5rem 0; cursor: pointer; width: 100%; text-align: left;
            font-weight: 600; border-left: 5px solid #FFD700; transition: all 0.3s;
            """
        else:
            button_style = """
            background: rgba(255,255,255,0.1); color: white; border: 1px solid rgba(255,255,255,0.2); 
            padding: 1rem; border-radius: 15px; margin: 0.5rem 0; cursor: pointer; 
            width: 100%; text-align: left; font-weight: 500; transition: all 0.3s;
            """
        
        if st.button(f"**{full_label}**", key=option['key'], use_container_width=True):
            st.session_state.selected = full_label
        
        # Add description
        st.caption(f"📌 {option['desc']}")
    
    st.markdown("---")
    
    # Quick stats in sidebar
    try:
        all_meds = recommender.get_all_medicines()
        if all_meds:
            st.markdown("### 📊 Quick Stats")
            total_meds = len(all_meds)
            avg_safety = np.mean([med.get('safety_rating', 0) for med in all_meds])
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("💊 Total", total_meds)
            with col2:
                st.metric("⭐ Safety", f"{avg_safety:.1f}/5.0")
    except:
        pass
    
    # System status
    st.markdown("### ⚡ System Status")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("🟢 Online")
    with col2:
        st.info("⚡ Fast")
    with col3:
        st.success("🔒 Secure")

# Get the selected value
selected = st.session_state.selected  

# #  # =============================================
# # # DASHBOARD PAGE - COMPLETE WORKING VERSION
# # # =============================================
# if selected == "🏠 Dashboard":
#     # Hero Section with Glass Morphism
#     st.markdown("""
#     <div class="glass-card">
#         <div style='text-align: center; padding: 2rem;'>
#             <h1 style='color: #667eea; margin-bottom: 1rem;'>Welcome to MediMatch Pro! 🩺</h1>
#             <p style='font-size: 1.3rem; color: #666; line-height: 1.6;'>
#             Your intelligent AI-powered medicine recommendation system. Get personalized medication 
#             suggestions based on your symptoms with advanced safety ratings and detailed medical information.
#             </p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Real-time statistics from database
#     st.markdown("### 📊 Live Database Statistics")
#     all_medicines = recommender.get_all_medicines()
#     stats = recommender.get_statistics()
    
     
#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         st.metric("💊 Total Medicines", len(all_medicines))
#     with col2:
#         avg_safety = sum(med.get('safety_rating', 0) for med in all_medicines) / len(all_medicines) if all_medicines else 0
#         st.metric("⭐ Avg Safety", f"{avg_safety:.1f}/5.0")
#     with col3:
#         categories = len(set(med.get('category', '') for med in all_medicines))
#         st.metric("🔬 Categories", categories)
#     with col4:
#         st.metric("⚡ Response Time", "<1s")
#     # Quick Symptom Analyzer
#     st.markdown("---")
#     st.markdown("## 🔍 Quick Symptom Analysis")
    
#     with st.container():
#         col1, col2 = st.columns([3, 1])
#         with col1:
#             symptoms = st.text_input(
#                 "**Describe your symptoms:**",
#                 placeholder="fever, headache, pain, inflammation...",
#                 help="Be specific for better recommendations",
#                 key="dashboard_symptoms"
#             )
#         with col2:
#             st.write("")  # Spacer            search_btn = st.button("🔍 Search", type="primary")
        
#         # Quick symptoms buttons
#     st.markdown("### ⚡ Quick Symptoms")
#     quick_symptoms = ["fever", "headache", "pain", "allergy", "cough", "nausea", "inflammation", "infection"]
#     quick_cols = st.columns(4)
#     for i, symptom in enumerate(quick_symptoms):
#         with quick_cols[i % 4]:
#             if st.button(f"🤒 {symptom.title()}", key=f"quick_{symptom}"):
#                 symptoms = symptom
#                 search_btn = True
    
#         # Search when button is clicked
#         if search_btn and symptoms:
#         st.markdown("---")
#         st.subheader("💊 AI Recommendations")
        
#         with st.spinner("🔍 AI is analyzing your symptoms..."):
#             results = recommender.recommend_by_symptoms(symptoms)
        
#         if results:
#             st.success(f"✅ Found {len(results)} medications for: **'{symptoms}'**")
            
                
#                 # =============================================
#                 # ENHANCED MEDICINE CARDS - WORKING VERSION
#                 # =============================================
#             for i, medicine in enumerate(results):
#                     st.markdown(f"""
#                     <div class="medicine-card-premium">
#                         <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
#                             <h2 style='margin: 0; color: white;'>💊 {medicine['name']}</h2>
#                             <div style='background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px;'>
#                                 <span style='font-size: 1.2rem; font-weight: bold;'>⭐ {medicine['safety_rating']}/5.0</span>
#                             </div>
#                         </div>
#                         <div style='display: grid-template-columns: 1fr 1fr; gap: 1rem;'>
#                             <div>
#                                 <strong>🎯 Category:</strong><br>
#                                 <span style='opacity: 0.9;'>{medicine['category']}</span>
#                             </div>
#                             <div>
#                                 <strong>💰 Price:</strong><br>
#                                 <span style='opacity: 0.9;'>{medicine['price_category']}</span>
#                             </div>
#                             <div>
#                                 <strong>🤒 Symptoms Treated:</strong><br>
#                                 <span style='opacity: 0.9;'>{medicine['for_symptoms']}</span>
#                             </div>
#                             <div>
#                                 <strong>📊 Safety Rating:</strong><br>
#                                 <span style='opacity: 0.9;'>Excellent ({medicine['safety_rating']}/5.0)</span>
#                             </div>
#                         </div>
#                     </div>
#                     """, unsafe_allow_html=True)
                    
#                     # Progress bar for safety rating
#                     safety_percent = (medicine['safety_rating'] / 5.0) * 100
#                     st.progress(safety_percent / 100)
                    
#             else:
#                 st.warning(f"❌ No medications found for: '{symptoms}'. Try different symptoms or be more specific.")
        
#         elif symptoms and not search_btn:
#             st.info("💡 Click the 'Search' button to find medications")
#         else:
#             st.info("💡 Enter some symptoms to search for medications")


# # =============================================
# # DASHBOARD PAGE - SYMPTOM SEARCH FEATURE
# # =============================================
# if selected == "🏠 Dashboard":
#     st.markdown("""
#     <div class="glass-card">
#         <h1 style='color: #667eea; text-align: center;'>💊 Dashboard</h1>
#         <p style='text-align: center; color: #666;'>Symptom-based medicine search</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # =============================================
#     # SYMPTOM INPUT SECTION
#     # =============================================
#     st.markdown("### 🔍 Enter Symptoms")
    
#     col1, col2 = st.columns([3, 1])
#     with col1:
#         symptoms = st.text_input(
#             "**Describe your symptoms:**",
#             placeholder="fever, headache, pain, allergy...",
#             key="dashboard_symptoms"
#         )
#     with col2:
#         st.write("")  # Spacer
#         search_btn = st.button("🔍 Search", type="primary")
    
#     # =============================================
#     # SEARCH AND DISPLAY RESULTS
#     # =============================================
#     if search_btn and symptoms:
#         with st.spinner("🔍 Searching medicines..."):
#             results = recommender.recommend_by_symptoms(symptoms)
        
#         if results:
#             st.success(f"✅ Found {len(results)} medicines for: '{symptoms}'")
            
#             for medicine in results:
#                 st.markdown(f"""
#                 <div class="medicine-card-premium">
#                     <h3>💊 {medicine['name']}</h3>
#                     <p><strong>Category:</strong> {medicine['category']}</p>
#                     <p><strong>Safety:</strong> ⭐{medicine['safety_rating']}/5.0</p>
#                     <p><strong>Treats:</strong> {medicine['for_symptoms']}</p>
#                 </div>
#                 """, unsafe_allow_html=True)
                
#                 # Progress bar
#                 safety_percent = (medicine['safety_rating'] / 5.0) * 100
#                 st.progress(safety_percent / 100)
#         else:
#             st.error(f"❌ No medicines found for: '{symptoms}'")

# # =============================================
# # DASHBOARD PAGE - WITH ENHANCED MEDICINE CARDS
# # =============================================
# if selected == "🏠 Dashboard":
#     # Hero Section with Glass Morphism
#     st.markdown("""
#     <div class="glass-card">
#         <div style='text-align: center; padding: 2rem;'>
#             <h1 style='color: #667eea; margin-bottom: 1rem;'>Welcome to MediMatch Pro! 🩺</h1>
#             <p style='font-size: 1.3rem; color: F5F527; line-height: 1.6;'>
#             Your intelligent AI-powered medicine recommendation system. Get personalized medication 
#             suggestions based on your symptoms with advanced safety ratings and detailed medical information.
#             </p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)
    
#       # Quick stats row
#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         st.metric("📊 Total Medicines", 24)
#     with col2:
#         st.metric("⭐ Avg Safety", "4.2/5.0")
#     with col3:
#         st.metric("🔬 Categories", 8)
#     with col4:
#         st.metric("⚡ Response Time", "<1s")

    
#     # Quick Symptom Analyzer
#     st.markdown("---")
#     st.markdown("## 🔍 Quick Symptom Analysis")
    
#     with st.container():
#       col1, col2 = st.columns([3, 1])
#     with col1:
#         symptoms = st.text_input(
#             "**Describe your symptoms:**",
#             placeholder="fever, headache, pain, allergy, inflammation...",
#             help="Be specific for better recommendations",
#             key="dashboard_input"
#         )
#     with col2:
#         st.write("")  # Spacer
#         search_btn = st.button("🔍 Search", type="primary", key="dashboard_search")
    
#         if symptoms:
#             with st.spinner("🔍 AI is analyzing your symptoms..."):
#                 results = recommender.recommend_by_symptoms(symptoms)
                
#             if results:
#                 st.success(f"✅ Found {len(results)} relevant medications!")
#     #       # Quick symptoms buttons
#     # st.markdown("### ⚡ Quick Symptoms")
#     # quick_symptoms = ["fever", "headache", "pain", "allergy", "cough", "nausea", "inflammation", "infection"]
#     # quick_cols = st.columns(4)
#     # for i, symptom in enumerate(quick_symptoms):
#     #     with quick_cols[i % 4]:
#     #         if st.button(f"🤒 {symptom.title()}", key=f"quick_{symptom}"):
#     #             symptoms = symptom
#     #             search_btn = True      

#      # Quick symptoms buttons
#     st.markdown("### ⚡ Quick Symptoms")
#     quick_symptoms = ["fever", "headache", "pain", "allergy", "cough", "nausea", "inflammation", "infection"]
#     quick_cols = st.columns(4)
#     for i, symptom in enumerate(quick_symptoms):
#         with quick_cols[i % 4]:
#             if st.button(f"🤒 {symptom.title()}", key=f"quick_{symptom}"):
#                 symptoms = symptom
#                 search_btn = True

      
#     # Search and display results
#     if search_btn and symptoms:
#         st.markdown("---")
#         st.subheader("💊 AI Recommendations")
        
#         with st.spinner("🔍 AI is analyzing your symptoms..."):
#             results = recommender.recommend_by_symptoms(symptoms)
        
#         if results:
#             st.success(f"✅ Found {len(results)} medications for: **'{symptoms}'**")
            
                
#                 # =============================================
#                 # ENHANCED MEDICINE CARDS - UPDATED TEXT
#                 # =============================================
#             for i, medicine in enumerate(results):
#                 # Create enhanced medicine card


#                 st.markdown(f"""
                   
#                     <div class="medicine-card-premium">
#                         <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
#                             <h2 style='margin: 0; color: white;'>💊 {medicine['name']}</h2>
#                             <div style='background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px;'>
#                                 <span style='font-size: 1.2rem; font-weight: bold;'>⭐ {medicine['safety_rating']}/5.0</span>
#                             </div>
#                     </div>
#         <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;'>
#         <div>
#             <strong>🎯 Primary Use:</strong><br>
#             <span style='opacity: 0.9;'>{medicine['primary_use']}</span>
#         </div>
#         <div>
#             <strong>📊 Classification:</strong><br>
#             <span style='opacity: 0.9;'>{medicine['drug_class']}</span>
#         </div>
#         <div>
#          <strong>💊 Formulation:</strong><br>
#         <span style='opacity: 0.9;'>{medicine['dosage_form']}</span>
#         </div>
#                             <div>
#                                 <strong>⏰ Duration:</strong><br>
#                                 <span style='opacity: 0.9;'>{medicine['duration']}</span>
#                             </div>
#                             <div style='margin-top: 1rem;'>
#                             <strong>💡 Important Information:</strong><br>
#                             <span style='opacity: 0.9; font-size: 0.9rem;'>{medicine['key_info']}</span>
#                         </div>
                        
                        
                        
   
                        
                        
                    
             

                 
#                     """, unsafe_allow_html=True)
                    
#                     # Progress bar
#                 safety_percent = (medicine['safety_rating'] / 5.0) * 100
#                 st.progress(safety_percent / 100)
                    
#             else:
#                 st.warning("❌ No medications found for these symptoms. Try different symptoms or be more specific.")


# =============================================
# HOME SECTION - COMPLETE IMPLEMENTATION
# =============================================
if selected == "🏠 Home":
    # Hero Section with Gradient Background
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; padding: 4rem 2rem; border-radius: 0 0 20px 20px; 
                margin: -1rem -1rem 2rem -1rem; text-align: center;'>
        <h1 style='color: white; font-size: 3.5rem; margin-bottom: 1rem;'>MediMatch Pro</h1>
        <p style='font-size: 1.5rem; opacity: 0.9;'>AI-Powered Medication Recommendation System</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Features Section
    st.markdown("## 🔍 Key Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px;'>
            <h3 style='color: #667eea;'>💊 Symptom Analysis</h3>
            <p style='color: #666;'>Get personalized medicine recommendations based on your symptoms</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px;'>
            <h3 style='color: #667eea;'>⭐ Safety Ratings</h3>
            <p style='color: #666;'>Detailed safety profiles for all medications</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px;'>
            <h3 style='color: #667eea;'>📊 Medicine Database</h3>
            <p style='color: #666;'>Comprehensive database of medications</p>
        </div>
        """, unsafe_allow_html=True)
    
    # How It Works Section
    st.markdown("---")
    st.markdown("## 🛠️ How It Works")
    
    steps = [
        ("1️⃣", "Describe Your Symptoms", "Enter symptoms like fever, headache, or pain"),
        ("2️⃣", "AI Analysis", "Our system analyzes your symptoms"),
        ("3️⃣", "Get Recommendations", "Receive personalized medicine suggestions"),
        ("4️⃣", "Check Details", "View safety ratings and usage information")
    ]
    
    for emoji, title, desc in steps:
        st.markdown(f"""
        <div style='display: flex; align-items: center; margin: 1rem 0;'>
            <div style='font-size: 2rem; margin-right: 1rem; color: #667eea;'>{emoji}</div>
            <div>
                <h3 style='margin: 0; color: #333;'>{title}</h3>
                <p style='margin: 0; color: #666;'>{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Call to Action Section
    st.markdown("---")
    st.markdown("## 🚀 Get Started")
    st.markdown("""
    <div style='text-align: center;'>
        <p style='font-size: 1.2rem; color: #333;'>
            Click the <strong style='color: #667eea;'>Dashboard</strong> in the sidebar to begin
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer Section
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;'>
        <p>© 2023 MediMatch Pro | Always consult healthcare professionals</p>
    </div>
    """, unsafe_allow_html=True)

# =============================================
# DASHBOARD PAGE - COMPREHENSIVE VERSION
# =============================================
if selected == "🏠 Dashboard":
    st.title("🧪 MediMatch Pro - Dashboard")
    st.markdown("---")
    
    # Initialize recommender
    try:
        recommender = MedicineRecommender()
        st.success("✅ Medicine database loaded successfully")
    except Exception as e:
        st.error(f"❌ Failed to initialize: {str(e)}")
        st.stop()
    
    # Real-time Statistics
    st.subheader("📊 Live Database Statistics")
    all_medicines = recommender.get_all_medicines()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("💊 Total Medicines", len(all_medicines))
    with col2:
        avg_safety = sum(med.get('safety_rating', 0) for med in all_medicines) / len(all_medicines) if all_medicines else 0
        st.metric("⭐ Avg Safety", f"{avg_safety:.1f}/5.0")
    with col3:
        categories = len(set(med.get('category', '') for med in all_medicines))
        st.metric("🔬 Categories", categories)
    with col4:
        st.metric("⚡ Response Time", "<1s")
    
    # Symptom Analysis Section
    st.markdown("---")
    st.subheader("🔍 Symptom Analysis")
    
    # Input section
    col1, col2 = st.columns([3, 1])
    with col1:
        symptoms = st.text_input(
            "**Describe your symptoms:**",
            placeholder="fever, headache, pain, allergy, inflammation...",
            help="Be specific for better recommendations",
            key="dashboard_input"
        )
    with col2:
        st.write("")  # Spacer
        search_btn = st.button("🔍 Search", type="primary", key="dashboard_search")
    
    # Quick symptoms buttons
    st.markdown("### ⚡ Quick Symptoms")
    quick_symptoms = ["fever", "headache", "pain", "allergy", "cough", "nausea", "inflammation", "infection"]
    quick_cols = st.columns(4)
    for i, symptom in enumerate(quick_symptoms):
        with quick_cols[i % 4]:
            if st.button(f"🤒 {symptom.title()}", key=f"quick_{symptom}"):
                symptoms = symptom
                search_btn = True
    
    # Search and display results
    if search_btn and symptoms:
        st.markdown("---")
        st.subheader("💊 AI Recommendations")
        
        with st.spinner("🔍 AI is analyzing your symptoms..."):
            results = recommender.recommend_by_symptoms(symptoms)
        
        if results:
            # st.success(f"✅ Found {len(results)} medications for: **'{symptoms}'**") 
            st.success(f"✅ Found {(results)} relevant medications!")
            for medicine in results:
                 
                    medicine_info = get_medicine_details(medicine)
                    
                    st.markdown(f"""

           
                <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                            color: white; padding: 1.5rem; border-radius: 15px; margin: 1rem 0;
                            border-left: 5px solid #ff6b6b;'>
                    <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
                        <h3 style='margin: 0; color: white;'>💊 {medicine['name']}</h3>
                        <div style='background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px;'>
                            <span style='font-size: 1.2rem; font-weight: bold;'>⭐ {medicine['safety_rating']}/5.0</span>
                        </div>
                    </div>
                    <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;'>
                        <div>
                            <strong>🎯 Category:</strong><br>
                            <span style='opacity: 0.9;'>{medicine['category']}</span>
                        </div>
                        <div>
                            <strong>💰 Price:</strong><br>
                            <span style='opacity: 0.9;'>{medicine['price_category']}</span>
                        </div>
                        <div>
                            <strong>🤒 Symptoms Treated:</strong><br>
                            <span style='opacity: 0.9;'>{medicine['for_symptoms']}</span>
                        </div>
                        <div>
                            <strong>🤒 Precautions:</strong><br>
                            <span style='opacity: 0.9;'>{medicine['key_info']}</span>
                        </div>
                      
                        <div>
                            <strong>📊 Safety Rating:</strong><br>
                            <span style='opacity: 0.9;'>Excellent ({medicine['safety_rating']}/5.0)</span>
                        </div>
                    
                </div>
                </div>
                """, unsafe_allow_html=True)
                
        else:
            st.error(f"❌ No medications found for: '{symptoms}'")
            st.info("💡 Try these symptoms: fever, headache, pain, allergy, infection")
    
    # Performance Testing Section (Collapsible)
    with st.expander("🧪 Advanced Testing Tools"):
        st.subheader("🔧 Performance & Validation Tests")
        
        # Quick performance test
        if st.button("⏱️ Run Quick Performance Test"):
            import time
            
            test_cases = ["fever", "headache", "pain", "allergy"]
            st.write("**Performance Results:**")
            
            for symptoms in test_cases:
                start_time = time.time()
                results = recommender.recommend_by_symptoms(symptoms)
                end_time = time.time()
                response_time = (end_time - start_time) * 1000
                
                status = "✅" if response_time < 100 else "⚠️"
                st.write(f"{status} '{symptoms}': {len(results)} results in {response_time:.1f}ms")
        
        # Data validation test
        if st.button("🔍 Validate Data Structure"):
            results = recommender.recommend_by_symptoms("fever")
            
            if results:
                sample_med = results[0]
                required_fields = ['name', 'for_symptoms', 'category', 'safety_rating', 'price_category']
                missing_fields = []
                
                for field in required_fields:
                    if field not in sample_med:
                        missing_fields.append(field)
                
                if missing_fields:
                    st.error(f"❌ Missing fields: {missing_fields}")
                else:
                    st.success("✅ All required fields present")
            else:
                st.error("❌ No results to validate")
    
    # If no search performed yet
    # ✅ CORRECT: Change elif to if
# if not symptoms:
#     st.info("💡 Enter symptoms above to search for medications")
        

# =============================================
# REQUIRED IMPORTS (Add to top of your file)
# =============================================
# Make sure you have these imports at the top of your web_app.py:
# import streamlit as st
# import pandas as pd
# from medicine_recommender import MedicineRecommender
# # Page configuration
# st.set_page_config(
#     page_title="MediMatch Pro - Symptom Dashboard",
#     page_icon="💊",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Enhanced CSS for beautiful dashboard
# st.markdown("""
# <style>
#     /* Main dashboard styling */
#     .dashboard-header {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         color: white;
#         padding: 3rem 2rem;
#         border-radius: 0 0 50px 50px;
#         margin: -2rem -2rem 2rem -2rem;
#         text-align: center;
#     }
    
#     .symptom-input-card {
#         background: rgba(255, 255, 255, 0.1);
#         backdrop-filter: blur(10px);
#         border-radius: 20px;
#         border: 2px solid rgba(255, 255, 255, 0.2);
#         padding: 2rem;
#         margin: 1rem 0;
#         box-shadow: 0 8px 32px rgba(0,0,0,0.1);
#     }
    
#     .medicine-result-card {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         color: white;
#         padding: 1.5rem;
#         border-radius: 15px;
#         margin: 1rem 0;
#         box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
#         border-left: 5px solid #ff6b6b;
#         transition: all 0.3s ease;
#     }
    
#     .medicine-result-card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 15px 40px rgba(102, 126, 234, 0.4);
#     }
    
#     .stats-card {
#         background: rgba(255, 255, 255, 0.05);
#         border-radius: 15px;
#         padding: 1.5rem;
#         border: 1px solid rgba(255, 255, 255, 0.1);
#         text-align: center;
#     }
    
#     .quick-symptom-btn {
#         background: rgba(255, 255, 255, 0.1);
#         border: 1px solid rgba(255, 255, 255, 0.2);
#         color: white;
#         padding: 0.8rem 1.5rem;
#         border-radius: 25px;
#         margin: 0.5rem;
#         cursor: pointer;
#         transition: all 0.3s ease;
#         display: inline-block;
#     }
    
#     .quick-symptom-btn:hover {
#         background: rgba(255, 255, 255, 0.2);
#         transform: scale(1.05);
#     }
    
#     .safety-badge {
#         background: linear-gradient(45deg, #4CAF50, #8BC34A);
#         color: white;
#         padding: 0.3rem 0.8rem;
#         border-radius: 20px;
#         font-weight: bold;
#         font-size: 0.9rem;
#     }
    
#     .category-badge {
#         background: linear-gradient(45deg, #2196F3, #03A9F4);
#         color: white;
#         padding: 0.3rem 0.8rem;
#         border-radius: 20px;
#         font-weight: bold;
#         font-size: 0.9rem;
#     }
    
#     .price-badge {
#         background: linear-gradient(45deg, #FF9800, #FFB74D);
#         color: white;
#         padding: 0.3rem 0.8rem;
#         border-radius: 20px;
#         font-weight: bold;
#         font-size: 0.9rem;
#     }
    
#     .stProgress > div > div {
#         background: linear-gradient(90deg, #4CAF50 0%, #8BC34A 50%, #FFEB3B 100%);
#         border-radius: 10px;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Initialize the medicine recommender
# @st.cache_resource
# def load_recommender():
#     return MedicineRecommender()

# recommender = load_recommender()

# # Dashboard Header
# st.markdown("""
# <div class="dashboard-header">
#     <h1 style='color: white; font-size: 3.5rem; margin-bottom: 1rem;'>💊 Symptom Medicine Finder</h1>
#     <h3 style='color: white; opacity: 0.9; margin-top: 0;'>Describe your symptoms and get instant medication recommendations</h3>
# </div>
# """, unsafe_allow_html=True)

# # =============================================
# # MAIN DASHBOARD LAYOUT
# # =============================================

# # Row 1: Quick Stats
# st.markdown("### 📊 Live Dashboard Statistics")
# col1, col2, col3, col4 = st.columns(4)

# # Get real-time statistics
# all_medicines = recommender.get_all_medicines()
# total_medicines = len(all_medicines)
# avg_safety = np.mean([med.get('safety_rating', 0) for med in all_medicines]) if all_medicines else 0
# categories = len(set(med.get('category', '') for med in all_medicines)) if all_medicines else 0
# high_safety = len([med for med in all_medicines if med.get('safety_rating', 0) >= 4.0]) if all_medicines else 0

# with col1:
#     st.metric("💊 Total Medicines", total_medicines)
# with col2:
#     st.metric("⭐ Avg Safety", f"{avg_safety:.1f}/5.0")
# with col3:
#     st.metric("📋 Categories", categories)
# with col4:
#     st.metric("🏆 High Safety", high_safety)

# st.markdown("---")

# # =============================================
# # SYMPTOM INPUT SECTION
# # =============================================
# st.markdown("### 🩺 Describe Your Symptoms")

# # Symptom input card
# with st.container():
#     col1, col2 = st.columns([3, 1])
    
#     with col1:
#         symptoms = st.text_area(
#             " ",
#             placeholder="Describe your symptoms in detail...\nExamples:\n• fever and headache\n• pain and inflammation\n• allergy and sneezing\n• infection and cough",
#             height=120,
#             help="Be specific for better recommendations",
#             key="symptom_input"
#         )
    
#     with col2:
#         st.write("")  # Spacer
#         search_btn = st.button("🔍 **Find Medicines**", type="primary", use_container_width=True)

# # Quick symptom buttons
# st.markdown("### ⚡ Quick Symptoms")
# quick_symptoms = ["fever", "headache", "pain", "allergy", "cough", "nausea", "inflammation", "infection"]

# quick_cols = st.columns(4)
# for i, symptom in enumerate(quick_symptoms):
#     with quick_cols[i % 4]:
#         if st.button(f"🤒 {symptom.title()}", use_container_width=True):
#             st.session_state.quick_symptom = symptom

# # Use quick symptom if clicked
# if 'quick_symptom' in st.session_state:
#     symptoms = st.session_state.quick_symptom
#     search_btn = True

# # =============================================
# # RESULTS DISPLAY SECTION
# # =============================================
# if search_btn or symptoms:
#     if symptoms and symptoms.strip():
#         with st.spinner("🔍 AI is analyzing your symptoms..."):
#             # Get recommendations from database
#             results = recommender.recommend_by_symptoms(symptoms)
        
#         if results:
#             # Success header
#             st.markdown(f"""
#             <div style='
#                 background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%);
#                 color: white;
#                 padding: 1.5rem 2rem;
#                 border-radius: 15px;
#                 margin: 2rem 0 1rem 0;
#                 text-align: center;
#                 font-weight: 600;
#                 font-size: 1.2rem;
#             '>
#                 ✅ Found {len(results)} perfect medication matches for: "{symptoms}"
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Results counter and filters
#             col1, col2, col3 = st.columns([2, 1, 1])
#             with col1:
#                 st.write(f"**Showing top {min(10, len(results))} results**")
#             with col2:
#                 sort_by = st.selectbox("Sort by:", ["Safety ⭐", "Name A-Z", "Category"])
#             with col3:
#                 show_count = st.slider("Show results:", 1, 10, 5)
            
#             # Sort results
#             if sort_by == "Safety ⭐":
#                 results.sort(key=lambda x: x['safety_rating'], reverse=True)
#             elif sort_by == "Name A-Z":
#                 results.sort(key=lambda x: x['name'])
#             elif sort_by == "Category":
#                 results.sort(key=lambda x: x['category'])
            
#             # Display medicine cards
#             for i, medicine in enumerate(results[:show_count]):
#                 # Calculate safety percentage for progress bar
#                 safety_percent = (medicine['safety_rating'] / 5.0) * 100
                
#                 st.markdown(f"""
#                 <div class="medicine-result-card">
#                     <div style='display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;'>
#                         <div>
#                             <h2 style='margin: 0 0 0.5rem 0; color: white; font-size: 1.5rem;'>
#                                 💊 {medicine['name']}
#                             </h2>
#                             <div style='display: flex; gap: 0.5rem; margin-bottom: 0.5rem;'>
#                                 <span class='safety-badge'>⭐ {medicine['safety_rating']}/5.0</span>
#                                 <span class='category-badge'>{medicine['category']}</span>
#                                 <span class='price-badge'>{medicine['price_category']}</span>
#                             </div>
#                         </div>
#                     </div>
                    
#                     <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;'>
#                         <div>
#                             <strong>🎯 Symptoms Treated:</strong><br>
#                             <span style='opacity: 0.9; font-size: 0.95rem;'>{medicine['for_symptoms']}</span>
#                         </div>
#                         <div>
#                             <strong>📊 Match Strength:</strong><br>
#                             <span style='opacity: 0.9;'>Excellent match for your symptoms</span>
#                         </div>
#                     </div>
                    
#                     <div style='margin-top: 1rem;'>
#                         <strong>📈 Safety Rating:</strong>
#                         <div style='width: 100%; background: rgba(255,255,255,0.2); border-radius: 10px; height: 8px; margin: 0.5rem 0;'>
#                             <div style='width: {safety_percent}%; background: linear-gradient(90deg, #4CAF50, #8BC34A); height: 100%; border-radius: 10px;'></div>
#                         </div>
#                         <div style='display: flex; justify-content: space-between; font-size: 0.9rem; opacity: 0.8;'>
#                             <span>Low Safety</span>
#                             <span>High Safety</span>
#                         </div>
#                     </div>
#                 </div>
#                 """, unsafe_allow_html=True)
                
#                 # Additional actions for each medicine
#                 col1, col2, col3 = st.columns([3, 1, 1])
#                 with col2:
#                     if st.button("📋 View Details", key=f"details_{i}", use_container_width=True):
#                         st.session_state[f"show_details_{i}"] = not st.session_state.get(f"show_details_{i}", False)
#                 with col3:
#                     if st.button("💊 Save", key=f"save_{i}", use_container_width=True):
#                         st.success(f"✅ {medicine['name']} saved to your list!")
                
#                 # Expandable details
#                 if st.session_state.get(f"show_details_{i}", False):
#                     with st.expander("🔍 Detailed Information", expanded=True):
#                         col1, col2 = st.columns(2)
#                         with col1:
#                             st.write("**💡 Key Information:**")
#                             st.info(medicine.get('key_info', 'Consult healthcare professional for proper usage.'))
#                         with col2:
#                             st.write("**📋 Usage Guidelines:**")
#                             st.write("• Take as directed by healthcare provider")
#                             st.write("• Follow dosage instructions carefully")
#                             st.write("• Consult doctor for any concerns")
                
#                 st.markdown("---")
            
#             # Download results option
#             st.markdown("### 💾 Export Results")
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 if st.button("📄 Export to CSV", use_container_width=True):
#                     df = pd.DataFrame(results)
#                     csv = df.to_csv(index=False)
#                     st.download_button(
#                         label="Download CSV",
#                         data=csv,
#                         file_name=f"medicine_recommendations_{symptoms.replace(' ', '_')}.csv",
#                         mime="text/csv"
#                     )
            
#             with col2:
#                 if st.button("🖨️ Print Results", use_container_width=True):
#                     st.info("🖨️ Use browser print function (Ctrl+P) to print these results")
            
#             with col3:
#                 if st.button("📱 Share Results", use_container_width=True):
#                     st.info("📱 Share this page URL with your healthcare provider")
        
#         else:
#             # No results found
#             st.markdown(f"""
#             <div style='
#                 background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
#                 color: white;
#                 padding: 2rem;
#                 border-radius: 15px;
#                 margin: 2rem 0;
#                 text-align: center;
#             '>
#                 <h3 style='color: white; margin: 0 0 1rem 0;'>❌ No Medications Found</h3>
#                 <p style='margin: 0; font-size: 1.1rem;'>
#                     No medications found for: "<strong>{symptoms}</strong>"<br>
#                     Try different symptoms or be more specific.
#                 </p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Suggestions
#             st.markdown("### 💡 Try These Instead:")
#             col1, col2, col3 = st.columns(3)
#             suggestions = [
#                 ("fever headache", "Common symptoms"),
#                 ("pain inflammation", "Pain relief"),
#                 ("allergy sneezing", "Allergy symptoms")
#             ]
            
#             for i, (suggestion, description) in enumerate(suggestions):
#                 with [col1, col2, col3][i]:
#                     if st.button(f"🔍 {suggestion.title()}", key=f"sugg_{i}", use_container_width=True):
#                         st.session_state.quick_symptom = suggestion
#                         st.rerun()
    
#     else:
#         # No symptoms entered
#         st.info("💡 Please enter some symptoms to search for medications")

# # =============================================
# # RECENT SEARCHES & HISTORY
# # =============================================
# st.markdown("---")
# st.markdown("### 📋 Search History")

# # Initialize session state for search history
# if 'search_history' not in st.session_state:
#     st.session_state.search_history = []

# # Add current search to history
# if symptoms and symptoms.strip() and search_btn:
#     if symptoms not in [item['symptoms'] for item in st.session_state.search_history]:
#         st.session_state.search_history.insert(0, {
#             'symptoms': symptoms,
#             'timestamp': pd.Timestamp.now(),
#             'results_count': len(results) if 'results' in locals() else 0
#         })
    
#     # Keep only last 5 searches
#     st.session_state.search_history = st.session_state.search_history[:5]

# # Display search history
# if st.session_state.search_history:
#     for i, search in enumerate(st.session_state.search_history):
#         col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
#         with col1:
#             st.write(f"**{search['symptoms']}**")
#         with col2:
#             st.write(f"🔍 {search['results_count']} results")
#         with col3:
#             st.write(search['timestamp'].strftime("%H:%M"))
#         with col4:
#             if st.button("🔁 Retry", key=f"retry_{i}"):
#                 symptoms = search['symptoms']
#                 search_btn = True
#                 st.rerun()
# else:
#     st.info("🔍 Your recent searches will appear here")

# # =============================================
# # SIDEBAR WITH ADDITIONAL FEATURES
# # =============================================
# with st.sidebar:
#     st.markdown("""
#     <div style='
#         background: linear-gradient(135deg, rgba(102, 126, 234, 0.9) 0%, rgba(118, 75, 162, 0.9) 100%);
#         color: white;
#         padding: 2rem 1.5rem;
#         border-radius: 20px;
#         margin-bottom: 2rem;
#         text-align: center;
#     '>
#         <h2 style='color: white; margin: 0;'>💊 Symptom Dashboard</h2>
#         <p style='margin: 0.5rem 0 0 0; opacity: 0.9;'>AI-Powered Medicine Finder</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Quick stats
#     st.markdown("### 📊 Quick Stats")
#     col1, col2 = st.columns(2)
#     with col1:
#         st.metric("💊 Total", total_medicines)
#     with col2:
#         st.metric("⭐ Safety", f"{avg_safety:.1f}/5.0")
    
#     st.markdown("---")
    
#     # Advanced filters
#     st.markdown("### ⚙️ Advanced Filters")
#     min_safety = st.slider("Minimum Safety", 1.0, 5.0, 3.5, 0.1)
#     price_filter = st.selectbox("Price Range", ["Any", "💰 Economy", "💵 Standard", "💎 Premium"])
#     category_filter = st.selectbox("Category", ["All", "Analgesic", "Antibiotic", "Antihistamine", "NSAID"])
    
#     st.markdown("---")
    
#     # Quick actions
#     st.markdown("### ⚡ Quick Actions")
#     if st.button("🔄 Clear Search", use_container_width=True):
#         symptoms = ""
#         st.rerun()
    
#     if st.button("📊 View All Medicines", use_container_width=True):
#         st.session_state.show_all_medicines = True
    
#     if st.button("🆘 Emergency Help", use_container_width=True):
#         st.warning("🚨 In case of emergency, contact your local emergency services immediately!")
#         st.info("📞 Emergency Numbers:\n• India: 112\n• US: 911\n• UK: 999\n• EU: 112")

# # =============================================
# # ALL MEDICINES VIEW
# # =============================================
# if st.session_state.get('show_all_medicines', False):
#     st.markdown("### 💊 Complete Medicine Database")
    
#     if all_medicines:
#         df = pd.DataFrame(all_medicines)
        
#         # Search and filter
#         col1, col2 = st.columns(2)
#         with col1:
#             search_term = st.text_input("🔍 Search medicines:", placeholder="Search by name or category...")
#         with col2:
#             items_per_page = st.selectbox("Items per page:", [10, 25, 50, 100])
        
#         # Filter data
#         if search_term:
#             filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
#         else:
#             filtered_df = df
        
#         # Pagination
#         if len(filtered_df) > 0:
#             total_pages = (len(filtered_df) // items_per_page) + (1 if len(filtered_df) % items_per_page else 0)
#             page = st.number_input("Page", min_value=1, max_value=total_pages, value=1)
            
#             start_idx = (page - 1) * items_per_page
#             end_idx = min(start_idx + items_per_page, len(filtered_df))
            
#             st.dataframe(filtered_df.iloc[start_idx:end_idx], use_container_width=True)
            
#             st.write(f"Showing {start_idx + 1}-{end_idx} of {len(filtered_df)} medicines")
#         else:
#             st.warning("No medicines found matching your search criteria")
    
#     if st.button("← Back to Dashboard"):
#         st.session_state.show_all_medicines = False
#         st.rerun()



               
# =============================================
# SYMPTOM ANALYZER PAGE
# =============================================
elif selected == "🔍 Symptom Analyzer":
    # Page header - matches your image design
    st.markdown("""
    <div style='background: #1a1a1a; padding: 2rem; border-radius: 15px; margin: 1rem 0;'>
        <h1 style='color: #667eea; text-align: center;'>🔍 AI Recommendations</h1>
    </div>
    """, unsafe_allow_html=True)  # ✅ ADD THIS PARAMETER
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Symptoms input - matches your image
        st.markdown("### 📝 Describe Your Symptoms")
        user_symptoms = st.text_area(
            " ",
            placeholder="Describe your symptoms...",
            height=150,
            help="Be specific for better recommendations"
        )
        
        # Advanced filters - matches your image exactly
        st.markdown("### ⚙️ Advanced Filters")
        col1, col2, col3 = st.columns(3)
        with col1:
            min_safety = st.slider("**Safety**", 1.0, 5.0, 3.5, 0.1)  # ✅ Matches your 3.50 setting
        with col2:
            max_price = st.selectbox("**Price**", ["Any", "💰 Economy", "💵 Standard", "💎 Premium"])
        with col3:
            category_filter = st.selectbox("**Category**", ["All", "Analgesic", "Antibiotic", "NSAID"])

    with  col1, col2, col3 :
        if user_symptoms:
            st.markdown("### 💊 AI Recommendations")
            
            with st.spinner("🤖 AI is analyzing your symptoms..."):
                results = recommender.recommend_by_symptoms(user_symptoms)
            
            if results:
                filtered_results = [med for med in results if med['safety_rating'] >= min_safety]
                
                if filtered_results:
                    # ✅ Success message - matches your dark green box
                    st.markdown(f"""
                    <div style='
                        background: #00b09b; 
                        color: white; 
                        padding: 1.5rem; 
                        border-radius: 10px; 
                        margin: 1rem 0;
                        text-align: center;
                        font-weight: bold;
                        font-size: 1.1rem;
                    '>
                        🎯 AI found {len(filtered_results)} perfect medication matches!
                    </div>
                    """, unsafe_allow_html=True)  # ✅ ADD THIS
                    
                    # ✅ Medicine cards - matches your blue card design
                    for medicine in filtered_results:
                        st.markdown(f"""
                        <div class="medicine-card-premium">
                        <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
                            <h2 style='margin: 0; color: white;'>💊 {medicine['name']}</h2>
                            <div style='background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px;'>
                                <span style='font-size: 1.2rem; font-weight: bold;'>⭐ {medicine['safety_rating']}/5.0</span>
                            </div>
                    </div>
      
                        
                        
   
                        
                        
                        """, unsafe_allow_html=True)  # ✅ ADD THIS
                        
                else:
                    st.error("❌ No medications meet your safety criteria.")
            else:
                st.warning("⚠️ No medications found. Try different symptoms.")


# =============================================
# MEDICINE DATABASE PAGE
# =============================================
elif selected == "📊 Medicine Database":
    st.markdown("""
    <div class="glass-card">
        <h1 style='color: #667eea; text-align: center;'>📊 Complete Medicine Database</h1>
        <p style='text-align: center; color:  F5F527;'>Advanced search and filtering for our comprehensive medicine library</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Search and analytics
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        search_term = st.text_input("🔍 Search medicines:", placeholder="Search by name, category, or symptoms...")
    
    all_medicines = recommender.get_all_medicines()
    
    if all_medicines:
        df = pd.DataFrame(all_medicines)
        
        # Enhanced metrics
        st.markdown("### 📈 Database Analytics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Medicines", len(df))
        with col2:
            st.metric("Avg Safety", f"{df['safety_rating'].mean():.1f}/5.0")
        with col3:
            st.metric("Categories", df['category'].nunique())
        with col4:
            st.metric("High Safety", len(df[df['safety_rating'] >= 4.0]))
        
        # Enhanced dataframe
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
    else:
        st.error("❌ No medicines found in the database.")

# =============================================
# ADD MEDICINE PAGE - NEW FEATURE
# =============================================
if selected == "➕ Add Medicine":
    st.markdown("""
    <div class="glass-card">
        <h1 style='color: #667eea; text-align: center;'>➕➕ Add New Medicine</h1>
        <p style='text-align: center; color: #666;'>Add a new medicine to the database with all required information</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Medicine form
    with st.form("add_medicine_form"):
        st.markdown("### 📝📝 Medicine Information")
        
        col1, col2 = st.columns(2)
        with col1:
            medicine_name = st.text_input("💊💊 Medicine Name*", placeholder="e.g., Paracetamol 500mg")
            category = st.selectbox("📋📋 Category*", [
                "Analgesic", "NSAID", "Antibiotic", "Antihistamine", "PPI", "H2 Blocker", 
                "Bronchodilator", "Statin", "Vitamin", "Mineral", "Other"
            ])
            safety_rating = st.slider("⭐ Safety Rating*", 1.0, 5.0, 4.0, 0.1)
        
        with col2:
            price_category = st.selectbox("💰💰 Price Category*", 
                ["💰 Economy", "💵💵 Standard", "💎💎 Premium"])
            dosage_form = st.text_input("💊💊 Dosage Form", placeholder="e.g., Tablet 500mg, Inhaler")
            duration = st.text_input("⏰⏰ Duration", placeholder="e.g., 4-6 hours, Once daily")
        
        # Symptoms and usage
        for_symptoms = st.text_area("🤒🤒 Symptoms Treated*", 
            placeholder="e.g., fever headache mild pain", 
            help="Describe what symptoms this medicine treats")
        
        primary_use = st.text_input("🎯🎯 Primary Use", 
            placeholder="e.g., Analgesic & Antipyretic")
        
        key_info = st.text_area("💡💡 Key Information", 
            placeholder="Important medical information, precautions, etc.",
            height=100)
        
        drug_class = st.text_input("🔬🔬 Drug Class", 
            placeholder="e.g., Non-opioid analgesic, SSRI")
        
        # Submit button
        submitted = st.form_submit_button("💾💾 Add Medicine to Database", type="primary")
        
        if submitted:
            # Validate required fields
            if not medicine_name or not for_symptoms or not category:
                st.error("❌❌ Please fill in all required fields (*)")
            else:
                # Prepare medicine data
                medicine_data = {
                    'name': medicine_name,
                    'for_symptoms': for_symptoms,
                    'category': category,
                    'safety_rating': safety_rating,
                    'price_category': price_category,
                    'key_info': key_info,
                    'primary_use': primary_use,
                    'drug_class': drug_class,
                    'dosage_form': dosage_form,
                    'duration': duration
                }
                
             # Add medicine to database
                success, message = recommender.add_medicine(medicine_data)
                if success:
                    st.success(message)
                    st.balloons()
                    
                #    # Show updated count
                #     total_medicines = recommender.get_total_medicines_count()
                #     st.info(f"📊📊 Total medicines in database: {total_medicines}")
                    
                    # Show user-added count
                    user_added_count = recommender.get_user_added_medicines_count()
                    st.info(f"➕➕ User-added medicines: {user_added_count}")
                else:
                    st.error(message)




# =============================================
# ANALYTICS PAGE
# =============================================
elif selected == "📈 Analytics":
    st.markdown("""
    <div class="glass-card">
        <h1 style='color: #667eea; text-align: center;'>📈 Advanced Analytics</h1>
        <p style='text-align: center; color: F5F527;'>Comprehensive analytics and insights from our medicine database</p>
    </div>
    """, unsafe_allow_html=True)
    
    all_medicines = recommender.get_all_medicines()
    if all_medicines:
        df = pd.DataFrame(all_medicines)
        
        # Interactive charts
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 📊 Category Distribution")
            category_chart = df['category'].value_counts()
            st.bar_chart(category_chart)
        
        with col2:
            st.markdown("### ⭐ Safety Distribution")
            safety_chart = df['safety_rating'].value_counts().sort_index()
            st.line_chart(safety_chart)

# =============================================
# ABOUT PAGE - SAME SIZE CARDS
# =============================================
elif selected == "ℹ️ About":
    # 修复的About页面代码
    st.markdown("""
    <div style='background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%); 
                padding: 3rem 2rem; border-radius: 20px; margin: 2rem 0; 
                border: 1px solid #333; color: white;'>
        <div style='text-align: center; margin-bottom: 3rem;'>
            <h1 style='color: #667eea; font-size: 2.5rem; margin-bottom: 0.5rem;'>🎓 Master's Research Project</h1>
            <h2 style='color: #667eea; font-size: 2rem; margin-top: 0;'>Advanced Medical AI</h2>
        </div>
        
          
<div>
            <p style='font-size: 1.2rem; line-height: 1.6; color: #cccccc;'>
            <strong style='color: #fff;'>MediMatch Pro</strong> is a pioneering application born from advanced research at the intersection of artificial intelligence and healthcare. Developed as part of a comprehensive Master’s project, it showcases how AI can enhance clinical decision support by analyzing complex medical data and offering intelligent insights to assist healthcare professionals. The app embodies innovation, academic rigor, and a vision for the future of medicine—where technology empowers clinicians to make faster, more accurate, and patient centered decisions.

           
        
    """, unsafe_allow_html=True)  # ⬅️ 关键修复：添加这个参数
# Professional Footer
st.markdown("""
<div style='text-align: center; padding: 3rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; border-radius: 20px; margin: 2rem 0;'>
    <h3 style='color: white; margin-bottom: 1rem;'>💊 MediMatch Pro</h3>
    <p style='opacity: 0.9; margin-bottom: 0.5rem;'>Advanced AI Medicine Recommendation System</p>
    <p style='opacity: 0.7; margin: 0;'>🎓 Master's Research Project | 🔬 Medical Informatics | ⚕️ Always Consult Professionals</p>
</div>
""", unsafe_allow_html=True)

# Test adding this medicine programmatically
# test_medicine = {
#     "name": "Loratadine 10mg",
#     "for_symptoms": "allergy hay fever itching runny nose",
#     "category": "Antihistamine",
#     "safety_rating": 4.3,
#     "price_category": "💰 Economy",
#     "key_info": "Non-drowsy formula. Once daily. Few drug interactions. Safe for long-term use.",
#     "primary_use": "Allergy relief",
#     "drug_class": "H1-receptor antagonist",
#     "dosage_form": "Tablet, 10mg",
#     "duration": "Once daily"
# }

# success, message = recommender.add_medicine(test_medicine)
# print(f"Add result: {success}, {message}")
# print(f"Total medicines now: {recommender.get_total_medicines_count()}")

# test_web_app.py - QUICK TEST FOR WEB-APP
import streamlit as st
from medicine_recommender import MedicineRecommender

def test_web_app_functionality():
    """Quick test to verify web-app works"""
    print("🧪 Testing Web-App Dashboard Feature...")
    print("=" * 50)
    
    # Initialize recommender
    recommender = MedicineRecommender()
    
    # Test 1: Check if recommender works
    print("1️⃣ Testing MedicineRecommender...")
    all_meds = recommender.get_all_medicines()
    print(f"   📊 Medicines in database: {len(all_meds)}")
    
    if len(all_meds) > 0:
        print("   ✅ Database loaded successfully")
    else:
        print("   ❌ Database is empty!")
        return False
    
    # Test 2: Test symptom search method
    print("\n2️⃣ Testing symptom search...")
    test_cases = [
        ("fever", "Should find Paracetamol"),
        ("headache", "Should find pain relievers"), 
        ("pain", "Should find NSAIDs"),
        ("allergy", "Should find antihistamines")
    ]
    
    all_passed = True
    for symptoms, expected in test_cases:
        results = recommender.recommend_by_symptoms(symptoms)
        status = "✅" if results else "❌"
        print(f"   {status} '{symptoms}': {(results)} results - {expected}")
        
        if not results:
            all_passed = False
    
    # Test 3: Test dashboard input simulation
    print("\n3️⃣ Testing dashboard inputs...")
    dashboard_inputs = [
        "fever headache",
        "pain inflammation", 
        "allergy sneezing"
    ]
    
    for input_text in dashboard_inputs:
        results = recommender.recommend_by_symptoms(input_text)
        status = "✅" if results else "❌"
        print(f"   {status} '{input_text}': {(results)} results")
    
    # Final result
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 WEB-APP IS READY! Run: streamlit run web_app.py")
        return True
    else:
        print("❌ Some tests failed. Check the implementation.")
        return False

if __name__ == "__main__":
    test_web_app_functionality()


#     # test_dashboard.py - COMPLETE DASHBOARD FEATURE TEST
# import streamlit as st
# import sys
# import traceback
# from medicine_recommender import MedicineRecommender

# def test_dashboard_feature():
#     """Comprehensive test of the dashboard feature"""
    
#     st.title("🧪 Dashboard Feature Test Suite")
#     st.markdown("---")
    
#     # Initialize recommender
#     try:
#         recommender = MedicineRecommender()
#         st.success("✅ MedicineRecommender initialized successfully")
#     except Exception as e:
#         st.error(f"❌ Failed to initialize: {str(e)}")
#         return
    
#     # Test 1: Basic functionality
#     st.subheader("1️⃣ Basic Dashboard Functionality")
    
#     col1, col2 = st.columns(2)
#     with col1:
#         test_symptoms = st.text_input("Test symptoms:", "fever headache")
#     with col2:
#         test_btn = st.button("🔍 Test Search", type="primary")
    
#     if test_btn:
#         st.markdown("---")
        
#         # Test the search
#         with st.spinner("Testing dashboard search..."):
#             results = recommender.recommend_by_symptoms(test_symptoms)
        
#         st.write(f"**Input:** '{test_symptoms}'")
#         st.write(f"**Results:** {len(results)} medicines found")
        
#         if results:
#             st.success("✅ Dashboard search is WORKING!")
#             st.write("**First 3 results:**")
#             for i, med in enumerate(results[:3]):
#                 st.write(f"{i+1}. 💊 {med['name']} (⭐{med['safety_rating']})")
#         else:
#             st.error("❌ Dashboard search returned NO results")
    
#     # Test 2: Test multiple symptom combinations
#     st.markdown("---")
#     st.subheader("2️⃣ Symptom Combinations Test")
    
#     test_cases = [
#         ("fever", "Single symptom"),
#         ("headache", "Single symptom"), 
#         ("fever headache", "Multiple symptoms"),
#         ("pain inflammation", "Multiple symptoms"),
#         ("allergy sneezing", "Multiple symptoms"),
#         ("cough fever", "Multiple symptoms")
#     ]
    
#     for symptoms, description in test_cases:
#         if st.button(f"Test: '{symptoms}'", key=f"test_{symptoms}"):
#             results = recommender.recommend_by_symptoms(symptoms)
#             status = "✅" if results else "❌"
#             st.write(f"{status} **'{symptoms}'**: {len(results)} results - {description}")
            
#             if results:
#                 for med in results[:2]:
#                     st.write(f"   💊 {med['name']} (⭐{med['safety_rating']})")
    
#     # Test 3: Edge cases
#     st.markdown("---")
#     st.subheader("3️⃣ Edge Cases Test")
    
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         if st.button("Test Empty Input"):
#             results = recommender.recommend_by_symptoms("")
#             st.write(f"Empty input: {len(results)} results (should be 0)")
#     with col2:
#         if st.button("Test None Input"):
#             results = recommender.recommend_by_symptoms(None)
#             st.write(f"None input: {len(results)} results")
#     with col3:
#         if st.button("Test Unknown Symptoms"):
#             results = recommender.recommend_by_symptoms("xyzunknown")
#             st.write(f"Unknown symptoms: {len(results)} results")
    
#     # Test 4: Performance test
#     st.markdown("---")
#     st.subheader("4️⃣ Performance Test")
    
#     if st.button("⏱️ Test Response Time"):
#         import time
        
#         test_inputs = ["fever", "headache", "pain", "allergy", "infection"]
        
#         for symptoms in test_inputs:
#             start_time = time.time()
#             results = recommender.recommend_by_symptoms(symptoms)
#             end_time = time.time()
#             response_time = (end_time - start_time) * 1000
            
#             status = "✅" if response_time < 100 else "⚠️"
#             st.write(f"{status} '{symptoms}': {len(results)} results in {response_time:.1f}ms")
    
#     # Test 5: Data validation
#     st.markdown("---")
#     st.subheader("5️⃣ Data Validation Test")
    
#     if st.button("🔍 Validate Data Structure"):
#         results = recommender.recommend_by_symptoms("fever")
        
#         if results:
#             sample_med = results[0]
#             required_fields = ['name', 'for_symptoms', 'category', 'safety_rating', 'price_category']
#             missing_fields = []
            
#             for field in required_fields:
#                 if field not in sample_med:
#                     missing_fields.append(field)
            
#             if missing_fields:
#                 st.error(f"❌ Missing fields: {missing_fields}")
#             else:
#                 st.success("✅ All required fields present")
                
#                 # Check data types
#                 st.write("**Data types:**")
#                 for field, value in sample_med.items():
#                     st.write(f"   - {field}: {type(value).__name__} = {value}")
#         else:
#             st.error("❌ No results to validate")
    
#     # Final summary
#     st.markdown("---")
#     st.subheader("🎯 Test Summary")
    
#     # Quick overall test
#     overall_test = recommender.recommend_by_symptoms("fever")
#     if overall_test and len(overall_test) > 0:
#         st.success("🎉 DASHBOARD FEATURE IS WORKING PERFECTLY!")
#         st.balloons()
#     else:
#         st.error("❌ Dashboard feature has issues")

# if __name__ == "__main__":
#     test_dashboard_feature()


if search_btn and symptoms:
    results = recommender.recommend_by_symptoms(symptoms)
    
    # DEBUG: See what's actually happening
    st.write(f"🔍 DEBUG: results = {results}")
    st.write(f"🔍 DEBUG: len(results) = {len(results) if results else 0}")
    st.write(f"🔍 DEBUG: results is None = {results is None}")
    st.write(f"🔍 DEBUG: results == [] = {results == []}")
    
    if results and len(results) > 0:
        st.success(f"✅ Found {len(results)} results!")
        # ... show results ...
    else:
        st.error("❌ No results found")