# packing a tuple
tuple1 = (1, False, "10")
print(tuple1)

# unpacking a tuple
a,b,c = tuple1
print("The assignrd to a :", a)

# tuple comparison
tuple2 = (1,2,4)
tuple3 = (1,2,3)
print(tuple2 == tuple3) # outputs a false

# deleting a tuple
tuple4 = (1,2,3,4,5)
del tuple4

tuple5 = ("John", False, 20, 0.7)
slice_tuple = tuple5[1:1:3]
print(slice_tuple)