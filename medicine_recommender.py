import pandas as pd

class MedicineRecommender:
    def __init__(self):
        self.medicines_df = self.create_medicine_data()
        self.user_added_medicines = []
        print("💊 Medicine database initialized successfully!")
    
    def create_medicine_data(self):
        """Create comprehensive medicine database"""
        data = {
            'name': [
                'Paracetamol 500mg', 'Ibuprofen 400mg', 'Aspirin 100mg',
                'Amoxicillin 250mg', 'Cetirizine 10mg', 'Omeprazole 20mg'
            ],
            'for_symptoms': [
                'fever headache mild pain', 'pain inflammation fever',
                'pain fever inflammation', 'bacterial infection',
                'allergy sneezing itching', 'heartburn acid reflux'
            ],
            'category': [
                'Analgesic', 'NSAID', 'NSAID', 'Antibiotic',
                'Antihistamine', 'PPI'
            ],
            'safety_rating': [4.5, 4.0, 4.1, 4.2, 4.3, 4.4],
            'price_category': [
                '💰 Economy', '💵 Standard', '💰 Economy',
                '💰 Economy', '💰 Economy', '💎 Premium'
            ],
            'key_info': [
                'First-line for mild-moderate pain. Max 4g/day. Avoid alcohol.',
                'Take with food. GI and kidney precautions. Anti-inflammatory.',
                'Low-dose for heart protection. GI bleeding risk. Not for children.',
                'Penicillin antibiotic. Complete full course. Check for allergies.',
                'Non-drowsy formula. Once daily. Few side effects.',
                'Proton pump inhibitor. Take before meals. Long-term use monitoring needed.'
            ]
        }
        return pd.DataFrame(data)
    
    def get_total_medicines_count(self):
        """Returns accurate total count of all medicines (base + user-added)"""
        try:
            return len(self.medicines_df) + len(self.user_added_medicines)
        except Exception as e:
            print(f"❌ Error counting total medicines: {str(e)}")
            return 0
    
    def get_user_added_medicines_count(self):
        """Returns count of only user-added medicines"""
        try:
            return len(self.user_added_medicines)
        except Exception as e:
            print(f"❌ Error counting user-added medicines: {str(e)}")
            return 0
    
    def add_medicine(self, medicine_data):
        """Add new medicine to database"""
        try:
            # Validate required fields
            required_fields = ['name', 'for_symptoms', 'category', 'safety_rating']
            for field in required_fields:
                if field not in medicine_data or not medicine_data[field]:
                    return False, f"❌ Missing required field: {field}"
            
            # Create complete record
            new_medicine = {
                'name': medicine_data['name'],
                'for_symptoms': medicine_data['for_symptoms'],
                'category': medicine_data['category'],
                'safety_rating': medicine_data['safety_rating'],
                'price_category': medicine_data.get('price_category', '💵 Standard'),
                'key_info': medicine_data.get('key_info', ''),
                'primary_use': medicine_data.get('primary_use', ''),
                'drug_class': medicine_data.get('drug_class', ''),
                'dosage_form': medicine_data.get('dosage_form', ''),
                'duration': medicine_data.get('duration', '')
            }
            
            # Add to both storage locations
            self.user_added_medicines.append(new_medicine)
            new_row = pd.DataFrame([new_medicine])
            self.medicines_df = pd.concat([self.medicines_df, new_row], ignore_index=True)
            
            return True, "✅ Medicine added successfully!"
        except Exception as e:
            return False, f"❌ Error adding medicine: {str(e)}"
    
    def get_all_medicines(self):
        """Get all medicines as dictionary records"""
        try:
            base_medicines = self.medicines_df.to_dict('records')
            return base_medicines + self.user_added_medicines
        except Exception as e:
            print(f"❌ Error getting medicines: {str(e)}")
            return []
    
    def search_medicine(self, medicine_name):
        """Search medicines by name"""
        try:
            all_meds = self.get_all_medicines()
            return [med for med in all_meds if medicine_name.lower() in med['name'].lower()]
        except Exception as e:
            print(f"❌ Error searching medicines: {str(e)}")
            return []
    
    def recommend_by_symptoms(self, symptoms):
        """Recommend medicines based on symptom matching"""
        try:
            recommendations = []
            symptoms_lower = symptoms.lower()
            
            for medicine in self.get_all_medicines():
                medicine_symptoms = medicine['for_symptoms'].lower()
                
                # Check if any symptom word matches
                symptom_words = [word.strip() for word in symptoms_lower.split(',')]
                match_found = any(symptom in medicine_symptoms for symptom in symptom_words if symptom)
                
                if match_found:
                    recommendations.append({
                        'name': medicine['name'],
                        'for_symptoms': medicine['for_symptoms'],
                        'category': medicine['category'],
                        'safety_rating': medicine['safety_rating'],
                        'price_category': medicine['price_category'],
                        'key_info': medicine['key_info'],
                        'match_strength': self.calculate_match_strength(symptom_words, medicine_symptoms)
                    })
            
            # Sort by safety rating and match strength
            recommendations.sort(key=lambda x: (x['safety_rating'], x.get('match_strength', 0)), reverse=True)
            return recommendations
        except Exception as e:
            print(f"❌ Error recommending by symptoms: {str(e)}")
            return []
    
    def calculate_match_strength(self, user_symptoms, medicine_symptoms):
        """Calculate how well the medicine matches symptoms"""
        matches = 0
        for symptom in user_symptoms:
            if symptom and symptom in medicine_symptoms:
                matches += 1
        return matches / len(user_symptoms) if user_symptoms else 0
    
    def get_statistics(self):
        """Get comprehensive database statistics"""
        try:
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
        except Exception as e:
            print(f"❌ Error calculating statistics: {str(e)}")
            return {}
