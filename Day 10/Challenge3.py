# Create a list of dictionaries and each contains a student with name age and grade
# Add 3 student
# update grade of 1 student
# Remove a student
# Loop through the list and print each students details

Students=[
    {"Name":"Aayush","Age":20,"Grade":"A"},
    {"Name":"Soumyika","Age":21,"Grade":"A"},
    {"Name":"Pratik","Age":31,"Grade":"B"}
]


Students.append({"Name":"Vins","Age":21,"Grade":"B"})
Students.append({"Name":"Ram","Age":51,"Grade":"D"})
Students.append({"Name":"Shyam","Age":23,"Grade":"C"})

Students[2]["Grade"]="C"

Students.pop(0)

for student in Students:
 print("Name:",student["Name"])
 print("Age:",student["Age"])
 print("Grade:",student["Grade"])
 print("---------------")