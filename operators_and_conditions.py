# Operators & Conditions
# 01.Identity Operators
# Example:

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (values are equal)
print(a is b)  # False (different objects in memory)
print(a is c)  # True (both 'a' and 'c' refer to the same object)

# Membership operator
# 02. in operator
# Example No.01
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False
# Example No.02
my_string = "Hello World"
print("World" in my_string)  # Output: True
print("Python" in my_string) # Output: False
    
# 03. Not in operator
# Example No.01
my_tuple = (10, 20, 30)
print(15 not in my_tuple) # Output: True
print(20 not in my_tuple) # Output: False
# Example No.02
my_dict = {"a": 1, "b": 2}
print("c" not in my_dict) # Output: True (checks for key existence)
print("a" not in my_dict) # Output: False

# Bitwise operators
# AND operator(&)
# Example No.01

result = a & b
print(result)  # 1 -> binary: 0001

# OR operator(|)
result = a | b
print(result)  # 7 -> binary: 0111

# XOR operator(^)
# Example No.01
result = a ^ b
print(result)  # 6 -> binary: 0110

# Not operator(~) 
result = ~a
print(result)  # -6 -> binary: ...11111010 (2's complement)

# Left Shift operator(<<)
result = a << 1
print(result)  # 10 -> binary: 1010

# Right Shift operator(>>)
result = a >> 1
print(result)  # 2 -> binary: 0010


