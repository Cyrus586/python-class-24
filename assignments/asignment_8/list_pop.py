# EXAMPLE 1
list1 = [1, 'Cyrus', 20.9, 190, True]
print(list1) # printed before poping

list1.pop()
print(list1) # removes one item from the end

# Example 2

list2 = [1, 'Cyrus', 20.9, 190, 'John']
print('Original List:', list2)

removed_element = list2.pop()
print("Modified list after pop(): ",list2)
print("Removed Element:", removed_element)