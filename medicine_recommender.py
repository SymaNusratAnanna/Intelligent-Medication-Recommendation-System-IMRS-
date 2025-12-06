# medicine_recommender.py - FINAL 100% WORKING VERSION
import pandas as pd

class MedicineRecommender:
    
    def __init__(self):
        self.medicines_df = self.create_medicine_data()
        self.user_added_medicines = []
        print("Enhanced medicine database loaded successfully!")

    def create_medicine_data(self):
        """Create comprehensive medicine database"""
        data = {
            'name': [
                'Paracetamol 500mg', 'Ibuprofen 400mg', 'Aspirin 100mg', 'Diclofenac 50mg', 'Naproxen 250mg', 'Tramadol 50mg',
                'Amoxicillin 250mg', 'Azithromycin 250mg', 'Ciprofloxacin 250mg', 'Doxycycline 100mg', 'Erythromycin 250mg', 'Cephalexin 250mg',
                'Cetirizine 10mg', 'Loratadine 10mg', 'Fexofenadine 120mg', 'Diphenhydramine 25mg', 'Chlorpheniramine 4mg',
                'Omeprazole 20mg', 'Ranitidine 150mg', 'Pantoprazole 40mg', 'Domperidone 10mg', 'Loperamide 2mg', 'Metoclopramide 10mg',
                'Salbutamol Inhaler', 'Budesonide Inhaler', 'Montelukast 10mg', 'Guaifenesin 400mg', 'Ambroxol 30mg',
                'Atorvastatin 10mg', 'Amlodipine 5mg', 'Metoprolol 25mg', 'Losartan 50mg', 'Hydrochlorothiazide 25mg',
                'Metformin 500mg', 'Glibenclamide 5mg', 'Insulin Glargine',
                'Sertraline 50mg', 'Fluoxetine 20mg', 'Alprazolam 0.25mg', 'Diazepam 5mg',
                'Hydrocortisone Cream 1%', 'Clotrimazole Cream 1%', 'Mupirocin Ointment 2%', 'Benzoyl Peroxide Gel 5%',
                'Vitamin C 500mg', 'Vitamin D3 1000IU', 'Zinc 50mg', 'Calcium 600mg', 'Iron 65mg'
            ],
            'for_symptoms': [
                'fever headache mild pain body ache', 'pain inflammation fever menstrual cramps joint pain', 'pain fever inflammation heart protection',
                'pain inflammation arthritis back pain', 'pain inflammation menstrual cramps muscle pain', 'moderate severe pain chronic pain',
                'bacterial infection throat infection ear infection pneumonia', 'bacterial infection respiratory infection sinusitis', 'urinary tract infection bacterial infection',
                'bacterial infection acne malaria prevention', 'bacterial infection respiratory infection stomach infection', 'bacterial infection skin infection cellulitis',
                'allergy sneezing itching runny nose hay fever', 'allergy hay fever itching hives', 'allergy chronic hives itching', 
                'allergy insomnia motion sickness drowsiness', 'allergy common cold sneezing',
                'heartburn acid reflux ulcer GERD', 'heartburn acid indigestion ulcer', 'acid reflux GERD ulcer stomach pain',
                'nausea vomiting indigestion motion sickness', 'diarrhea loose motion', 'nausea vomiting gastroparesis',
                'asthma wheezing breathing difficulty bronchitis', 'asthma COPD inflammation cough', 'asthma allergic rhinitis wheezing',
                'cough chest congestion mucus phlegm', 'cough bronchitis thick mucus',
                'high cholesterol heart disease prevention', 'high blood pressure chest pain angina', 'high blood pressure heart rate control',
                'high blood pressure kidney protection', 'high blood pressure edema swelling fluid retention',
                'diabetes type 2 high blood sugar', 'diabetes type 2 blood sugar control', 'diabetes type 1 insulin dependent',
                'depression anxiety OCD stress', 'depression panic disorder OCD', 'anxiety panic disorder stress', 'anxiety muscle spasm insomnia',
                'skin inflammation itching eczema rash', 'fungal infection ringworm athletes foot', 'bacterial skin infection impetigo boil',
                'acne pimples blackheads skin inflammation',
                'immune support cold prevention fatigue', 'bone health calcium absorption weakness', 'immune support wound healing taste loss',
                'bone health osteoporosis prevention', 'anemia iron deficiency tiredness weakness'
            ],
            'category': [
                'Analgesic', 'NSAID', 'NSAID', 'NSAID', 'NSAID', 'Opioid Analgesic',
                'Antibiotic', 'Antibiotic', 'Antibiotic', 'Antibiotic', 'Antibiotic', 'Antibiotic',
                'Antihistamine', 'Antihistamine', 'Antihistamine', 'Antihistamine', 'Antihistamine',
                'PPI', 'H2 Blocker', 'PPI', 'Prokinetic', 'Antidiarrheal', 'Antiemetic',
                'Bronchodilator', 'Corticosteroid', 'Leukotriene Inhibitor', 'Expectorant', 'Mucolytic',
                'Statin', 'Calcium Channel Blocker', 'Beta Blocker', 'ARB', 'Diuretic',
                'Biguanide', 'Sulfonylurea', 'Insulin',
                'SSRI', 'SSRI', 'Benzodiazepine', 'Benzodiazepine',
                'Corticosteroid', 'Antifungal', 'Antibiotic', 'Antiacne',
                'Vitamin', 'Vitamin', 'Mineral', 'Mineral', 'Mineral'
            ],
            'safety_rating': [
                4.5, 4.0, 4.1, 3.8, 3.9, 3.2, 4.2, 4.1, 3.9, 3.8, 3.7, 4.0,
                4.3, 4.2, 4.3, 3.5, 4.1, 4.4, 4.2, 4.3, 3.9, 4.0, 3.8,
                4.1, 4.0, 4.2, 4.3, 4.1, 4.2, 4.0, 3.9, 4.1, 3.8,
                4.3, 3.7, 4.0, 3.9, 3.8, 3.2, 3.1, 4.4, 4.3, 4.2, 4.1,
                4.8, 4.7, 4.6, 4.5, 4.4
            ],
            'price_category': [
                'Economy', 'Standard', 'Economy', 'Standard', 'Standard', 'Premium',
                'Economy', 'Standard', 'Standard', 'Economy', 'Economy', 'Standard',
                'Economy', 'Economy', 'Standard', 'Economy', 'Economy',
                'Premium', 'Economy', 'Premium', 'Standard', 'Economy', 'Standard',
                'Economy', 'Premium', 'Standard', 'Economy', 'Standard',
                'Premium', 'Standard', 'Economy', 'Standard', 'Economy',
                'Economy', 'Economy', 'Premium', 'Standard', 'Economy', 'Standard', 'Standard',
                'Economy', 'Economy', 'Standard', 'Economy',
                'Economy', 'Economy', 'Economy', 'Economy', 'Economy'
            ],
            'key_info': [
                'First-line for mild-moderate pain. Max 4g/day. Safe in pregnancy.',
                'Take with food. Avoid in stomach ulcer or asthma.',
                'Low-dose for heart protection. Avoid in children (Reye syndrome).',
                'Strong NSAID. Take with food. Risk of stomach bleeding.',
                'Long-acting NSAID. Good for arthritis.',
                'Controlled opioid. Risk of addiction.',
                'Complete full course. Check penicillin allergy.',
                'Once daily. Good for respiratory infections.',
                'Avoid in pregnancy. Tendon rupture risk.',
                'Take with water. Avoid sunlight.',
                'Many drug interactions.',
                'Good for skin infections.',
                'Non-drowsy. Once daily.',
                'Non-drowsy. Safe long-term.',
                'Very safe. Long-term use OK.',
                'Causes drowsiness. Used as sleep aid.',
                'Classic antihistamine.',
                'Take 30 min before food. Long-term use needs monitoring.',
                'Being replaced by PPIs.',
                'Better than Omeprazole in some cases.',
                'Can cause tremors. Avoid alcohol.',
                'Stops diarrhea quickly. Not for infection.',
                'Can cause muscle spasms. Short-term use.',
                'Rescue inhaler. Use when short of breath.',
                'Maintenance inhaler. Rinse mouth after use.',
                'Once daily tablet for asthma control.',
                'Loosens mucus. Drink water.',
                'Breaks down thick mucus.',
                'Take at night. Muscle pain = stop immediately.',
                'For blood pressure and angina.',
                'Slows heart rate. Avoid in asthma.',
                'Protects kidneys in diabetes.',
                'Removes excess water.',
                'First choice for type 2 diabetes.',
                'Can cause low sugar.',
                'Long-acting insulin. Inject once daily.',
                'Takes 4-6 weeks to work.',
                'Long half-life. Good for missing doses.',
                'Fast acting. High addiction risk.',
                'Long acting. Muscle relaxant.',
                'Mild steroid cream. Avoid face.',
                'For fungal infections. 2-4 weeks.',
                'For bacterial skin infections.',
                'For acne. May cause dryness.',
                'Boosts immunity. Safe daily.',
                'Essential for bones. Take with calcium.',
                'Boosts immunity and healing.',
                'Take with Vitamin D.',
                'For anemia. Take with Vitamin C.'
            ]
        }
        return pd.DataFrame(data)

    def recommend_by_symptoms(self, user_symptoms):
        """FIXED: Now returns list, works with spaces/commas/sentences"""
        if not user_symptoms or not user_symptoms.strip():
            return []

        user_input = user_symptoms.lower().strip()

        # Handle both comma and space separation
        if ',' in user_input:
            words = [w.strip() for w in user_input.split(',') if w.strip()]
        else:
            words = [w.strip() for w in user_input.split() if w.strip()]

        # Remove filler words
        stop_words = {'i', 'have', 'am', 'feeling', 'with', 'and', 'the', 'a', 'an', 'my', 'me', 'in', 'on', 'for', 'very', 'too', 'having', 'feel', 'is', 'got', 'been'}
        symptom_words = [w for w in words if w not in stop_words and len(w) > 2]

        if not symptom_words:
            return []

        recommendations = []
        for _, med in self.medicines_df.iterrows():
            med_symptoms = med['for_symptoms'].lower()
            matches = sum(1 for word in symptom_words if word in med_symptoms)

            if matches > 0:
                strength = matches / len(symptom_words)
                recommendations.append({
                    'name': med['name'],
                    'category': med['category'],
                    'safety_rating': med['safety_rating'],
                    'price_category': med['price_category'],
                    'key_info': med['key_info'],
                    'match_strength': strength
                })

        # Sort by safety + match strength
        recommendations.sort(key=lambda x: (x['safety_rating'], x['match_strength']), reverse=True)
        return recommendations  # FIXED: This was missing before!

    def add_medicine(self, medicine_data):
        """Add new medicine to database"""
        try:
            new_med = {
                'name': medicine_data['name'],
                'for_symptoms': medicine_data['for_symptoms'].lower(),
                'category': medicine_data['category'],
                'safety_rating': medicine_data['safety_rating'],
                'price_category': medicine_data.get('price_category', 'Standard'),
                'key_info': medicine_data.get('key_info', 'Consult doctor before use.')
            }
            new_row = pd.DataFrame([new_med])
            self.medicines_df = pd.concat([self.medicines_df, new_row], ignore_index=True)
            self.user_added_medicines.append(new_med)
            return True, "Medicine added successfully!"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def get_all_medicines(self):
        return self.medicines_df.to_dict('records')

    def get_total_medicines_count(self):
        return len(self.medicines_df)

    def get_user_added_medicines_count(self):
        return len(self.user_added_medicines)

    def search_medicine(self, name):
        results = self.medicines_df[self.medicines_df['name'].str.contains(name, case=False, na=False)]
        return results.to_dict('records')

# Quick test
if __name__ == "__main__":
    r = MedicineRecommender()
    print("Total medicines:", r.get_total_medicines_count())
    results = r.recommend_by_symptoms("fever headache")
    print("Found for 'fever headache':", len(results))
    if results:
        print("Top match:", results[0]['name'], "⭐", results[0]['safety_rating'])
    print("WEB-APP READY!")