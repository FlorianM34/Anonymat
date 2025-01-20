import random
import pandas as pd #pip install pandas


# Define possible names
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez","Dough",
            "Valjean","Dupont","Lefevre","Leroy","Leroux","Bonaparte","Bros","Jameson","Bourbon","Trump","Gates","Musk","Jobs"]
first_names = ["James", "Mary", "Robert", "Patricia", "John", 
            "Jennifer", "Michael", "Linda", "David", "Elizabeth","Nicolas","Florian",
            "Dorian","Josselin","Kylian","Pio","Napoleon","Rayman","Mario","Luigi","Lebron","Kevin","Ricardo","Donald","Elon","Steve"]

# Generate unique name combinations
unique_names = list(set((ln, fn) for ln in last_names for fn in first_names))

# repeat if necessary
required_rows = 10000
if len(unique_names) < required_rows:
    unique_names *= (required_rows // len(unique_names)) + 1

students_data_unique = []
year = "2024-2025"

for i in range(required_rows):
    last_name, first_name = unique_names[i]
    student_code = f"{random.randint(2221000, 2221999)}"
    course_code = f"HAI{random.randint(100, 999)}"
    grade = round(random.uniform(10, 20), 1)
    students_data_unique.append([last_name, first_name, student_code, course_code, year, grade])

# Create DataFrame and save to CSV
df_unique = pd.DataFrame(students_data_unique, columns=["Nom", "Prenom", "CodeEtudiant", "CodeUE", "Annee", "Note"])
df_unique.to_csv("CSV_Notes_Data.csv", index=False)

print("created successfully.")
