# medicine_recommender.py - COMPLETE ENHANCED VERSION
import pandas as pd

class MedicineRecommender:
    
    def __init__(self):
        self.medicines_df = self.create_medicine_data()
        print("💊 Enhanced medicine database with detailed information loaded successfully!")
    
    def create_medicine_data(self):
        """Create comprehensive medicine database with enhanced information"""
        data = {
            'name': [
                # ANALGESICS & PAIN RELIEVERS
                'Paracetamol 500mg', 'Ibuprofen 400mg', 'Aspirin 100mg', 
                'Diclofenac 50mg', 'Naproxen 250mg', 'Tramadol 50mg',
                
                # ANTIBIOTICS
                'Amoxicillin 250mg', 'Azithromycin 250mg', 'Ciprofloxacin 250mg',
                'Doxycycline 100mg', 'Erythromycin 250mg', 'Cephalexin 250mg',
                
                # ANTIHISTAMINES & ALLERGY
                'Cetirizine 10mg', 'Loratadine 10mg', 'Fexofenadine 120mg',
                'Diphenhydramine 25mg', 'Chlorpheniramine 4mg',
                
                # GASTROINTESTINAL
                'Omeprazole 20mg', 'Ranitidine 150mg', 'Pantoprazole 40mg',
                'Domperidone 10mg', 'Loperamide 2mg', 'Metoclopramide 10mg',
                
                # RESPIRATORY
                'Salbutamol Inhaler', 'Budesonide Inhaler', 'Montelukast 10mg',
                'Guaifenesin 400mg', 'Ambroxol 30mg',
                
                # CARDIAC & BLOOD PRESSURE
                'Atorvastatin 10mg', 'Amlodipine 5mg', 'Metoprolol 25mg',
                'Losartan 50mg', 'Hydrochlorothiazide 25mg',
                
                # DIABETES
                'Metformin 500mg', 'Glibenclamide 5mg', 'Insulin Glargine',
                
                # MENTAL HEALTH
                'Sertraline 50mg', 'Fluoxetine 20mg', 'Alprazolam 0.25mg',
                'Diazepam 5mg',
                
                # SKIN & TOPICAL
                'Hydrocortisone Cream 1%', 'Clotrimazole Cream 1%',
                'Mupirocin Ointment 2%', 'Benzoyl Peroxide Gel 5%',
                
                # VITAMINS & SUPPLEMENTS
                'Vitamin C 500mg', 'Vitamin D3 1000IU', 'Zinc 50mg',
                'Calcium 600mg', 'Iron 65mg'
            ],
            'for_symptoms': [
                # ANALGESICS
                'fever headache mild pain', 'pain inflammation fever menstrual cramps',
                'pain fever inflammation heart attack prevention', 'pain inflammation arthritis',
                'pain inflammation menstrual cramps', 'moderate severe pain chronic pain',
                
                # ANTIBIOTICS
                'bacterial infection throat infection ear infection', 'bacterial infection respiratory infection',
                'urinary tract infection bacterial infection', 'bacterial infection acne malaria prevention',
                'bacterial infection respiratory infection', 'bacterial infection skin infection',
                
                # ANTIHISTAMINES
                'allergy sneezing itching runny nose', 'allergy hay fever itching',
                'allergy chronic hives', 'allergy insomnia motion sickness', 'allergy common cold',
                
                # GASTROINTESTINAL
                'heartburn acid reflux ulcer', 'heartburn acid indigestion', 'acid reflux GERD ulcer',
                'nausea vomiting indigestion', 'diarrhea', 'nausea vomiting gastroparesis',
                
                # RESPIRATORY
                'asthma bronchitis breathing difficulty', 'asthma COPD inflammation',
                'asthma allergic rhinitis', 'cough chest congestion', 'cough bronchitis',
                
                # CARDIAC
                'high cholesterol heart disease prevention', 'high blood pressure chest pain',
                'high blood pressure heart rate angina', 'high blood pressure kidney protection',
                'high blood pressure edema fluid retention',
                
                # DIABETES
                'diabetes type 2 high blood sugar', 'diabetes type 2', 'diabetes type 1 insulin dependent',
                
                # MENTAL HEALTH
                'depression anxiety OCD', 'depression panic disorder', 'anxiety panic disorder',
                'anxiety muscle spasm alcohol withdrawal',
                
                # SKIN
                'skin inflammation itching eczema', 'fungal infection ringworm athletes foot',
                'bacterial skin infection impetigo', 'acne pimples skin inflammation',
                
                # VITAMINS
                'immune support cold prevention', 'bone health calcium absorption', 'immune support wound healing',
                'bone health osteoporosis prevention', 'anemia iron deficiency'
            ],
            'category': [
                # ANALGESICS
                'Analgesic', 'NSAID', 'NSAID', 'NSAID', 'NSAID', 'Opioid Analgesic',
                
                # ANTIBIOTICS
                'Antibiotic', 'Antibiotic', 'Antibiotic', 'Antibiotic', 'Antibiotic', 'Antibiotic',
                
                # ANTIHISTAMINES
                'Antihistamine', 'Antihistamine', 'Antihistamine', 'Antihistamine', 'Antihistamine',
                
                # GASTROINTESTINAL
                'PPI', 'H2 Blocker', 'PPI', 'Prokinetic', 'Antidiarrheal', 'Antiemetic',
                
                # RESPIRATORY
                'Bronchodilator', 'Corticosteroid', 'Leukotriene Inhibitor', 'Expectorant', 'Mucolytic',
                
                # CARDIAC
                'Statin', 'Calcium Channel Blocker', 'Beta Blocker', 'ARB', 'Diuretic',
                
                # DIABETES
                'Biguanide', 'Sulfonylurea', 'Insulin',
                
                # MENTAL HEALTH
                'SSRI', 'SSRI', 'Benzodiazepine', 'Benzodiazepine',
                
                # SKIN
                'Corticosteroid', 'Antifungal', 'Antibiotic', 'Antiacne',
                
                # VITAMINS
                'Vitamin', 'Vitamin', 'Mineral', 'Mineral', 'Mineral'
            ],
            'safety_rating': [
                # Safety ratings (1-5 scale)
                4.5, 4.0, 4.1, 3.8, 3.9, 3.2,  # Analgesics
                4.2, 4.1, 3.9, 3.8, 3.7, 4.0,   # Antibiotics
                4.3, 4.2, 4.3, 3.5, 4.1,        # Antihistamines
                4.4, 4.2, 4.3, 3.9, 4.0, 3.8,   # Gastrointestinal
                4.1, 4.0, 4.2, 4.3, 4.1,        # Respiratory
                4.2, 4.0, 3.9, 4.1, 3.8,         # Cardiac
                4.3, 3.7, 4.0,                   # Diabetes
                3.9, 3.8, 3.2, 3.1,             # Mental Health
                4.4, 4.3, 4.2, 4.1,             # Skin
                4.8, 4.7, 4.6, 4.5, 4.4         # Vitamins
            ],
            'price_category': [  # Price categories for filtering
                '💰 Economy', '💵 Standard', '💰 Economy', '💵 Standard', '💵 Standard', '💎 Premium',  # Analgesics
                '💰 Economy', '💵 Standard', '💵 Standard', '💰 Economy', '💰 Economy', '💵 Standard',  # Antibiotics
                '💰 Economy', '💰 Economy', '💵 Standard', '💰 Economy', '💰 Economy',                 # Antihistamines
                '💎 Premium', '💰 Economy', '💎 Premium', '💵 Standard', '💰 Economy', '💵 Standard',  # Gastrointestinal
                '💰 Economy', '💎 Premium', '💵 Standard', '💰 Economy', '💵 Standard',                # Respiratory
                '💎 Premium', '💵 Standard', '💰 Economy', '💵 Standard', '💰 Economy',                # Cardiac
                '💰 Economy', '💰 Economy', '💎 Premium',                                              # Diabetes
                '💵 Standard', '💰 Economy', '💵 Standard', '💵 Standard',                            # Mental Health
                '💰 Economy', '💰 Economy', '💵 Standard', '💰 Economy',                              # Skin
                '💰 Economy', '💰 Economy', '💰 Economy', '💰 Economy', '💰 Economy'                  # Vitamins
            ],
            'key_info': [  # Detailed medical information
                'First-line for mild-moderate pain. Max 4g/day. Avoid alcohol.',
                'Take with food. GI and kidney precautions. Anti-inflammatory.',
                'Low-dose for heart protection. GI bleeding risk. Not for children.',
                'Powerful NSAID. Monitor liver and kidney function. Take with food.',
                'Longer acting NSAID. Good for chronic pain. Take with food.',
                'Opioid analgesic. Risk of dependence. Schedule IV controlled substance.',
                
                'Penicillin antibiotic. Complete full course. Check for allergies.',
                'Macrolide antibiotic. Once daily dosing. Fewer GI side effects.',
                'Fluoroquinolone. Tendon rupture risk. Avoid in children and adolescents.',
                'Tetracycline. Photosensitivity risk. Take with plenty of water.',
                'Macrolide. Multiple drug interactions. GI side effects common.',
                'First-generation cephalosporin. Good for skin infections.',
                
                'Non-drowsy formula. Once daily. Few side effects.',
                'Non-sedating. Once daily. Minimal drug interactions.',
                'Third-generation. Non-drowsy. Safe for long-term use.',
                'First-generation. Causes drowsiness. Also used for sleep aid.',
                'Classic antihistamine. Affordable. Mild drowsiness possible.',
                
                'Proton pump inhibitor. Take before meals. Long-term use monitoring needed.',
                'H2 blocker. Being phased out due to safety concerns.',
                'PPI with fewer interactions. Good for GERD.',
                'Prokinetic agent. QT prolongation risk. Lactation use.',
                'Antidiarrheal. Not for infectious diarrhea. Opioid derivative.',
                'Antiemetic. Extrapyramidal side effects risk. Short-term use.',
                
                'Bronchodilator. Rescue medication. Short-acting.',
                'Inhaled corticosteroid. Maintenance therapy. Rinse mouth after use.',
                'Leukotriene inhibitor. Once daily. Good for allergy-induced asthma.',
                'Expectorant. Thins mucus. Stay hydrated.',
                'Mucolytic. Breaks down thick mucus. Good for productive cough.',
                
                'Statin. Cholesterol lowering. Take in evening.',
                'Calcium channel blocker. For hypertension and angina.',
                'Beta blocker. Slows heart rate. Avoid in asthma.',
                'ARB. Blood pressure control. Kidney protective.',
                'Diuretic. Removes excess fluid. Monitor electrolytes.',
                
                'First-line for type 2 diabetes. GI side effects common.',
                'Stimulates insulin secretion. Hypoglycemia risk.',
                'Long-acting basal insulin. Once daily injection.',
                
                'SSRI antidepressant. Takes 4-6 weeks for full effect.',
                'SSRI with long half-life. Good for compliance.',
                'Benzodiazepine. Fast-acting. High addiction potential.',
                'Long-acting benzodiazepine. Muscle relaxant properties.',
                
                'Topical steroid. Mild potency. Avoid face and broken skin.',
                'Antifungal cream. Apply to clean dry area.',
                'Topical antibiotic. For skin infections. Not for deep wounds.',
                'Antiacne treatment. May bleach fabrics. Start with lower concentration.',
                
                'Antioxidant. Immune support. Water soluble.',
                'Bone health. Calcium absorption. Sunlight vitamin.',
                'Immune function. Wound healing. Mineral supplement.',
                'Bone health. Take with vitamin D for better absorption.',
                'For iron deficiency anemia. May cause constipation.'
            ],
            # ✅ NEW: ADDED DETAILED MEDICAL INFORMATION
            'primary_use': [
                # ANALGESICS
                'Analgesic & Antipyretic (Pain & Fever relief)',
                'NSAID - Inflammation, Pain, Fever reduction',
                'Pain relief & cardiovascular protection',
                'NSAID - Arthritis, Pain, Inflammation',
                'NSAID - Chronic pain, Inflammation',
                'Opioid - Moderate to severe pain relief',
                
                # ANTIBIOTICS
                'Bacterial infections treatment',
                'Broad-spectrum antibiotic for respiratory infections',
                'Urinary tract and bacterial infections',
                'Bacterial infections, Acne, Malaria prevention',
                'Respiratory and skin infections',
                'Bacterial skin and respiratory infections',
                
                # ANTIHISTAMINES
                'Antihistamine for allergy relief',
                'Non-sedating allergy relief',
                'Chronic allergy and hives treatment',
                'Allergy relief and sleep aid',
                'Classic antihistamine for allergies',
                
                # GASTROINTESTINAL
                'Acid reflux & ulcer treatment',
                'Heartburn and acid indigestion',
                'GERD and acid-related conditions',
                'Nausea and vomiting relief',
                'Diarrhea treatment',
                'Nausea and gastroparesis',
                
                # RESPIRATORY
                'Asthma and COPD symptom relief',
                'Asthma inflammation control',
                'Asthma and allergy prevention',
                'Cough and chest congestion relief',
                'Productive cough treatment',
                
                # CARDIAC
                'Cholesterol reduction',
                'High blood pressure treatment',
                'Blood pressure and heart rate control',
                'Blood pressure management',
                'Fluid retention and blood pressure',
                
                # DIABETES
                'Type 2 diabetes management',
                'Diabetes blood sugar control',
                'Insulin-dependent diabetes',
                
                # MENTAL HEALTH
                'Depression and anxiety treatment',
                'Depression and panic disorder',
                'Anxiety and panic disorder',
                'Anxiety and muscle relaxation',
                
                # SKIN
                'Skin inflammation and itching',
                'Fungal skin infections',
                'Bacterial skin infections',
                'Acne treatment',
                
                # VITAMINS
                'Immune system support',
                'Bone health and calcium absorption',
                'Immune function and wound healing',
                'Bone health maintenance',
                'Iron deficiency anemia treatment'
            ],
            'drug_class': [
                # ANALGESICS
                'Non-opioid analgesic',
                'Non-steroidal anti-inflammatory',
                'Salicylate, Antiplatelet agent',
                'NSAID',
                'NSAID',
                'Opioid analgesic',
                
                # ANTIBIOTICS
                'Penicillin antibiotic',
                'Macrolide antibiotic',
                'Fluoroquinolone antibiotic',
                'Tetracycline antibiotic',
                'Macrolide antibiotic',
                'Cephalosporin antibiotic',
                
                # ANTIHISTAMINES
                'H1-receptor antagonist',
                'Second-generation antihistamine',
                'Third-generation antihistamine',
                'First-generation antihistamine',
                'Classic antihistamine',
                
                # GASTROINTESTINAL
                'Proton pump inhibitor',
                'H2 receptor antagonist',
                'Proton pump inhibitor',
                'Dopamine antagonist',
                'Opioid receptor agonist',
                'Dopamine antagonist',
                
                # RESPIRATORY
                'Short-acting beta-agonist',
                'Inhaled corticosteroid',
                'Leukotriene receptor antagonist',
                'Expectorant',
                'Mucolytic agent',
                
                # CARDIAC
                'HMG-CoA reductase inhibitor',
                'Calcium channel blocker',
                'Beta-1 selective blocker',
                'Angiotensin receptor blocker',
                'Thiazide diuretic',
                
                # DIABETES
                'Biguanide antihyperglycemic',
                'Sulfonylurea',
                'Long-acting basal insulin',
                
                # MENTAL HEALTH
                'Selective serotonin reuptake inhibitor',
                'SSRI antidepressant',
                'Benzodiazepine',
                'Benzodiazepine',
                
                # SKIN
                'Topical corticosteroid',
                'Topical antifungal',
                'Topical antibiotic',
                'Antiacne preparation',
                
                # VITAMINS
                'Water-soluble vitamin',
                'Fat-soluble vitamin',
                'Essential mineral',
                'Mineral supplement',
                'Mineral supplement'
            ],
            'dosage_form': [
                # ANALGESICS
                'Tablet, 500mg', 'Tablet, 400mg', 'Enteric-coated tablet, 100mg',
                'Tablet, 50mg', 'Tablet, 250mg', 'Tablet, 50mg',
                
                # ANTIBIOTICS
                'Capsule, 250mg', 'Tablet, 250mg', 'Tablet, 250mg',
                'Capsule, 100mg', 'Tablet, 250mg', 'Capsule, 250mg',
                
                # ANTIHISTAMINES
                'Tablet, 10mg', 'Tablet, 10mg', 'Tablet, 120mg',
                'Tablet, 25mg', 'Tablet, 4mg',
                
                # GASTROINTESTINAL
                'Capsule, 20mg', 'Tablet, 150mg', 'Capsule, 40mg',
                'Tablet, 10mg', 'Capsule, 2mg', 'Tablet, 10mg',
                
                # RESPIRATORY
                'Metered dose inhaler', 'Inhaler', 'Chewable tablet, 10mg',
                'Tablet, 400mg', 'Tablet, 30mg',
                
                # CARDIAC
                'Tablet, 10mg', 'Tablet, 5mg', 'Tablet, 25mg',
                'Tablet, 50mg', 'Tablet, 25mg',
                
                # DIABETES
                'Tablet, 500mg', 'Tablet, 5mg', 'Injection pen',
                
                # MENTAL HEALTH
                'Tablet, 50mg', 'Capsule, 20mg', 'Tablet, 0.25mg',
                'Tablet, 5mg',
                
                # SKIN
                'Cream, 1%', 'Cream, 1%', 'Ointment, 2%', 'Gel, 5%',
                
                # VITAMINS
                'Tablet, 500mg', 'Softgel, 1000IU', 'Tablet, 50mg',
                'Tablet, 600mg', 'Tablet, 65mg'
            ],
            'duration': [
                # ANALGESICS
                '4-6 hours', '6-8 hours', '4-6 hours (analgesic), 24 hours (antiplatelet)',
                '8-12 hours', '12 hours', '4-6 hours',
                
                # ANTIBIOTICS
                '7-10 day course', '3-5 day course', '7-14 day course',
                '7-10 day course', '7-10 day course', '7-10 day course',
                
                # ANTIHISTAMINES
                '24 hours', '24 hours', '24 hours', '4-6 hours', '4-6 hours',
                
                # GASTROINTESTINAL
                'Once daily, 4-8 weeks', 'Twice daily', 'Once daily',
                'As needed', 'As needed', 'Before meals',
                
                # RESPIRATORY
                '4-6 hours as needed', 'Twice daily maintenance', 'Once daily',
                'Every 4 hours', 'Three times daily',
                
                # CARDIAC
                'Once daily, long-term', 'Once daily', 'Once or twice daily',
                'Once daily', 'Once daily in morning',
                
                # DIABETES
                'Twice daily with meals', 'Once daily with breakfast', 'Once daily injection',
                
                # MENTAL HEALTH
                'Once daily, long-term', 'Once daily', 'As needed', '2-4 times daily as needed',
                
                # SKIN
                'Apply 2-3 times daily', 'Apply twice daily', 'Apply 3 times daily', 'Apply once daily',
                
                # VITAMINS
                'Once daily', 'Once daily', 'Once daily', 'Once daily with food', 'Once daily'
            ]
        }
        return pd.DataFrame(data)
    
    def recommend_by_symptoms(self, user_symptoms):
        """Enhanced symptom matching with better logic"""
        recommendations = []
        user_symptoms_lower = user_symptoms.lower()
        
        for _, medicine in self.medicines_df.iterrows():
            medicine_symptoms = medicine['for_symptoms'].lower()
            
            # Improved matching: check if any symptom word matches
            symptom_words = [word.strip() for word in user_symptoms_lower.split(',')]
            match_found = False
            
            for symptom in symptom_words:
                if symptom and symptom in medicine_symptoms:
                    match_found = True
                    break
            
            if match_found:
                recommendations.append({
                    'name': medicine['name'],
                    'for_symptoms': medicine['for_symptoms'],
                    'category': medicine['category'],
                    'safety_rating': medicine['safety_rating'],
                    'price_category': medicine['price_category'],
                    'key_info': medicine['key_info'],
                    'primary_use': medicine['primary_use'],
                    'drug_class': medicine['drug_class'],
                    'dosage_form': medicine['dosage_form'],
                    'duration': medicine['duration'],
                    'match_strength': self.calculate_match_strength(symptom_words, medicine_symptoms)
                })
        
        # Sort by safety rating and match strength
        recommendations.sort(key=lambda x: (x['safety_rating'], x.get('match_strength', 0)), reverse=True)
        return recommendations
    
    def calculate_match_strength(self, user_symptoms, medicine_symptoms):
        """Calculate how well the medicine matches symptoms"""
        matches = 0
        for symptom in user_symptoms:
            if symptom and symptom in medicine_symptoms:
                matches += 1
        return matches / len(user_symptoms) if user_symptoms else 0
    
    def get_all_medicines(self):
        """Return all medicines with additional info"""
        return self.medicines_df.to_dict('records')
    
    def search_medicine(self, medicine_name):
        """Search medicine by name"""
        results = self.medicines_df[
            self.medicines_df['name'].str.contains(medicine_name, case=False, na=False)
        ]
        return results.to_dict('records')
    
    def get_medicines_by_category(self, category):
        """Get medicines by category"""
        results = self.medicines_df[
            self.medicines_df['category'].str.contains(category, case=False, na=False)
        ]
        return results.to_dict('records')
    
    def get_statistics(self):
        """Get comprehensive statistics for dashboard"""
        all_meds = self.get_all_medicines()
        
        if not all_meds:
            return {
                'total_medicines': 0,
                'categories': 0,
                'avg_safety': 0,
                'price_distribution': {},
                'category_distribution': {}
            }
        
        # Calculate statistics
        safety_ratings = [med.get('safety_rating', 0) for med in all_meds]
        categories = list(set(med.get('category', 'Unknown') for med in all_meds))
        
        # Price distribution
        price_counts = {}
        for med in all_meds:
            price_cat = med.get('price_category', 'Unknown')
            price_counts[price_cat] = price_counts.get(price_cat, 0) + 1
        
        # Category distribution
        category_counts = {}
        for med in all_meds:
            category = med.get('category', 'Unknown')
            category_counts[category] = category_counts.get(category, 0) + 1
        
        return {
            'total_medicines': len(all_meds),
            'categories': len(categories),
            'avg_safety': round(sum(safety_ratings) / len(safety_ratings), 2) if safety_ratings else 0,
            'price_distribution': price_counts,
            'category_distribution': category_counts,
            'high_safety_meds': len([med for med in all_meds if med.get('safety_rating', 0) >= 4.0])
        }
    
    def get_medicines_by_price(self, price_category):
        """Get medicines by price category"""
        results = self.medicines_df[
            self.medicines_df['price_category'].str.contains(price_category, case=False, na=False)
        ]
        return results.to_dict('records')
    
    def get_top_safe_medicines(self, limit=5):
        """Get top safest medicines"""
        sorted_meds = self.medicines_df.sort_values('safety_rating', ascending=False)
        return sorted_meds.head(limit).to_dict('records')