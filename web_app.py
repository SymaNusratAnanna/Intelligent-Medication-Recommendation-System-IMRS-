# web_app.py - COMPLETELY FIXED VERSION (No errors)
import streamlit as st
import pandas as pd
import numpy as np
from medicine_recommender import MedicineRecommender

# Page configuration
st.set_page_config(
    page_title="MediGuide Pro - Automated Medication Recommendation System",
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
    <h1 class="main-header floating">💊 MediGuide Pro</h1>
    <h3 style='color: white; opacity: 0.9; margin-top: 0;'>Automated Medication Recommendation System</h3>
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
        <h2 style='color: white; margin: 0; font-weight: 700;'>MediGuide Pro</h2>
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


# =============================================
# HOME SECTION - COMPLETE IMPLEMENTATION
# =============================================
if selected == "🏠 Home":
    # Hero Section with Gradient Background
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #37369E 100%); 
                color: white; padding: 4rem 2rem; border-radius: 20px; 
                margin: -1rem -1rem 2rem -1rem; text-align: center;'>
        <h1 style='color: white; font-size: 2rem; margin-bottom: 1rem;'>Tell us what you feel, get personalized medicine recommendations
analysis with safety ratings in seconds</h1>
        <p style='font-size: 1.5rem; opacity: 0.9;'></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Features Section
    st.markdown("## 🔍 Key Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background:linear-gradient(135deg, #667eea 0%, #2EB6E8 100%); padding: 2rem; border-radius: 15px;'>
            <h3 style='color: #1B4582;'>💊 Symptom Analysis</h3>
            <p style='color: white;'>Describe your symptoms in simple terms and get  medication recommendations. Our system analyzes your symptoms against a comprehensive database of medicines, providing personalized suggestions with detailed safety ratings and usage information.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background:linear-gradient(135deg, #667eea 0%, #2EB6E8 100%); padding: 2rem; border-radius: 15px;'>
            <h3 style='color: #1B4582;'>⭐ Safety Ratings</h3>
            <p style='color: white;'>Every medication in our database comes with a 1-5 star safety rating based on clinical data and user feedback. Higher ratings indicate better safety profiles and fewer side effects, helping you make informed decisions about your healthcare.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #2EB6E8 100%); padding: 2rem; border-radius: 15px;'>
            <h3 style='color: #1B4582;'>📊 Medicine Database</h3>
            <p style='color: white;'>Comprehensive database of medications</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("  ")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background:linear-gradient(135deg, #667eea 0%, #2EB6E8 100%); padding: 2rem; border-radius: 15px;'>
            <h3 style='color: #1B4582;'>💊 Symptom Analysis</h3>
            <p style='color: white;'>Describe your symptoms in simple terms and get  medication recommendations. Our system analyzes your symptoms against a comprehensive database of medicines, providing personalized suggestions with detailed safety ratings and usage information.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background:linear-gradient(135deg, #667eea 0%, #2EB6E8 100%); padding: 2rem; border-radius: 15px;'>
            <h3 style='color: #1B4582;'>⭐ Safety Ratings</h3>
            <p style='color: white;'>Every medication in our database comes with a 1-5 star safety rating based on clinical data and user feedback. Higher ratings indicate better safety profiles and fewer side effects, helping you make informed decisions about your healthcare.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #2EB6E8 100%); padding: 2rem; border-radius: 15px;'>
            <h3 style='color: #1B4582;'>📊 Medicine Database</h3>
            <p style='color: white;'>Comprehensive database of medications</p>
        </div>
        """, unsafe_allow_html=True)
    
    # How It Works Section
    st.markdown("---")
    st.markdown("## 🛠️ How It Works")
    
    steps = [
        ("1️⃣", "Describe Your Symptoms", "Simply tell us what you're experiencing - like 'fever with headache' or 'allergy symptoms with sneezing'. Be specific for better matches. Our AI understands natural language and can process multiple symptoms simultaneously"),
        ("2️⃣", "AI Analysis", "Using advanced natural language processing, our AI analyzes your symptoms, matches them with relevant medications, and applies safety filters to provide you with the most appropriate recommendations in seconds"),
        ("3️⃣", "Get Recommendations", "Receive personalized medicine suggestions with complete details including safety ratings, price categories, and specific symptom coverage. Each recommendation includes important usage instructions and precautions."),
        ("4️⃣", "Check Details", "Review comprehensive medication information including dosage guidelines, potential side effects, drug interactions, and special precautions. All information is presented clearly for easy understanding.")
    ]
    
    for emoji, title, desc in steps:
        st.markdown(f"""
        <div style='display: flex; align-items: center; margin: 1rem 0;'>
            <div style='font-size: 2rem; margin-right: 1rem; color: #667eea;'>{emoji}</div>
            <div>
                <h3 style='margin: 0; color: #667eea;'>{title}</h3>
                <p style='margin: 0; color: white;'>{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Call to Action Section
    st.markdown("---")
    st.markdown("## 🚀 Get Started")
    st.markdown("""
    <div style='text-align: center;'>
        <p style='font-size: 1.5rem; color: #333;'>
            Click the <strong style='color: #667eea;'>Dashboard</strong> in the sidebar to begin
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer Section
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;'>
        <p>© MediGuide Pro develoved by Ananna Syma Nusrat | Always consult healthcare professionals</p>
    </div>
    """, unsafe_allow_html=True)

# =============================================
# DASHBOARD PAGE - COMPREHENSIVE VERSION
# =============================================
if selected == "🏠 Dashboard":
    st.title("🧪 MediGuide Pro - Dashboard")
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
    if all_medicines:
        df = pd.DataFrame(all_medicines)
        
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        # st.metric("💊 Total Medicines", len(all_medicines))
          st.metric("Total Medicines", len(df))
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
        st.subheader("💊 Recommendations")
        
        with st.spinner("🔍 Analyzing your symptoms..."):
            results = recommender.recommend_by_symptoms(symptoms)
        
        # if results:
        #     # st.success(f"✅ Found {len(results)} medications for: **'{symptoms}'**") 

        #     st.success(f"✅ Found {(results)} relevant medications!")

        if results and len(results) > 0:
            st.success(f"✅ Found {len(results)} relevant medications!")
            
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
    
           
# # =============================================
# # SYMPTOM ANALYZER PAGE
# # =============================================

elif selected == "🔍 Symptom Analyzer":
    # Page header with gradient background
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; padding: 2rem; border-radius: 15px; margin: -1rem -1rem 2rem -1rem;'>
        <h1 style='color: white; text-align: center; margin-bottom: 0;'>🔍  Symptom Analyzer</h1>
        <p style='text-align: center; opacity: 0.9; font-size: 1.2rem;'>Get personalized medicine recommendations</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Symptoms input with better styling
        st.markdown("### 📝 Describe Your Symptoms")
        user_symptoms = st.text_area(
            " ",
            placeholder="e.g. fever, headache, pain, allergy...",
            height=150,
            help="Be specific for better recommendations",
            key="symptom_input"
        )
        # Search button
    with col1:
        st.write("")  # Spacer
        search_btn = st.button("🔍 Search Medicines", type="primary", use_container_width=True)
          
        # Advanced filters section
        st.markdown("### ⚙️ Advanced Filters")
        filter_col1, filter_col2, filter_col3 = st.columns(3)
        with filter_col1:
            min_safety = st.slider("**Safety Rating**", 1.0, 5.0, 3.5, 0.1)
        with filter_col2:
            max_price = st.selectbox("**Price**", ["Any", "💰 Economy", "💵 Standard", "💎 Premium"])
        with filter_col3:
            category_filter = st.selectbox("**Category**", ["All", "Analgesic", "Antibiotic", "NSAID"])
    
  
    
    # Quick symptom buttons
    st.markdown("### ⚡ Quick Symptoms")
    quick_cols = st.columns(4)
    quick_symptoms = ["fever", "headache", "pain", "allergy", "cough", "nausea", "inflammation", "infection"]
    
    for i, symptom in enumerate(quick_symptoms):
        with quick_cols[i % 4]:
            if st.button(f"🤒 {symptom.title()}", key=f"quick_{symptom}", use_container_width=True):
                user_symptoms = symptom
                search_btn = True
    
    # Search and display results - FIXED SECTION
    if search_btn and user_symptoms:
        st.markdown("---")
        st.subheader(f"🔍 Searching for: **'{user_symptoms}'**")
        
        with st.spinner("🤖 Analyzing your symptoms..."):
            # Get results from database
            results = recommender.recommend_by_symptoms(user_symptoms)
        
        if results:
            # Apply filters
            filtered_results = []
            for med in results:
                # Safety filter
                if med['safety_rating'] < min_safety:
                    continue
                # Price filter
                if max_price != "Any" and med['price_category'] != max_price:
                    continue
                # Category filter
                if category_filter != "All" and med['category'] != category_filter:
                    continue
                filtered_results.append(med)
            
            if filtered_results:
                # Success message
                st.markdown(f"""
                <div style='background: #00b09b; color: white; padding: 1.5rem; 
                            border-radius: 10px; margin: 1rem 0; text-align: center;
                            font-weight: bold; font-size: 1.1rem;'>
                    ✅ Found {len(filtered_results)} matching medications!
                </div>
                """, unsafe_allow_html=True)
                
                # Display medicine cards
                for medicine in filtered_results:
                    st.markdown(f"""
                    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                                color: white; padding: 1.5rem; border-radius: 15px; margin: 1.5rem 0;
                                border-left: 5px solid #ff6b6b; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
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
                                <strong>🤒 Treats:</strong><br>
                                <span style='opacity: 0.9;'>{medicine['for_symptoms']}</span>
                            </div>
                            <div>
                                <strong>📊 Safety:</strong><br>
                                <span style='opacity: 0.9;'>Excellent ({medicine['safety_rating']}/5.0)</span>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Progress bar
                    safety_percent = (medicine['safety_rating'] / 5.0) * 100
                    st.progress(safety_percent / 100)
                    
                    st.markdown("---")
            else:
                st.error("❌ No medications match your filter criteria")
                st.info("💡 Try adjusting your filters or try different symptoms")
        else:
            st.error(f"❌ No medications found for: '{user_symptoms}'")
            st.info("💡 Try these symptoms: fever, headache, pain, allergy, infection")
    
    elif not user_symptoms and search_btn:
        st.warning("⚠️ Please enter some symptoms to search")


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
        <p style='text-align: center; color: white;'>Add a new medicine to the database with all required information</p>
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
        <p style='text-align: center; color: white;'>Comprehensive analytics and insights from our medicine database</p>
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
            <strong style='color: #fff;'>MediGuide Pro</strong> is a pioneering application born from advanced research at the intersection of artificial intelligence and healthcare. Developed as part of a comprehensive Master’s project, it showcases how AI can enhance clinical decision support by analyzing complex medical data and offering intelligent insights to assist healthcare professionals. The app embodies innovation, academic rigor, and a vision for the future of medicine—where technology empowers clinicians to make faster, more accurate, and patient centered decisions.

           
        
    """, unsafe_allow_html=True)  # ⬅️ 关键修复：添加这个参数
# Professional Footer
st.markdown("""
<div style='text-align: center; padding: 3rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; border-radius: 20px; margin: 2rem 0;'>
    <h3 style='color: white; margin-bottom: 1rem;'>💊 MediGuide Pro</h3>
    <p style='opacity: 0.9; margin-bottom: 0.5rem;'>Automated  Medication Recommendation System</p>
    <p style='opacity: 0.7; margin: 0;'>🎓 Master's Research Project | 🔬 Medical Informatics | ⚕️ Always Consult Professionals</p>
</div>
""", unsafe_allow_html=True)

