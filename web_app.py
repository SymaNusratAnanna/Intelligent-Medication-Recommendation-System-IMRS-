# web_app.py - COMPLETELY FIXED VERSION
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

# CSS Styling
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
    }
    
    .medicine-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        border-left: 5px solid #ff6b6b;
    }
</style>
""", unsafe_allow_html=True)

# Initialize recommender
@st.cache_resource
def load_recommender():
    return MedicineRecommender()

recommender = load_recommender()

# Header
st.markdown("""
<div style='text-align: center; padding: 3rem 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            border-radius: 0 0 50px 50px; margin: -2rem -2rem 2rem -2rem; color: white;'>
    <h1 class="main-header">💊 MediMatch Pro</h1>
    <h3 style='color: white; opacity: 0.9; margin-top: 0;'>AI-Powered Medicine Recommendation System</h3>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.9) 0%, rgba(118, 75, 162, 0.9) 100%); 
                padding: 2rem 1.5rem; border-radius: 20px; margin-bottom: 2rem; 
                color: white; text-align: center;'>
        <div style='font-size: 3rem; margin-bottom: 1rem;'>💊</div>
        <h2 style='color: white; margin: 0;'>MediMatch Pro</h2>
        <p style='margin: 0.5rem 0 0 0; opacity: 0.9;'>Medical Navigator</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation state
    if 'selected' not in st.session_state:
        st.session_state.selected = "🏠 Dashboard"
    
    # Navigation buttons
    if st.button("🏠 Dashboard", use_container_width=True):
        st.session_state.selected = "🏠 Dashboard"
    
    if st.button("🔍 Symptom Analyzer", use_container_width=True):
        st.session_state.selected = "🔍 Symptom Analyzer"
    
    if st.button("➕ Add Medicine", use_container_width=True):
        st.session_state.selected = "➕ Add Medicine"
    
    if st.button("📊 Medicine Database", use_container_width=True):
        st.session_state.selected = "📊 Medicine Database"
    
    # Quick stats
    try:
        st.markdown("---")
        st.markdown("### 📊 Quick Stats")
        stats = recommender.get_statistics()
        col1, col2 = st.columns(2)
        with col1:
            st.metric("💊 Total", stats['total_medicines'])
        with col2:
            st.metric("⭐ Safety", f"{stats['avg_safety']}/5.0")
    except:
        pass

# Get selected page
selected = st.session_state.selected

# =============================================
# DASHBOARD PAGE - FIXED
# =============================================
if selected == "🏠 Dashboard":
    st.markdown("""
    <div class="glass-card">
        <h1 style='color: #667eea; text-align: center;'>💊 MediMatch Pro Dashboard</h1>
        <p style='text-align: center; color: #666;'>Your intelligent medicine recommendation system</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Real-time statistics
    st.markdown("### 📊 Live Database Statistics")
    
    stats = recommender.get_statistics()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("💊 Total Medicines", stats['total_medicines'])
    with col2:
        st.metric("📋 Categories", stats['categories'])
    with col3:
        st.metric("⭐ Avg Safety", f"{stats['avg_safety']}/5.0")
    with col4:
        st.metric("🏆 High Safety", stats['high_safety_meds'])
    
    st.markdown("---")
    
    # =============================================
    # SYMPTOM SEARCH - FIXED AND WORKING
    # =============================================
    st.markdown("### 🔍 Quick Symptom Search")
    
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            symptoms = st.text_input(
                "**Describe your symptoms for instant recommendations:**",
                placeholder="fever, headache, pain, inflammation, allergy...",
                key="dashboard_symptoms"
            )
        with col2:
            st.write("")  # Spacer
            search_btn = st.button("🔍 Search", type="primary")
        
        # Search when button is clicked
        if search_btn or symptoms:
            if symptoms and symptoms.strip():
                with st.spinner("🔍 AI is analyzing your symptoms..."):
                    # Get results from database
                    results = recommender.recommend_by_symptoms(symptoms)
                
                if results:
                    st.success(f"✅ Found {len(results)} relevant medications!")
                    
                    # Display medicine cards
                    for medicine in results[:5]:  # Show top 5 results
                        st.markdown(f"""
                        <div class="medicine-card">
                            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
                                <h2 style='margin: 0; color: white;'>💊 {medicine['name']}</h2>
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
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Progress bar
                        safety_percent = (medicine['safety_rating'] / 5.0) * 100
                        st.progress(safety_percent / 100)
                        
                else:
                    st.warning(f"❌ No medications found for: '{symptoms}'. Try different symptoms.")
            else:
                st.info("💡 Please enter some symptoms to search for medications.")

# ==============================================
# SYMPTOM ANALYZER PAGE - FIXED
# =============================================
elif selected == "🔍 Symptom Analyzer":
    st.markdown("""
    <div class="glass-card">
        <h1 style='color: #667eea; text-align: center;'>🔍 AI Symptom Analyzer</h1>
        <p style='text-align: center; color: #666;'>Advanced AI-powered medicine recommendations</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📝 Describe Your Symptoms")
        user_symptoms = st.text_area(
            " ",
            placeholder="Describe your symptoms in detail...",
            height=150,
            key="symptom_analyzer_input"
        )
        
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
            
            with st.spinner("🤖 AI is analyzing your symptoms..."):
                results = recommender.recommend_by_symptoms(user_symptoms)
            
            if results:
                # Apply filters
                filtered_results = [med for med in results if med['safety_rating'] >= min_safety]
                
                if max_price != "Any":
                    filtered_results = [med for med in filtered_results if med['price_category'] == max_price]
                
                if category_filter != "All":
                    filtered_results = [med for med in filtered_results if category_filter.lower() in med['category'].lower()]
                
                if filtered_results:
                    st.success(f"✅ AI found {len(filtered_results)} perfect medication matches!")
                    
                    for medicine in filtered_results:
                        st.markdown(f"""
                        <div class="medicine-card">
                            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
                                <h2 style='margin: 0; color: white;'>💊 {medicine['name']}</h2>
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
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        safety_percent = (medicine['safety_rating'] / 5.0) * 100
                        st.progress(safety_percent / 100)
                        
                else:
                    st.error("❌ No medications meet your filter criteria.")
            else:
                st.warning("⚠️ No medications found. Try different symptoms.")
        else:
            st.info("💡 Please enter your symptoms to get AI recommendations")

# =============================================
# ADD MEDICINE PAGE
# =============================================
elif selected == "➕ Add Medicine":
    st.markdown("""
    <div class="glass-card">
        <h1 style='color: #667eea; text-align: center;'>➕ Add New Medicine</h1>
        <p style='text-align: center; color: #666;'>Add a new medicine to the database</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("add_medicine_form"):
        st.markdown("### 📝 Medicine Information")
        
        col1, col2 = st.columns(2)
        with col1:
            medicine_name = st.text_input("💊 Medicine Name*", placeholder="e.g., Paracetamol 500mg")
            category = st.selectbox("📋 Category*", ["Analgesic", "NSAID", "Antibiotic", "Antihistamine", "PPI", "Other"])
            safety_rating = st.slider("⭐ Safety Rating*", 1.0, 5.0, 4.0, 0.1)
        
        with col2:
            price_category = st.selectbox("💰 Price Category*", ["💰 Economy", "💵 Standard", "💎 Premium"])
            for_symptoms = st.text_area("🤒 Symptoms Treated*", placeholder="e.g., fever headache mild pain")
        
        submitted = st.form_submit_button("💾 Add Medicine to Database", type="primary")
        
        if submitted:
            if not medicine_name or not for_symptoms or not category:
                st.error("❌ Please fill in all required fields (*)")
            else:
                medicine_data = {
                    'name': medicine_name,
                    'for_symptoms': for_symptoms,
                    'category': category,
                    'safety_rating': safety_rating,
                    'price_category': price_category
                }
                
                success, message = recommender.add_medicine(medicine_data)
                if success:
                    st.success(message)
                    st.balloons()
                else:
                    st.error(message)

# =============================================
# MEDICINE DATABASE PAGE
# =============================================
elif selected == "📊 Medicine Database":
    st.markdown("""
    <div class="glass-card">
        <h1 style='color: #667eea; text-align: center;'>📊 Complete Medicine Database</h1>
        <p style='text-align: center; color: #666;'>Browse all available medicines</p>
    </div>
    """, unsafe_allow_html=True)
    
    all_medicines = recommender.get_all_medicines()
    
    if all_medicines:
        df = pd.DataFrame(all_medicines)
        st.dataframe(df, use_container_width=True)
    else:
        st.error("❌ No medicines found in the database.")
# # =============================================
# # ADD MEDICINE PAGE - NEW FEATURE
# # =============================================
# if selected == "➕ Add Medicine":
#     st.markdown("""
#     <div class="glass-card">
#         <h1 style='color: #667eea; text-align: center;'>➕➕ Add New Medicine</h1>
#         <p style='text-align: center; color: #666;'>Add a new medicine to the database with all required information</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Medicine form
#     with st.form("add_medicine_form"):
#         st.markdown("### 📝📝 Medicine Information")
        
#         col1, col2 = st.columns(2)
#         with col1:
#             medicine_name = st.text_input("💊💊 Medicine Name*", placeholder="e.g., Paracetamol 500mg")
#             category = st.selectbox("📋📋 Category*", [
#                 "Analgesic", "NSAID", "Antibiotic", "Antihistamine", "PPI", "H2 Blocker", 
#                 "Bronchodilator", "Statin", "Vitamin", "Mineral", "Other"
#             ])
#             safety_rating = st.slider("⭐ Safety Rating*", 1.0, 5.0, 4.0, 0.1)
        
#         with col2:
#             price_category = st.selectbox("💰💰 Price Category*", 
#                 ["💰 Economy", "💵💵 Standard", "💎💎 Premium"])
#             dosage_form = st.text_input("💊💊 Dosage Form", placeholder="e.g., Tablet 500mg, Inhaler")
#             duration = st.text_input("⏰⏰ Duration", placeholder="e.g., 4-6 hours, Once daily")
        
#         # Symptoms and usage
#         for_symptoms = st.text_area("🤒🤒 Symptoms Treated*", 
#             placeholder="e.g., fever headache mild pain", 
#             help="Describe what symptoms this medicine treats")
        
#         primary_use = st.text_input("🎯🎯 Primary Use", 
#             placeholder="e.g., Analgesic & Antipyretic")
        
#         key_info = st.text_area("💡💡 Key Information", 
#             placeholder="Important medical information, precautions, etc.",
#             height=100)
        
#         drug_class = st.text_input("🔬🔬 Drug Class", 
#             placeholder="e.g., Non-opioid analgesic, SSRI")
        
#         # Submit button
#         submitted = st.form_submit_button("💾💾 Add Medicine to Database", type="primary")
        
#         if submitted:
#             # Validate required fields
#             if not medicine_name or not for_symptoms or not category:
#                 st.error("❌❌ Please fill in all required fields (*)")
#             else:
#                 # Prepare medicine data
#                 medicine_data = {
#                     'name': medicine_name,
#                     'for_symptoms': for_symptoms,
#                     'category': category,
#                     'safety_rating': safety_rating,
#                     'price_category': price_category,
#                     'key_info': key_info,
#                     'primary_use': primary_use,
#                     'drug_class': drug_class,
#                     'dosage_form': dosage_form,
#                     'duration': duration
#                 }
                
#              # Add medicine to database
#                 success, message = recommender.add_medicine(medicine_data)
#                 if success:
#                     st.success(message)
#                     st.balloons()
                    
#                    # Show updated count
#                     total_medicines = recommender.get_total_medicines_count()
#                     st.info(f"📊📊 Total medicines in database: {total_medicines}")
                    
#                     # Show user-added count
#                     user_added_count = recommender.get_user_added_medicines_count()
#                     st.info(f"➕➕ User-added medicines: {user_added_count}")
#                 else:
#                     st.error(message)




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

# simple_web_test.py - EASY ONE-CLICK TEST
def quick_web_test():
    """Quick test to verify web-app is working"""
    
    print("🌐 QUICK WEB-APP TEST")
    print("=" * 50)
    
    from medicine_recommender import MedicineRecommender
    
    try:
        # Initialize
        recommender = MedicineRecommender()
        
        print("1. Testing database connection...")
        all_meds = recommender.get_all_medicines()
        print(f"   ✅ Database loaded: {len(all_meds)} medicines")
        
        print("2. Testing symptom search...")
        results = recommender.recommend_by_symptoms("fever headache")
        print(f"   ✅ Search working: {len(results)} results found")
        
        print("3. Testing web data format...")
        if results:
            sample = results[0]
            required = ['name', 'safety_rating', 'category', 'for_symptoms']
            missing = [field for field in required if field not in sample]
            
            if not missing:
                print("   ✅ Data format is web-ready")
                print(f"   💊 Sample: {sample['name']} (⭐{sample['safety_rating']})")
            else:
                print(f"   ❌ Missing fields: {missing}")
                return False
        else:
            print("   ❌ No results found")
            return False
        
        print("4. Testing performance...")
        import time
        start = time.time()
        recommender.recommend_by_symptoms("pain")
        end = time.time()
        response_time = (end - start) * 1000
        
        if response_time < 500:
            print(f"   ✅ Performance good: {response_time:.1f}ms")
        else:
            print(f"   ⚠️ Performance slow: {response_time:.1f}ms")
        
        print("\n🎉 WEB-APP IS WORKING CORRECTLY! 🚀")
        return True
        
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return False

if __name__ == "__main__":
    quick_web_test()


    


