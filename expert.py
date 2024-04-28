def select_diseases(symptoms):
    diseases = {"Allergies": ['sneezing', 'blocked nose', 'watery eyes', 'red eyes', 'coughing', 'red rash']}
    matching_diseases = [disease for disease, disease_symptoms in diseases.items() if any(symptom.lower() in disease_symptoms for symptom in symptoms)]
    return matching_diseases

symptoms_input = input("Enter your symptoms (separated by commas): ").lower().split(',')
symptoms = [symptom.strip() for symptom in symptoms_input if symptom.strip()]
diagnosed_diseases = select_diseases(symptoms)

if diagnosed_diseases:
    print("You may have the following disease(s):")
    print('\n'.join("- " + disease for disease in diagnosed_diseases))
else:
    print("Unable to diagnose any disease based on the given symptoms.")
