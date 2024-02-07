list1 = ["John", False, 20, 0.7, 9]
print(len(list1))# checking the length of a list

list1.remove(9) # removing a value from a list
print(len(list1))

# Concatenating lists
list2 = ["John", 20, 30]
new_list = list1 + list2
print(new_list)

# clear() removes everything from a list
list2.clear()
print(list2)


# count
count_items = new_list.count(20)
print(count_items)


# sort(only sort number)
unsort_items = [29,10,23,1,5,67]
unsort_items.sort()
print("These are the sorted items: ",unsort_items)

# reverse items
unsort_items.reverse()
print(unsort_items)

# copying
copy_item = unsort_items.copy()
print(copy_item)
