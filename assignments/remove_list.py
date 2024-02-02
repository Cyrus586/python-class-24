# EXAMPLE 1
print()
fruits = ["Mango", "Apple", "Orange", "Banana"]
el_to_remove = "Banana"
print("original list:", fruits)
fruits.remove(el_to_remove)
print("list after removing", el_to_remove + ":", fruits)
print()

# EXAMPLE 2
numbers = [1,2,3,4,5,6]
index_to_remove = 3
print("original list:", numbers)
del numbers[index_to_remove]
print("list after removing element at index", index_to_remove, ":", numbers)