my_set = {1,2,3,7,5,9,2,1}
print(my_set)
#Add
my_set.add(8)
print(my_set)
#Remove
my_set.remove(5)
print(my_set)
#Discard
my_set.discard(1)
print(my_set)
#Union
set2 = {1,5,7,9,10,12,11}
combined = my_set.union(set2)
print("combined = ",combined)
#Intersection
intersect = my_set.intersection(set2)
print(intersect)
#Difference
diff=my_set.difference(set2)
print(diff)