dict1 = {"a":1, "b":2 }
dict2 = {"a":3, "b":4 }

dict2.update(dict1)
print(dict2)

# comparing a dictionary
dict1 = {"a":1, "b":2 }
dict2 = {"a":3, "b":4 }
print( dict1 == dict2)

#length of a dict
print(len(dict1))


# sorting items in dict
dict3 = {"a":1, "b":2, "c":3, }
sort_dict = dict(sorted(dict3.items()))
print(sort_dict)