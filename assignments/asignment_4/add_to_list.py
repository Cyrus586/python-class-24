# APPENDING ADDING TO LIST EXAMPLES IN PYTHON

# EXAMPLE 1
print()
emp_list = []
newElement = "Student"
emp_list.append(newElement)
print("Empty list after adding", newElement + ":", emp_list)
print()

# EXAMPLE 2

contra = ["a","b","c"]
contra.append("d")
print("Contra after appending", contra)
print()



# INSERTING EXAMPLES IN PYTHN


# EXAMPLE 3
fruits = ["Mango", "Apple", "Orange", "Banana"]
New_Fruits = "Berries"
indexInsert = 1
fruits.insert(indexInsert, New_Fruits)
print("Fruits list after inserting", New_Fruits, "at index", indexInsert, ":", fruits)
print()

# EXAMPLE 4
veg = ["carrot", "Broccoli"]
newElement2 = "Spinach"
veg = veg + [newElement2]
print("Veg list after adding", newElement2, ":", veg)
print()

# EXAMPLE 5
study = ["Roger", "3.14", True, 20, 17.27]
print("Original study ", study)
study.insert(1, "Markson")
print("Study after appending: ", study)
study.insert(-1, "Pass")
print("List after appending: ", study)
print()