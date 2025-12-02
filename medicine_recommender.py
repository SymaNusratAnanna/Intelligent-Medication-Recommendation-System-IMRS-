# medicine_recommender.py - EXPANDED VERSION
import pandas as pd


class MedicineRecommender:
    def __init__(self):
        self.medicines_df = self.create_medicine_data()
        print("💊 Enhanced medicine database loaded successfully!")
    
    def create_medicine_data(self):
        """Create comprehensive medicine database"""
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
                
                # RESPIRATOSTRY
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