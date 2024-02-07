pychos = [1,2,3,4,5,6,7]
squared_pychos = [] # empty list to get values
for pycho in pychos:
    squared_pychos.append(pycho ** 2)
    
print("Squared pychos without list comprehension", squared_pychos)
squared_pychos_lc = [pycho ** 2 for pycho in pychos ]
print("Squared pychos with list comprehension", squared_pychos_lc) 