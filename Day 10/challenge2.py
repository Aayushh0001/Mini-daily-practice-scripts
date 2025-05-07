Dictonary={
    "Aayush":20,
    "Soumyika":21,
    "Pratik":22    
}

Dictonary["Soumyika"]=22

#Dictonary.update({"Soumyika":22})  (ALTERNATE)

Dictonary.pop("Pratik")

for key,value in Dictonary.items():
    print(key,"->",value)