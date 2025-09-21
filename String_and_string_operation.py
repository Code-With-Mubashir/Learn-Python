# String
# Example No.01
name = "Mubashir"
print(name)

print(name[0])  # First character
print(name[-1]) # Last character

# Example No.02
greeting = "Hello, " + name
print(greeting)
print(greeting * 3)  # Repeat the string 3 times
print(len(greeting))  # Length of the string
print(name[1:4])    # Substring from index 1 to 3
print(name.lower())  # Convert to lowercase
print(name.upper())  # Convert to uppercase

# Example No.03
multiline_string = """This is a
multiline
string."""
print(multiline_string)
print(multiline_string.split())  # Split the string into a list of words
print(multiline_string.replace("multiline", "single line"))  # Replace substring
print("line" in multiline_string)  # Check if substring exists
print(multiline_string.find("is"))  # Find the index of substring
print(multiline_string.strip())  # Remove leading/trailing whitespace
print(multiline_string.startswith("This"))  # Check if string starts with a substring
print(multiline_string.endswith("string."))  # Check if string ends with a substring
print(multiline_string.count("line"))  # Count occurrences of a substring
print(multiline_string.index("a"))  # Find the index of a substring (raises error if not found)
print(multiline_string.isalpha())  # Check if all characters are alphabetic
print(multiline_string.isdigit())  # Check if all characters are digits
print(multiline_string.isalnum())  # Check if all characters are alphanumeric
print(multiline_string.isspace())  # Check if all characters are whitespace
print(multiline_string.title())  # Convert to title case
print(multiline_string.capitalize())  # Capitalize the first character
print(multiline_string.center(50))  # Center the string within a specified width
print(multiline_string.zfill(50))  # Pad the string with zeros on the left
print(multiline_string.swapcase())  # Swap case of each character
print(multiline_string.encode())  # Encode the string to bytes
print(multiline_string.partition("is"))  # Partition the string at the first occurrence of a substring

# Example No.04
# Formatted String
formatted_string = f"Hello, {name}. Welcome to Python programming."
print(formatted_string)
print("Hello, {}. Welcome to Python programming.".format(name))
print("Hello, {0}. Welcome to Python programming.".format(name))
print("Hello, {name}. Welcome to Python programming.".format(name=name))


# Example No.05
# Escape Characters
escape_string = "He said, \"Hello!\"\nWelcome to Python programming.\tEnjoy your stay."
print(escape_string)
print(r"He said, \"Hello!\"\nWelcome to Python programming.\tEnjoy your stay.")  # Raw string
print("C:\\Users\\Mubashir")  # Escaping backslash
print("First Line\rSecond Line")  # Carriage return
print("Column1\tColumn2\tColumn3")  # Tab space
print("This is a backslash: \\")  # Backslash
print("This is a single quote: \'")  # Single quote
print("This is a double quote: \"")  # Double quote
print("This is a bell sound: \a")  # Bell/alert
print("This is a form feed: \f")  # Form feed
print("This is a vertical tab: \v")  # Vertical tab
print("This is a unicode character: \u03A9")  # Unicode character (Omega symbol)
print("This is a hexadecimal character: \x48")  # Hexadecimal character (H)
print("This is a octal character: \101")  # Octal character (A)
print("This is a backspace: ABC\bD")  # Backspace
print("This is a new line: Line1\nLine2")  # New line



# String_Operations
# 1. Concatenation operator

# Example No.01
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World

# Example No.02
first_name = "Mubashir"
last_name = "Rasool"
full_name = first_name + " " + last_name
print(full_name)  # Output: Mubashir Rasool

# 2. Repetition operator
# Example No.01
s = "Hi"
result = s * 3
print(result)

# Example No.02
name = "Mubashir"
result = name * 12
print(result)

# Example No.03

Book_name = "Movies_subscription"
result = Book_name * 5
print(result)


# 3.Length of string
# Example No.01
Name = "Mubashir Rasool"
print(len(Name))

# Example No.02
Country_Name = "Pakistan"
print(len(Country_Name))

# Example No.03
fathers_name = "Abu Abdullah"
print(len(fathers_name))


# 4.Accessing Characters
# Example No.01
Name = "Mubashir Rasool"
Country_Name = "Pakistan"
fathers_name = "Abu Abdullah"
Book_name = "Movies_subscription"
print(Name[1:7])
print(Country_Name[1:])
print(fathers_name[:7])
print(Book_name[:-6])

# 5.Slicing String
s = "Hello World"
print(s[1:5])
print(s[6:])
print(s[:5])
print(s[:-6])

# 6. String Formatting
# Example No.01
name = "Mubashir"
age = 20
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

# Example No.02
first_name = "Mubashir"
last_name = "Rasool"
age = 20
formatted_string = f"My name is {first_name} {last_name} and I am {age} years old."
print(formatted_string)

# Example No.03
first_name = "Mubashir"
last_name = "Rasool"
age = 20
formatted_string = "I'm {} and my age is {}.{}{}".format(first_name, age, first_name, last_name)
print(formatted_string)
# Example No.04
first_name = "Mubashir"
second_name = "Rasool"
formatted_string = "I'm {} and my age is {}.{}{}".format(first_name, age, first_name, second_name)
print(formatted_string)

# 7.String Methods
# Example No.01
Book_name = "Movies_subscription"
print(Book_name.lower())
print(Book_name.upper)
print(Book_name.strip)
Book_name.replace("subscription","App")
Book_name.capitalize
Book_name.count
Book_name.casefold

# 8.Substring
# Example No.01
items = ["apple","Banana","Cherry","Almond"]
print("apple" in items)
print("Graps"  not in  items)
print("Banana" in items)


    

