# ASSIGNMENT OPERATIONS
#   = equal
#   += add and
#   *= multipy and
#   -= subtract and
#   /= divide and
#   %= modulus and
#   **= exponent and
#   //= floor division

def assign1():
    x = 10
    return x

print("Returned value:", assign1())



def assign2(y):
    y += 3
    return y


print("Returned value:", assign2(4))

def assign3(z):
    z *= 2
    return z

print("Returned value:", assign3(7))



a = 21
b = 10 
c =0

c = a + b
print(c)

c += a
print(c)

c *= a
print(c)

c /= a
print(c)

c = 2
print(c)

c **= a
print(c)

c %= a
print(c)

c //= a
print(c)