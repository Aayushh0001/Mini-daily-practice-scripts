student={
"name":"aayush",
"Age":20,
"language":"python"}

print(student.get("name"))

#Adding a new key
student["college"]="NCIT"

student.pop("Age") #Removes key

#Looping through keys and values
for key,value in student.items():
 print(key,"->",value)

