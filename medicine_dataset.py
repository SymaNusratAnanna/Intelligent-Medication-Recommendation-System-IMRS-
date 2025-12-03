# # medicine_dataset.py - COMPLETE DATASET WITH 49 MEDICINES
# import pandas as pd
# import random

# class MedicineDataset:
#     def __init__(self):
#         self.medicines = self.create_comprehensive_medicine_data()
    
#     def create_comprehensive_medicine_data(self):
#         """Create complete dataset with 49 medicines matching your image"""
#         return [
#             # ANALGESICS & PAIN RELIEVERS (8 medicines)
#             {
#                 "name": "Paracetamol 500mg",
#                 "category": "Analgesic",
#                 "safety_rating": 4.5,
#                 "for_symptoms": "fever, headache, mild to moderate pain",
#                 "price_category": "💰 Economy",
#                 "key_info": "First-line for mild-moderate pain. Max 4g/day."
#             },
#             {
#                 "name": "Ibuprofen 400mg",
#                 "category": "NSAID",
#                 "safety_rating": 4.0,
#                 "for_symptoms": "pain, inflammation, fever, arthritis",
#                 "price_category": "💵 Standard",
#                 "key_info": "Take with food. GI and kidney precautions."
#             },
#             {
#                 "name": "Aspirin 100mg",
#                 "category": "Anti-platelet",
#                 "safety_rating": 3.8,
#                 "for_symptoms": "pain, fever, cardiovascular protection",
#                 "price_category": "💰 Economy",
#                 "key_info": "Low-dose for heart protection. GI bleeding risk."
#             },
#             {
#                 "name": "Naproxen 250mg",
#                 "category": "NSAID",
#                 "safety_rating": 3.9,
#                 "for_symptoms": "arthritis, pain, inflammation, menstrual cramps",
#                 "price_category": "💵 Standard",
#                 "key_info": "Longer acting. Take with food."
#             },
#             {
#                 "name": "Diclofenac 50mg",
#                 "category": "NSAID",
#                 "safety_rating": 3.7,
#                 "for_symptoms": "arthritis, acute pain, inflammation",
#                 "price_category": "💵 Standard",
#                 "key_info": "Powerful NSAID. Monitor liver and kidney function."
#             },
#             {
#                 "name": "Tramadol 50mg",
#                 "category": "Opioid",
#                 "safety_rating": 3.2,
#                 "for_symptoms": "moderate to severe pain",
#                 "price_category": "💎 Premium",
#                 "key_info": "Opioid analgesic. Risk of dependence. Schedule IV."
#             },
#             {
#                 "name": "Codeine 30mg",
#                 "category": "Opioid",
#                 "safety_rating": 3.0,
#                 "for_symptoms": "mild to moderate pain, cough",
#                 "price_category": "💎 Premium",
#                 "key_info": "Opioid with cough suppression. Monitor for dependence."
#             },
#             {
#                 "name": "Celecoxib 200mg",
#                 "category": "NSAID",
#                 "safety_rating": 3.9,
#                 "for_symptoms": "osteoarthritis, rheumatoid arthritis, pain",
#                 "price_category": "💎 Premium",
#                 "key_info": "COX-2 selective. Lower GI risk than traditional NSAIDs."
#             },

#             # ANTIBIOTICS (10 medicines)
#             {
#                 "name": "Amoxicillin 250mg",
#                 "category": "Antibiotic",
#                 "safety_rating": 4.2,
#                 "for_symptoms": "bacterial infections, respiratory infections, UTI",
#                 "price_category": "💰 Economy",
#                 "key_info": "Penicillin antibiotic. Complete full course."
#             },
#             {
#                 "name": "Azithromycin 250mg",
#                 "category": "Antibiotic",
#                 "safety_rating": 4.1,
#                 "for_symptoms": "respiratory infections, STIs, skin infections",
#                 "price_category": "💵 Standard",
#                 "key_info": "Macrolide antibiotic. Once daily dosing."
#             },
#             {
#                 "name": "Ciprofloxacin 500mg",
#                 "category": "Antibiotic",
#                 "safety_rating": 3.8,
#                 "for_symptoms": "UTI, respiratory infections, abdominal infections",
#                 "price_category": "💵 Standard",
#                 "key_info": "Fluoroquinolone. Tendon rupture risk. Avoid in children."
#             },
#             {
#                 "name": "Doxycycline 100mg",
#                 "category": "Antibiotic",
#                 "safety_rating": 4.0,
#                 "for_symptoms": "acne, respiratory infections, malaria prophylaxis",
#                 "price_category": "💰 Economy",
#                 "key_info": "Tetracycline. Take with plenty of water. Photosensitivity risk."
#             },
#             {
#                 "name": "Clarithromycin 500mg",
#                 "category": "Antibiotic",
#                 "safety_rating": 3.9,
#                 "for_symptoms": "respiratory infections, H. pylori eradication",
#                 "price_category": "💵 Standard",
#                 "key_info": "Macrolide. Multiple drug interactions. Monitor ECG."
#             },
#             {
#                 "name": "Metronidazole 400mg",
#                 "category": "Antibiotic",
#                 "safety_rating": 3.7,
#                 "for_symptoms": "anaerobic infections, parasitic infections, dental",
#                 "price_category": "💰 Economy",
#                 "key_info": "Nitroimidazole. Avoid alcohol. Metallic taste side effect."
#             },
#             {
#                 "name": "Cephalexin 500mg",
#                 "category": "Antibiotic",
#                 "safety_rating": 4.1,
#                 "for_symptoms": "skin infections, UTI, respiratory infections",
#                 "price_category": "💰 Economy",
#                 "key_info": "First-generation cephalosporin. Penicillin cross-sensitivity."
#             },
#             {
#                 "name": "Levofloxacin 500mg",
#                 "category": "Antibiotic",
#                 "safety_rating": 3.6,
#                 "for_symptoms": "pneumonia, UTI, skin infections",
#                 "price_category": "💎 Premium",
#                 "key_info": "Fluoroquinolone. Reserve for resistant infections."
#             },
#             {
#                 "name": "Co-amoxiclav 625mg",
#                 "category": "Antibiotic",
#                 "safety_rating": 4.0,
#                 "for_symptoms": "resistant infections, animal bites, dental",
#                 "price_category": "💵 Standard",
#                 "key_info": "Amoxicillin + clavulanate. Broad spectrum. Higher diarrhea risk."
#             },
#             {
#                 "name": "Trimethoprim 200mg",
#                 "category": "Antibiotic",
#                 "safety_rating": 3.9,
#                 "for_symptoms": "UTI, respiratory infections",
#                 "price_category": "💰 Economy",
#                 "key_info": "Folate inhibitor. Avoid in pregnancy and folate deficiency."
#             },

#             # CARDIOVASCULAR (8 medicines)
#             {
#                 "name": "Atorvastatin 10mg",
#                 "category": "Statin",
#                 "safety_rating": 4.1,
#                 "for_symptoms": "high cholesterol, cardiovascular risk",
#                 "price_category": "💎 Premium",
#                 "key_info": "HMG-CoA reductase inhibitor. Take in evening."
#             },
#             {
#                 "name": "Lisinopril 10mg",
#                 "category": "ACE Inhibitor",
#                 "safety_rating": 4.0,
#                 "for_symptoms": "hypertension, heart failure, post-MI",
#                 "price_category": "💰 Economy",
#                 "key_info": "ACE inhibitor. Monitor for cough and angioedema."
#             },
#             {
#                 "name": "Amlodipine 5mg",
#                 "category": "Calcium Blocker",
#                 "safety_rating": 4.2,
#                 "for_symptoms": "hypertension, angina",
#                 "price_category": "💵 Standard",
#                 "key_info": "Dihydropyridine CCB. Ankle swelling side effect."
#             },
#             {
#                 "name": "Metoprolol 50mg",
#                 "category": "Beta Blocker",
#                 "safety_rating": 4.0,
#                 "for_symptoms": "hypertension, angina, heart failure, arrhythmia",
#                 "price_category": "💰 Economy",
#                 "key_info": "Beta-1 selective. Taper gradually. Avoid in asthma."
#             },
#             {
#                 "name": "Losartan 50mg",
#                 "category": "ARB",
#                 "safety_rating": 4.3,
#                 "for_symptoms": "hypertension, diabetic nephropathy",
#                 "price_category": "💵 Standard",
#                 "key_info": "Angiotensin receptor blocker. Less cough than ACEi."
#             },
#             {
#                 "name": "Hydrochlorothiazide 25mg",
#                 "category": "Diuretic",
#                 "safety_rating": 3.8,
#                 "for_symptoms": "hypertension, edema",
#                 "price_category": "💰 Economy",
#                 "key_info": "Thiazide diuretic. Monitor electrolytes. Photosensitivity."
#             },
#             {
#                 "name": "Clopidogrel 75mg",
#                 "category": "Anti-platelet",
#                 "safety_rating": 4.0,
#                 "for_symptoms": "post-stent, stroke prevention, ACS",
#                 "price_category": "💎 Premium",
#                 "key_info": "P2Y12 inhibitor. Bleeding risk. Check CYP2C19 status."
#             },
#             {
#                 "name": "Warfarin 5mg",
#                 "category": "Anticoagulant",
#                 "safety_rating": 2.8,
#                 "for_symptoms": "atrial fibrillation, DVT/PE, mechanical valves",
#                 "price_category": "💰 Economy",
#                 "key_info": "Vitamin K antagonist. Regular INR monitoring required."
#             },

#             # GASTROINTESTINAL (6 medicines)
#             {
#                 "name": "Omeprazole 20mg",
#                 "category": "PPI",
#                 "safety_rating": 4.4,
#                 "for_symptoms": "GERD, ulcers, acid reflux",
#                 "price_category": "💎 Premium",
#                 "key_info": "Proton pump inhibitor. Take before meals."
#             },
#             {
#                 "name": "Pantoprazole 40mg",
#                 "category": "PPI",
#                 "safety_rating": 4.3,
#                 "for_symptoms": "GERD, erosive esophagitis, ZE syndrome",
#                 "price_category": "💎 Premium",
#                 "key_info": "PPI with fewer interactions. IV formulation available."
#             },
#             {
#                 "name": "Ranitidine 150mg",
#                 "category": "H2 Blocker",
#                 "safety_rating": 4.1,
#                 "for_symptoms": "ulcers, GERD, acid indigestion",
#                 "price_category": "💰 Economy",
#                 "key_info": "H2 receptor antagonist. Being phased out due to NDMA concerns."
#             },
#             {
#                 "name": "Domperidone 10mg",
#                 "category": "Anti-emetic",
#                 "safety_rating": 3.5,
#                 "for_symptoms": "nausea, vomiting, gastroparesis",
#                 "price_category": "💵 Standard",
#                 "key_info": "Dopamine antagonist. QT prolongation risk. Lactation use."
#             },
#             {
#                 "name": "Loperamide 2mg",
#                 "category": "Anti-diarrheal",
#                 "safety_rating": 3.9,
#                 "for_symptoms": "diarrhea, traveler's diarrhea",
#                 "price_category": "💰 Economy",
#                 "key_info": "Opioid receptor agonist in gut. Not for infectious diarrhea."
#             },
#             {
#                 "name": "Mesalazine 400mg",
#                 "category": "5-ASA",
#                 "safety_rating": 4.0,
#                 "for_symptoms": "ulcerative colitis, Crohn's disease",
#                 "price_category": "💎 Premium",
#                 "key_info": "Aminosalicylate. Monitor renal function with long-term use."
#             },

#             # NEUROLOGICAL & PSYCHIATRIC (7 medicines)
#             {
#                 "name": "Sertraline 50mg",
#                 "category": "SSRI",
#                 "safety_rating": 3.9,
#                 "for_symptoms": "depression, anxiety, OCD, PTSD",
#                 "price_category": "💵 Standard",
#                 "key_info": "SSRI antidepressant. Takes 4-6 weeks for full effect."
#             },
#             {
#                 "name": "Amitriptyline 25mg",
#                 "category": "TCA",
#                 "safety_rating": 3.4,
#                 "for_symptoms": "depression, neuropathic pain, migraine",
#                 "price_category": "💰 Economy",
#                 "key_info": "Tricyclic antidepressant. Sedating. Overdose risk."
#             },
#             {
#                 "name": "Diazepam 5mg",
#                 "category": "Benzodiazepine",
#                 "safety_rating": 2.5,
#                 "for_symptoms": "anxiety, seizures, muscle spasm, alcohol withdrawal",
#                 "price_category": "💵 Standard",
#                 "key_info": "Benzodiazepine. High addiction potential. Short-term use only."
#             },
#             {
#                 "name": "Carbamazepine 200mg",
#                 "category": "Anticonvulsant",
#                 "safety_rating": 3.6,
#                 "for_symptoms": "epilepsy, trigeminal neuralgia, bipolar",
#                 "price_category": "💵 Standard",
#                 "key_info": "Enzyme inducer. Monitor levels. HLA-B*1502 screening in Asians."
#             },
#             {
#                 "name": "Gabapentin 300mg",
#                 "category": "Anticonvulsant",
#                 "safety_rating": 3.8,
#                 "for_symptoms": "neuropathic pain, epilepsy, restless legs",
#                 "price_category": "💵 Standard",
#                 "key_info": "Renal excretion. Titrate slowly. Abuse potential."
#             },
#             {
#                 "name": "Sumatriptan 50mg",
#                 "category": "Triptan",
#                 "safety_rating": 3.7,
#                 "for_symptoms": "migraine, cluster headaches",
#                 "price_category": "💎 Premium",
#                 "key_info": "5-HT1 agonist. Not for hemiplegic or basilar migraine."
#             },
#             {
#                 "name": "Pregabalin 75mg",
#                 "category": "Anticonvulsant",
#                 "safety_rating": 3.5,
#                 "for_symptoms": "neuropathic pain, anxiety, epilepsy",
#                 "price_category": "💎 Premium",
#                 "key_info": "Schedule V controlled substance. Abuse and dependence risk."
#             },

#             # RESPIRATORY & ALLERGY (5 medicines)
#             {
#                 "name": "Salbutamol Inhaler",
#                 "category": "Bronchodilator",
#                 "safety_rating": 4.0,
#                 "for_symptoms": "asthma, COPD, bronchospasm",
#                 "price_category": "💰 Economy",
#                 "key_info": "Short-acting beta-agonist. Rescue medication only."
#             },
#             {
#                 "name": "Fluticasone Inhaler",
#                 "category": "Corticosteroid",
#                 "safety_rating": 4.2,
#                 "for_symptoms": "asthma, allergic rhinitis, COPD",
#                 "price_category": "💎 Premium",
#                 "key_info": "Inhaled corticosteroid. Rinse mouth after use to prevent thrush."
#             },
#             {
#                 "name": "Montelukast 10mg",
#                 "category": "Leukotriene",
#                 "safety_rating": 3.9,
#                 "for_symptoms": "asthma, allergic rhinitis, exercise-induced asthma",
#                 "price_category": "💵 Standard",
#                 "key_info": "Leukotriene receptor antagonist. Take in evening. Neuropsychiatric monitoring."
#             },
#             {
#                 "name": "Cetirizine 10mg",
#                 "category": "Antihistamine",
#                 "safety_rating": 4.3,
#                 "for_symptoms": "allergies, urticaria, hay fever",
#                 "price_category": "💰 Economy",
#                 "key_info": "Second-generation antihistamine. Non-drowsy. Once daily."
#             },
#             {
#                 "name": "Loratadine 10mg",
#                 "category": "Antihistamine",
#                 "safety_rating": 4.4,
#                 "for_symptoms": "allergies, allergic rhinitis, urticaria",
#                 "price_category": "💰 Economy",
#                 "key_info": "Non-sedating antihistamine. Fewer drug interactions."
#             },

#             # DIABETES & ENDOCRINE (5 medicines)
#             {
#                 "name": "Metformin 500mg",
#                 "category": "Biguanide",
#                 "safety_rating": 4.2,
#                 "for_symptoms": "type 2 diabetes, insulin resistance, PCOS",
#                 "price_category": "💰 Economy",
#                 "key_info": "First-line for type 2 diabetes. GI side effects common."
#             },
#             {
#                 "name": "Gliclazide 80mg",
#                 "category": "Sulfonylurea",
#                 "safety_rating": 3.6,
#                 "for_symptoms": "type 2 diabetes",
#                 "price_category": "💰 Economy",
#                 "key_info": "Insulin secretagogue. Hypoglycemia risk. Take with food."
#             },
#             {
#                 "name": "Insulin Glargine",
#                 "category": "Insulin",
#                 "safety_rating": 3.8,
#                 "for_symptoms": "type 1 and 2 diabetes",
#                 "price_category": "💎 Premium",
#                 "key_info": "Long-acting basal insulin. Once daily. Hypoglycemia risk."
#             },
#             {
#                 "name": "Levothyroxine 50mcg",
#                 "category": "Thyroid",
#                 "safety_rating": 4.5,
#                 "for_symptoms": "hypothyroidism, thyroid replacement",
#                 "price_category": "💰 Economy",
#                 "key_info": "Thyroid hormone replacement. Take on empty stomach. Avoid calcium/iron within 4 hours."
#             },
#             {
#                 "name": "Sitagliptin 100mg",
#                 "category": "DPP-4 Inhibitor",
#                 "safety_rating": 4.1,
#                 "for_symptoms": "type 2 diabetes",
#                 "price_category": "💎 Premium",
#                 "key_info": "Gliptin class. Weight neutral. Low hypoglycemia risk."
#             }
#         ]
    
#     def get_all_medicines(self):
#         """Get all 49 medicines"""
#         return self.medicines
    
#     def get_medicine_by_name(self, name):
#         """Get specific medicine by name"""
#         for medicine in self.medicines:
#             if medicine['name'].lower() == name.lower():
#                 return medicine
#         return None
    
#     def get_medicines_by_category(self, category):
#         """Get medicines by category"""
#         return [med for med in self.medicines if med['category'].lower() == category.lower()]
    
#     def get_medicines_by_symptoms(self, symptoms):
#         """AI-powered symptom matching"""
#         symptoms_lower = symptoms.lower()
#         matches = []
        
#         for medicine in self.medicines:
#             medicine_symptoms = medicine['for_symptoms'].lower()
#             # Simple keyword matching (can be enhanced with ML)
#             if any(symptom in medicine_symptoms for symptom in symptoms_lower.split()):
#                 matches.append(medicine)
        
#         # Sort by safety rating (highest first)
#         matches.sort(key=lambda x: x['safety_rating'], reverse=True)
#         return matches
    
#     def get_statistics(self):
#         """Get dataset statistics"""
#         df = pd.DataFrame(self.medicines)
#         stats = {
#             'total_medicines': len(self.medicines),
#             'categories': df['category'].nunique(),
#             'avg_safety': df['safety_rating'].mean(),
#             'price_distribution': df['price_category'].value_counts().to_dict()
#         }
#         return stats
    
#     def to_dataframe(self):
#         """Convert to pandas DataFrame for analysis"""
#         return pd.DataFrame(self.medicines)

# # Usage example
# if __name__ == "__main__":
#     dataset = MedicineDataset()
    
#     print("=== MEDICINE DATASET STATISTICS ===")
#     stats = dataset.get_statistics()
#     print(f"Total Medicines: {stats['total_medicines']}")
#     print(f"Categories: {stats['categories']}")
#     print(f"Average Safety Rating: {stats['avg_safety']:.2f}/5.0")
#     print(f"Price Distribution: {stats['price_distribution']}")
    
#     # Test symptom search
#     print("\n=== TESTING SYMPTOM SEARCH ===")
#     fever_meds = dataset.get_medicines_by_symptoms("fever")
#     print(f"Medicines for fever: {len(fever_meds)} found")
#     for med in fever_meds[:3]:  # Show first 3
#         print(f"  - {med['name']} (Safety: {med['safety_rating']}/5.0)")