# main.py - This runs your medicine recommendation system
from medicine_recommender import MedicineRecommender

def main():
    print("🩺 Welcome to MediMatch - Medicine Recommendation System!")
    print("=" * 50)
    
    # Create the recommender system
    recommender = MedicineRecommender()
    
    # Simple menu
    while True:
        print("\n📋 Main Menu:")
        print("1. 🔍 Get medicine recommendations by symptoms")
        print("2. 📊 View all available medicines")
        print("3. ❌ Exit the system")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            symptoms = input("Enter your symptoms (comma-separated): ").strip()
            if symptoms:
                print(f"\n💡 Searching for medicines for: {symptoms}")
                recommendations = recommender.recommend_by_symptoms(symptoms)
                
                if recommendations:
                    print(f"✅ Found {len(recommendations)} recommendation(s):")
                    for i, med in enumerate(recommendations, 1):
                        print(f"   {i}. 💊 {med['name']}")
                        print(f"      For: {med['for_symptoms']}")
                        print(f"      Type: {med['category']}")
                        print(f"      Safety: {med['safety_rating']}/5.0")
                else:
                    print("❌ No medicines found for these symptoms.")
            else:
                print("⚠️ Please enter valid symptoms.")
                
        elif choice == "2":
            print("\n📚 All Available Medicines:")
            all_meds = recommender.get_all_medicines()
            for i, med in enumerate(all_meds, 1):
                print(f"   {i}. {med['name']} - {med['category']}")
                
        elif choice == "3":
            print("👋 Thank you for using MediMatch! Stay healthy!")
            break
            
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    input("Press Enter to start the program...")
    main()
    input("Press Enter to exit the program...")
    