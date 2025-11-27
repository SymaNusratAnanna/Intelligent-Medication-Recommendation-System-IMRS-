# medicine_recommender.py - The brain of your system
import pandas as pd

class MedicineRecommender:
    def __init__(self):
        self.medicines_df = self.create_medicine_data()
        print("💊 Medicine database loaded successfully!")
    
    def create_medicine_data(self):
        """Create our medicine database"""
        data = {
            'name': [
                'Paracetamol 500mg', 'Ibuprofen 400mg', 'Amoxicillin 250mg',
                'Cetirizine 10mg', 'Omeprazole 20mg', 'Aspirin 100mg'
            ],
            'for_symptoms': [
                'fever, headache, mild pain',
                'pain, inflammation, fever', 
                'bacterial infections, fever',
                'allergies, sneezing, itching',
                'acid reflux, heartburn, ulcers',
                'pain, fever, inflammation, heart protection'
            ],
            'category': ['Analgesic', 'NSAID', 'Antibiotic', 'Antihistamine', 'PPI', 'NSAID'],
            'safety_rating': [4.5, 4.0, 4.2, 4.3, 4.4, 4.1]
        }
        return pd.DataFrame(data)
    
    def recommend_by_symptoms(self, user_symptoms):
        """Recommend medicines based on symptoms"""
        recommendations = []
        
        for _, medicine in self.medicines_df.iterrows():
            # Convert symptoms to lowercase for case-insensitive matching
            medicine_symptoms = medicine['for_symptoms'].lower()
            user_symptoms_lower = user_symptoms.lower()
            
            # Check if any user symptom matches medicine symptoms
            match_found = any(
                symptom.strip() in medicine_symptoms 
                for symptom in user_symptoms_lower.split(',')
            )
            
            if match_found:
                recommendations.append({
                    'name': medicine['name'],
                    'for_symptoms': medicine['for_symptoms'],
                    'category': medicine['category'],
                    'safety_rating': medicine['safety_rating']
                })
        
        return recommendations
    
    def get_all_medicines(self):
        """Return all medicines in the system"""
        return self.medicines_df.to_dict('records')
    
    def search_medicine(self, medicine_name):
        """Search for a specific medicine"""
        results = self.medicines_df[
            self.medicines_df['name'].str.contains(medicine_name, case=False)
        ]
        return results.to_dict('records')

# Test the class
if __name__ == "__main__":
    # Quick test
    recommender = MedicineRecommender()
    print("🧪 Testing the system...")
    test_results = recommender.recommend_by_symptoms("fever")
    print(f"Test results: {len(test_results)} medicines found for 'fever'")