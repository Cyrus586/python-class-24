# LOGICAL OPERATIONS
#   and logical AND
#   or logical OR
#   not logical NOT

print(True and True)
print(True and False)
print(True or False)
print(not False)


num1 = [1,2,3,4,5]
num2 = [4,5,6,7,8]
log_op_num = [n1 for n1 in num1 for n2 in num2 if n1 == n2]
print("\nExample 1: Selecting elements from two lists using AND operators")
print("List 1:", num1)
print("List 2:", num2)
print("Logical operation numbers", log_op_num)


box = 20
brush = 70
list1 = [1,2,3,5]

if(box in list1):
    print("line 1 - box is available in the given list")
else:
    print("line 1 - box is not available in the given list")