# In python, operator precedence determines the order in which operators are evaluated in an expression.
# Operators with higher precedence are evaluated first.
# Eg:
    # 1. Parentheses: `()`
    # 2. Exponentiation: `**`
    # 3. Unary plus and minus: `+x`, `-x`
    # 4. multipy, divide, floor divide, modulus: `*`, `/`, `//`,`%`
    # 5. Addition and subtract: `+`, `-`
    # 6. bitwise shifts: `<<`, `>>`
    # 7. bitwise and: `&` 
    # 8. bitwise xor: `^`
    # 9. bitwise or: `|` 
    # 10.comparison operators: `==`, `!=`, `>`, `<`, `>=`,`<=`,`in`,`not in`,`is`,`is not`
    # 11.boolean not: `not`
    # 12.boolean and: `and`
    # 13.boolean or: `or`
    
    
    
result = (10 + 5) *2 
print(result)

result1 = 2 ** 3 * 4
print(result1)

result2 = -3 * 4
print(result2)

result3 = 10 + 5 *2 
print(result3)

result4 = 2 + 3 < 5 * 2
print(result4)