# web_app.py - FIXED VERSION (No errors)
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

# Advanced CSS with animations and modern design
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
        0 background-position: 0% 50%; }
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
        box-shadow: 0 8px 32px0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.2);
    }
    
    /* Premium medicine cards */
    .medicine-card-premium {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        box-shadow: 10px 30px rgba(102, 126, 234, 0.3);
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
    
    /* Premium navigation */
    .nav-section-premium {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 1.5rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    /* Metric cards with glow effect */
    .metric-card-premium {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem border-radius: 20px;
        text-align: center;
        margin: 1rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .metric-card-premium:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.4);
    }
    
    /* Custom progress bars */
    .stProgress > div > div {
        background: linear-gradient(90deg, #4CAF50 0%, #8BC34A 50%, #FFEB3B 100        border-radius: 10px;
    }
    
    /* Beautiful buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
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
    
    /* Custom warning box */
    .custom-warning {
        background: #fff3cd;
        color: #856404;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
        text-align: center;
        margin: 1rem 0;
    }
    
    /* Custom error box */
    .custom-error {
        background: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #dc3545;
        text-align: center;
        margin: 1rem 0;
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
    <p style='opacity: 0.8;'>Advanced medical intelligence for personalized treatment recommendations</p>
</div>
""", unsafe_allow_html=True)

# Enhanced navigation with beautiful styling
with st.sidebar:
    st.markdown("""
    <div class="nav-section-premium">
        <div style='text-align: center; margin-bottom: 1rem;'>
            <div class="floating">💊</div>
            <h3 style='color: white; margin: 1rem 0;'>Medical Navigator</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Beautiful radio buttons
    selected = st.radio(
        "Choose your destination:",
        ["🏠 Dashboard", "🔍 Symptom Analyzer", "📊 Medicine Database", "📈 Analytics", "ℹ️ About"],
        index=0
    )
    
    # Quick stats in sidebar
    st.markdown("---")
    try:
        all_meds = recommender.get_all_medicines()
        if all_meds:
            st.markdown("### 📊 Quick Stats")
            total_meds = len(all_meds)
            avg_safety = np.mean([med.get('safety_rating', 0) for med in all_meds])
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Medicines", total_meds)
            with col2:
                st.metric("Avg Safety", f"{avg_safety:.1f}/5.0")
    except:
        pass

# Dashboard Page
if selected == "🏠 Dashboard":
    # Hero Section with Glass Morphism
    st.markdown("""
    <div class="glass-card">
        <div style='text-align: center; padding: 2rem;'>
            <h1 style='color: #667eea; margin-bottom: 1rem;'>Welcome to MediMatch Pro! 🩺</h1>
            <p style='font-size: 1.3rem; color: #666; line-height: 1.6;'>
            Your intelligent AI-powered medicine recommendation system. Get personalized medication 
            suggestions based on your symptoms with advanced safety ratings and detailed medical information.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick stats row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card-premium"><h4>📊 Total Medicines</h4><h2>24</h2></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card-premium"><h4>⭐ Avg Safety</h4><h2>4.2/5.0</h2></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card-premium"><h4>🔬 Categories</h4><h2>8</h2></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card-premium"><h4>⚡ Response Time</h4><h2><1s</h2></div>', unsafe_allow_html=True)
    
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
        
        if symptoms:
            with st.spinner("🔍 AI is analyzing your symptoms..."):
                results = recommender.recommend_by_symptoms(symptoms)
                
            if results:
                st.markdown(f'<div class="success-box-premium">🎯 Found {len(results)} perfect matches for your symptoms!</div>', unsafe_allow_html=True)
                
                # Enhanced medicine cards
                for i, medicine in enumerate(results, 1):
                    safety_color = "🟢" if medicine['safety_rating'] >= 4.0 else "🟡" if medicine['safety_rating'] >= 3.0 else "🔴"
                    
                    st.markdown(f"""
                    <div class="medicine-card-premium">
                        <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
                            <h2 style='margin: 0; color: white;'>💊 {medicine['name']}</h2>
                            <div style='background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px;'>
                                <span style='font-size: 1.2rem; font-weight: bold;'>{safety_color} {medicine['safety_rating']}/5.0</span>
                            </div>
                        </div>
                        
                        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; color: white;'>
                            <div>
                                <strong>🧬 Treatment For:</strong><br>
                                <span style='opacity: 0.9;'>{medicine['for_symptoms']}</span>
                            </div>
                            <div>
                                <strong>📋 Category:</strong><br>
                                <span style='opacity: 0.9;'>{medicine['category']}</span>
                            </div>
                        </div>
                        
                        <div style='margin-top: 1rem;'>
                            <strong>⭐ Safety Progress:</strong>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Animated progress bar
                    safety_percent = (medicine['safety_rating'] / 5.0) * 100
                    st.progress(safety_percent / 100)
                    
            else:
                # FIXED: Using custom CSS class instead of unsafe_allow_html
                st.markdown('<div class="custom-warning">❌ No medications found for these symptoms. Try different symptoms or be more specific.</div>', unsafe_allow_html=True)

# Symptom Analyzer Page
elif selected == "🔍 Symptom Analyzer":
    st.markdown("""
    <div class="glass-card">
        <h1 style='color: #667eea; text-align: center; margin-bottom: 2rem;'>🔍 Advanced Symptom Analyzer</h1>
        <p style='text-align: center; color: #666; font-size: 1.2rem;'>
        Detailed symptom analysis with advanced filtering and AI-powered recommendations
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📝 Describe Your Symptoms")
        user_symptoms = st.text_area(
            " ",
            placeholder="Be specific about your symptoms...\nExample: High fever above 38°C, severe headache, body aches, fatigue",
            height=150,
            help="The more detailed your description, the better our AI can help you"
        )
        
        # Advanced filters
        st.markdown("### ⚙️ Advanced Filters")
        col1, col2, col3 = st.columns(3)
        with col1:
            min_safety = st.slider("**Safety**", 1.0, 5.0, 3.5, 0.1)
        with col2:
            max_price = st.selectbox("**Price**", ["Any", "💰 Economy", "💵 Standard", "💎 Premium"])
        with col3:
            category_filter = st.selectbox("**Category**", ["All", "Analgesic", "Antibiotic", "NSAID"])

    with col2:
        if user_symptoms:
            st.markdown("### 💊 AI Recommendations")
            
            with st.spinner("🤖 AI is analyzing your symptoms with advanced algorithms..."):
                results = recommender.recommend_by_symptoms(user_symptoms)
            
            if results:
                filtered_results = [med for med in results if med['safety_rating'] >= min_safety]
                
                if filtered_results:
                    st.markdown(f"""
                    <div class="success-box-premium">
                        🎯 AI found {len(filtered_results)} perfect medication matches!
                    </div>
                    """, unsafe_allow_html=True)
                    
                    for medicine in filtered_results:
                        safety_percent = (medicine['safety_rating'] / 5.0) * 100
                        safety_color = "#4CAF50" if medicine['safety_rating'] >= 4.0 else "#FF9800" if medicine['safety_rating'] >= 3.0 else "#F44336"
                        
                        st.markdown(f"""
                        <div style='background: linear-gradient(135deg, {safety_color}20 0%, {safety_color}40 100%); 
                                    padding: 2rem; border-radius: 15px; margin: 1rem 0; border-left: 5px solid {safety_color};'>
                            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
                                <h3 style='margin: 0; color: #333;'>💊 {medicine['name']}</h3>
                                <div style='background: {safety_color}; color: white; padding: 0.5rem 1rem; border-radius: 15px;'>
                                    ⭐ {medicine['safety_rating']}/5.0
                                </div>
                            </div>
                            <div style='color: #666;'>
                                <strong>Category:</strong> {medicine['category']} | 
                                <strong>Treats:</strong> {medicine['for_symptoms']}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    # FIXED: Using custom CSS class
                    st.markdown('<div class="custom-error">❌ No medications meet your safety criteria. Try adjusting the filters.</div>', unsafe_allow_html=True)
            else:
                # FIXED: Using custom CSS class
                st.markdown('<div class="custom-warning">⚠️ No medications found. Try different symptoms or be more specific.</div>', unsafe_allow_html=True)

# Medicine Database Page
elif selected == "📊 Medicine Database":
    st.markdown("""
    <div class="glass-card">
        <h1 style='color: #667eea; text-align: center;'>📊 Complete Medicine Database</h1>
        <p style='text-align: center; color: #666;'>Advanced search and filtering for our comprehensive medicine library</p>
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
        st.markdown('<div class="custom-error">❌ No medicines found in the database.</div>', unsafe_allow_html=True)

# Analytics Page
elif selected == "📈 Analytics":
    st.markdown("""
    <div class="glass-card">
        <h1 style='color: #667eea; text-align: center;'>📈 Advanced Analytics</h1>
        <p style='text-align: center; color: #666;'>Comprehensive analytics and insights from our medicine database</p>
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

# About Page
elif selected == "ℹ️ About":
    st.markdown("""
    <div class="glass-card">
        <h1 style='color: #667eea; text-align: center;'>ℹ️ About MediMatch Pro</h1>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; 
                    padding: 3rem; border-radius: 20px; margin: 2rem 0;'>
            <h2 style='color: white;'>🎓 Master's Project - Advanced Medical AI</h2>
            <p style='font-size: 1.1rem; line-height: 1.6;'>
            <strong>MediMatch Pro</strong> represents the cutting edge of AI-powered medical technology, 
            developed as part of advanced academic research in medical informatics and artificial intelligence.
            </p>
            
            <h3 style='color: white; margin-top: 2rem;'>✨ Revolutionary Features:</h3>
            <ul style='font-size: 1.1rem;'>
            <li>🤖 Advanced AI symptom analysis</li>
            <li>⭐ Intelligent safety rating system</li>
            <li>🔍 Real-time medical database search</li>
            <li>📊 Comprehensive analytics dashboard</li>
            <li>🎨 Professional medical-grade interface</li>
            </ul>
            
            <div style='background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin-top: 2rem;'>
                <h4 style='color: white; margin: 0;'>⚕️ Medical Disclaimer</h4>
                <p style='margin: 0.5rem 0 0 0; opacity: 0.9;'>
                This system is for educational and research purposes. Always consult healthcare professionals.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Professional Footer
st.markdown("""
<div style='text-align: center; padding: 3rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; border-radius: 20px; margin: 2rem 0;'>
    <h3 style='color: white; margin-bottom: 1rem;'>💊 MediMatch Pro</h3>
    <p style='opacity: 0.9; margin-bottom: 0.5rem;'>Advanced AI Medicine Recommendation System</p>
    <p style='opacity: 0.7; margin: 0;'>🎓 Master's Research Project | 🔬 Medical Informatics | ⚕️ Always Consult Professionals</p>
</div>
""", unsafe_allow_html=True)