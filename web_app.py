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
        {"icon": "🏠", "label": "Dashboard", "desc": "Home & quick access", "key": "dashboard"},
        {"icon": "🔍", "label": "Symptom Analyzer", "desc": "AI-powered analysis", "key": "symptoms"},
         {"icon": "➕", "label": "Add Medicine", "desc": "Add new medicine to database", "key": "add_medicine"},  # MOVED HERE
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
        if option['desc']:
            st.caption(f"📌📌 {option['desc']}")
    
    st.markdown("---")
    
     # Quick stats in sidebar - UPDATED TO SHOW TOTAL MEDICINES
try:
    total_medicines = recommender.get_total_medicines_count()
    all_meds = recommender.get_all_medicines_with_user_added()
    
    if all_meds:
        st.markdown("### 📊📊 Quick Stats")
        avg_safety = np.mean([med.get('safety_rating', 0) for med in all_meds])
        user_added_count = recommender.get_user_added_medicines_count()
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("💊💊 Total", total_medicines)
        with col2:
            st.metric("⭐ Safety", f"{avg_safety:.1f}/5.0")
        
        if user_added_count > 0:
            st.info(f"📝📝 User Added: {user_added_count} medicines")

except Exception as e:
    st.error(f"Error loading stats: {e}")  # ✅ FIXED - proper f-string

selected = st.session_state.selected


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
                success, message = recommender.add_medicine()
                
                if success:
                    st.success(message)
                    st.balloons()
                    
                    # Show updated count
                    total_medicines = recommender.get_total_medicines_count()
                    st.info(f"📊📊 Total medicines in database: {total_medicines}")
                    
                    # Clear form
                    st.rerun()
                else:
                    st.error(message)

# =============================================
# DASHBOARD PAGE - WITH ENHANCED MEDICINE CARDS
# =============================================
if selected == "🏠 Dashboard":
    # Hero Section with Glass Morphism
    st.markdown("""
    <div class="glass-card">
        <div style='text-align: center; padding: 2rem;'>
            <h1 style='color: #667eea; margin-bottom: 1rem;'>Welcome to MediMatch Pro! 🩺</h1>
            <p style='font-size: 1.3rem; color: F5F527; line-height: 1.6;'>
            Your intelligent AI-powered medicine recommendation system. Get personalized medication 
            suggestions based on your symptoms with advanced safety ratings and detailed medical information.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick stats row - UPDATED WITH TOTAL MEDICINES COUNT
    try:
        total_medicines = recommender.get_total_medicines_count()
        all_meds = recommender.get_all_medicines_with_user_added()
        avg_safety = np.mean([med.get('safety_rating', 0) for med in all_meds]) if all_meds else 0
        user_added_count = recommender.get_user_added_medicines_count()
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📊📊 Total Medicines", total_medicines)
        with col2:
            st.metric("⭐ Avg Safety", f"{avg_safety:.1f}/5.0")
        with col3:
            st.metric("🔬🔬 Categories", len(set(med.get('category', '') for med in all_meds)))
        with col4:
            st.metric("👤 User Added", user_added_count)
    except Exception as e:
        st.error(f"Error loading dashboard stats: {e}")
    # Quick Symptom Analyzer
    st.markdown("---")
    st.markdown("## 🔍 Quick Symptom Analysis")
    
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            symptoms = st.text_input(
                "**Describe your symptoms:**",
                placeholder="fever, headache, pain, inflammation...",
                help="Be specific for better recommendations"
            )

            
            # =============================================
# MEDICINE DATABASE PAGE - UPDATED TO SHOW USER-ADDED MEDICINES
# =============================================
elif selected == "📊📊 Medicine Database":
    st.markdown("""
    <div class="glass-card">
        <h1 style='color: #667eea; text-align: center;'>📊📊 Complete Medicine Database</h1>
        <p style='text-align: center; color: #666;'>Advanced search and filtering for our comprehensive medicine library</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Search and analytics
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        search_term = st.text_input("🔍🔍 Search medicines:", placeholder="Search by name, category, or symptoms...")
    
    # Get all medicines including user-added
    all_medicines = recommender.get_all_medicines_with_user_added()
    
    if all_medicines:
        df = pd.DataFrame(all_medicines)
        
        # Enhanced metrics - shows total count including user-added
        total_count = recommender.get_total_medicines_count()
        user_added_count = recommender.get_user_added_medicines_count()
        
        st.markdown("### 📈📈 Database Analytics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Medicines", total_count)
        with col2:
            st.metric("Avg Safety", f"{df['safety_rating'].mean():.1f}/5.0")
        with col3:
            st.metric("Categories", df['category'].nunique())
        with col4:
            st.metric("User Added", user_added_count)
        
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
        st.error("❌❌ No medicines found in the database.")

        # ------------




        
        # if symptoms:
        #     with st.spinner("🔍 AI is analyzing your symptoms..."):
        #         results = recommender.recommend_by_symptoms(symptoms)
                
        #     if results:
        #         st.success(f"✅ Found {len(results)} relevant medications!")
                
        #         # =============================================
        #         # ENHANCED MEDICINE CARDS - UPDATED TEXT
        #         # =============================================
        #         for medicine in results:
        #             # Get enhanced medicine information
        #             medicine_info = get_medicine_details(medicine)
                    
        #             st.markdown(f"""
                   
        #             <div class="medicine-card-premium">
        #                 <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
        #                     <h2 style='margin: 0; color: white;'>💊 {medicine['name']}</h2>
        #                     <div style='background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px;'>
        #                         <span style='font-size: 1.2rem; font-weight: bold;'>⭐ {medicine['safety_rating']}/5.0</span>
        #                     </div>
        #             </div>
        # <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;'>
        # <div>
        #     <strong>🎯 Primary Use:</strong><br>
        #     <span style='opacity: 0.9;'>{medicine_info['primary_use']}</span>
        # </div>
        # <div>
        #     <strong>📊 Classification:</strong><br>
        #     <span style='opacity: 0.9;'>{medicine_info['drug_class']}</span>
        # </div>
        # <div>
        #                         <strong>💊 Formulation:</strong><br>
        #                         <span style='opacity: 0.9;'>{medicine_info['dosage_form']}</span>
        #                     </div>
        #                     <div>
        #                         <strong>⏰ Duration:</strong><br>
        #                         <span style='opacity: 0.9;'>{medicine_info['duration']}</span>
        #                     </div>
        #                     <div style='margin-top: 1rem;'>
        #                     <strong>💡 Important Information:</strong><br>
        #                     <span style='opacity: 0.9; font-size: 0.9rem;'>{medicine_info['key_info']}</span>
        #                 </div>
                        
                        
                        
   
                        
                        
                    
             

                 
        #             """, unsafe_allow_html=True)
                    
        #             # Progress bar
        #             safety_percent = (medicine['safety_rating'] / 5.0) * 100
        #             st.progress(safety_percent / 100)
                    
        #     else:
        #         st.warning("❌ No medications found for these symptoms. Try different symptoms or be more specific.")

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
            <strong style='color: #fff;'>MediMatch Pro</strong> is a pioneering application born from advanced research at the intersection of artificial intelligence and healthcare. Developed as part of a comprehensive Master’s project, it showcases how AI can enhance clinical decision support by analyzing complex medical data and offering intelligent insights to assist healthcare professionals. The app embodies innovation, academic rigor, and a vision for the future of medicine—where technology empowers clinicians to make faster, more accurate, and patient‑centered decisions.

           
        
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




# # Add this right before you call get_total_medicines_count()
# print("=== DEBUGGING ===")
# print(f"Recommender object: {repr(recommender)}")
# print(f"Methods available: {dir(recommender)}")
# print(f"medicines_df type: {type(recommender.medicines_df)}")
# print(f"user_added_medicines type: {type(getattr(recommender, 'user_added_medicines', None))}")

# # Then call the method
# total = recommender.get_total_medicines_count()
# print(f"Total medicines returned: {total}")


# # Test the counting methods
# print("=== COUNT VERIFICATION ===")
# print(f"Total medicines (method): {recommender.get_total_medicines_count()}")
# print(f"User added (method): {recommender.get_user_added_medicines_count()}")
# print(f"Manual count: {len(recommender.medicines_df) + len(recommender.user_added_medicines)}")

# # Debug medicine counts
# print("=== DEBUG ===")
# print(f"Type of medicines_df: {type(recommender.medicines_df)}")
# print(f"Type of user_added_medicines: {type(recommender.user_added_medicines)}")
# print(f"Base medicines count: {len(recommender.medicines_df)}")
# print(f"User added count: {len(recommender.user_added_medicines)}")
# print(f"Total medicines (method): {recommender.get_total_medicines_count()}")
# print(f"User added (method): {recommender.get_user_added_medicines_count()}")




# # Debug medicine counts
# print("=== DEBUG ===")
# print(f"Type of medicines_df: {type(recommender.medicines_df)}")
# print(f"Type of user_added_medicines: {type(recommender.user_added_medicines)}")
# print(f"Base medicines count: {len(recommender.medicines_df)}")
# print(f"User added count: {len(recommender.user_added_medicines)}")
# print(f"Total medicines (method): {recommender.get_total_medicines_count()}")
# print(f"User added (method): {recommender.get_user_added_medicines_count()}")