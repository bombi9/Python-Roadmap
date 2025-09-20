# Variables:
conditionalSymptoms = [
    ("fever", ["Flu", "Infection", "Viral Fever"]),
    ("headache", ["Migraine", "Tension Headache", "Dehydration"]),
    ("cough", ["Cold", "Allergies", "Bronchitis"]),
    ("stuffy nose", ["Common Cold", "Sinusitis"]),
    ("rash", ["Allergy", "Measles", "Eczema"]),
    ("sore throat", ["Strep Throat", "Common Cold"]),
    ("fatigue", ["Flu", "Anemia", "Chronic Fatigue Syndrome"])
]
question = "Enter the symptoms that you have separated by comma or white space: "
Diagonisis = ""

answer = input(question)
for word in answer.replace(",", " ").split():

    for condition, symptom in conditionalSymptoms:
        if word.title() in symptom:
            Diagonisis +=  f"{condition} " if not(Diagonisis) else f"or {condition} "


print(Diagonisis)