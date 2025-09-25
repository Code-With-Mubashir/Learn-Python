# Learn-Python-with-Mubashir
I'm passionate python programmer and welcome to learning python with Mubashir. This repository is designed for students, teachers and researcher who is beginner and want to excel in their field. Whether you're just starting career as passionate programmer or looking to sharpend your skills, this series provide structured, hands on learning through **Jupyter Notebook** covering different topics.
## 💡 What is a String?
Strings are sequence of numbers, letters, symbols and spaces enclosed into single, double or triple quotes. Strings are ordered collection, immutable once created it cannot be changed, strings are primarily used to strore and manupulate textual data.
- Single Quote 'Hellow World'
- Double Quote "Hello World!"
- Triple Quote ''' This is your Second Assignment'''
## 🛠️ String-Operations
string operations are action performed on sequence of characters (string) in programming, including cancatination, substringing, comparison, case conversion, finding length and finding specific character or sub strings.
Here are some **common string operation**s:
### 1.Cancatination
Joining two or more srings together to form a single, longer string. You can join two or more strings using ' + ' operator.
### 2.Substring
Extracting a portion of a string from it.
### 3.Length
Determining the number of character from string by using the len(). It counts all number, spaces, character and symbols.
### 4.Repetition
Repetition means saying the same thing again and again. Repeat a string multiple times using the * operators.
### 5.Indexing 
Strings are like list of characters. You can get any letter using its index starting from 0. Think of it like picking a word by its position.
### 6.Slicing(Getting Part of string)
You can get any part of string by using [start:end]
### 7.Changing Cases
Use methods like .upper(),.lower() and .title() to change letter cases. It is used for formating text nicely.
### 8.Stripping(Removing Extra spaces)
In string, .strip() method used to remove extra spaces from beginning and end.
### 9.Replacing
In string, .replace() method used to replace specific part of word or letter.
### 10.Checking Substring
Use in to check one string is inside another. It is very helpful to search in text.
### 11.Spiliting and Joining
- .spilit() method used to breat the string into list.
- .join() method used to join the string together.
### 12.String Formating
We can add values into strings f-string or .format().
## 🧑‍💻 What is User Input?
  Let's talk about user input in very easy way. 
  User input means getting information from the user using the program. We use the input() function to do this in python.
  
                                        age = int(input("Enter your age: "))
                                                    print(age + 5)
## 🧮 What are operators ?
Operators are symbols or special words that are used to perform operatios on variable or values.
                                        a = 5
                                        b = 3
                              print(a + b)  # Output: 8

### Common Types of Operators:
**1. Arithmetic Operators:**
          Arithmetic operators are used to perform basic mathematic operations.Some Common Arithmetic Operators are
| operator | Description    | Example     |
|----------|---------------|-------------|
| +        | Addition      | 3 + 1 = 4   |
| -        | Subtraction   | 2 - 1 = 1   |
| *        | Multiplication| 4 * 2 = 8   |
| /        | Division      | 8 / 2 = 4   |
| %        | Modulus       | 5 % 2 = 1   |
| **       | Exponentation | 2 ** 3 = 8  |

           
**2.Comparison operators:**
        Comparison operators are used to compare two values.Some Common Comparison Operators are
| operator | Description        | Example  |
|----------|--------------------|----------|
| ==       | Equal to           | 5 == 5   |
| !=       | Not Equal to       | 5 != 5   |
| >        | Greater than       | 4 > 2    |
| <        | Less than          | 2 < 4    |
| >=       | Greater or Equal   | 6 >= 6   |
| <=       | Less or Equal      | 3 <= 5   |

**3.Logical Operators:**
         Logical Operators are used to combine and invert boolean values.
         Some Common Logical Operators are
| Operator | Name        | Description                              | Example          | Result |
|----------|-------------|------------------------------------------|------------------|--------|
| `&&`     | Logical AND | True if **both** conditions are true     | `true && false`  | false  |
| `||`     | Logical OR  | True if **at least one** condition is true| `true || false`  | true   |
| `!`      | Logical NOT | Inverts the truth value                   | `!true`          | false  |

         
  # Operators & conditions
  ## Identity operators
  An identity operators determines whether two variables or values refer to the same object in memory.
    In python, the primary identity operators are:
    **is**: This operator returns **True** if both operands refer to the exact same object in memory, and **False** otherwise.
   **is not**: This operator returns **True** if both operands refer to different objects in memory, and **False** otherwise.

  ## Membership operators
  Membership operators are used to test for the presence of a value within a sequence. They determine if a specific element or substring exists within a larger collection of data. These operators are commonly used in programming languages like Python. 
  In Python, the two primary membership operators are:
**in operator:** This operator evaluates to **True** if the value on its left operand is found within the sequence on its right operand. Otherwise, it evaluates to **False**.
**not in operator:** This operator is the inverse of in. It evaluates to **True** if the value on its left operand is not found within the sequence on its right operand. Otherwise, it evaluates to **False**.

## Bitwise Operator
A bitwise operator performs a logical or bitwise operation on the individual bits of integers. Common bitwise operators include AND (&), OR (|), XOR (^), and NOT (~), which act on the binary representations of numbers to manipulate them at the bit level for tasks like setting flags, encryption, and data compression.  
**Common Bitwise Operators:**
**Bitwise AND (&):** Returns 1 only if both corresponding bits are 1. 
**Bitwise OR (|):** Returns 1 if at least one of the corresponding bits is 1. 
**Bitwise XOR (^):** Returns 1 if the corresponding bits are different (one is 0 and the other is 1). 
**Bitwise NOT (~):** Inverts each bit (0 becomes 1, and 1 becomes 0). 
**Left Shift (<<):** Shifts the bits of a number to the left by a specified number of positions, filling the rightmost positions with zeros. 
**Right Shift (>>):** Shifts the bits of a number to the right, filling the leftmost positions according to the type of shift (arithmetic or logical). 

| Operator | Name         | Description                                  | Example (a = 5, b = 3)        | Result (Decimal) | Result (Binary) |
|----------|--------------|----------------------------------------------|-------------------------------|------------------|-----------------|
| `&`      | AND          | Sets each bit to 1 if both bits are 1        | `a & b` → `5 & 3`             | 1                | `0001`          |
| `|`      | OR           | Sets each bit to 1 if one of the bits is 1   | `a | b` → `5 | 3`             | 7                | `0111`          |
| `^`      | XOR          | Sets each bit to 1 if bits are different     | `a ^ b` → `5 ^ 3`             | 6                | `0110`          |
| `~`      | NOT          | Inverts all the bits                         | `~a` → `~5`                   | -6               | `...11111010`   |
| `<<`     | Left Shift   | Shifts bits to the left, adds 0s on the right| `a << 1` → `5 << 1`           | 10               | `1010`          |
| `>>`     | Right Shift  | Shifts bits to the right, discards rightmost | `a >> 1` → `5 >> 1`           | 2                | `0010`          |

# 🧮 DATA TYPES
Data types in python define the type of value a variable holds _______ whether it's number, text, list, etc.

### 🔢 Common Built-in Data Types in Python

Some common built  in data types in python are given below.

#### 1. Numeric Data Type
Numeric data type represent different type of numbers such as Int, float and complex.
##### Integer 
Integer data type represents whole number which is stored in variable.
##### Float
Float data type represents decimal number which is stored in variable.
##### Complex
Complex data type represents complex number — number with real part and imaginary part.
## Some Common Math Function 
Some common math functions you can use in Python’s built-in math module, with examples.
| Function               | Description                         | Example                        | Output           |
|------------------------|-------------------------------------|-------------------------------|------------------|
| `math.sqrt(x)`         | Square root                        | `math.sqrt(16)`                | `4.0`            |
| `math.pow(x, y)`       | x raised to the power y            | `math.pow(2, 3)`               | `8.0`            |
| `math.ceil(x)`         | Smallest integer ≥ x               | `math.ceil(4.2)`               | `5`              |
| `math.floor(x)`        | Largest integer ≤ x                | `math.floor(4.7)`              | `4`              |
| `math.sin(x)`          | Sine of x (x in radians)           | `math.sin(math.pi/2)`          | `1.0`            |
| `math.cos(x)`          | Cosine of x (x in radians)         | `math.cos(0)`                 | `1.0`            |
| `math.tan(x)`          | Tangent of x (x in radians)        | `math.tan(math.pi/4)`          | `1.0`            |
| `math.log(x[, base])`  | Logarithm of x (default base e)    | `math.log(100, 10)`            | `2.0`            |
| `math.exp(x)`          | Exponential function \(e^x\)       | `math.exp(2)`                 | `7.389056...`    |
| `math.factorial(n)`    | Factorial of n (n!)                 | `math.factorial(5)`            | `120`            |
## Functional Control Statement
The if-elif-else statement is a fundamental control flow structure in many programming languages, including Python, used for making decisions and executing different blocks of code based on conditions. 


- **if —** Tests a condition; runs code block if condition is True.

- **elif —** “else if” — tests another condition if previous if or elif was False.

- **else —** Runs if all previous conditions were False.          
### Nested statement
A nested statement in Python refers to placing one or more statements inside another statement.


age = 25

is_student = True

if age >= 18:

    print("You are an adult.")
    
    if is_student:
    
        print("You are also a student.")
        
    else:
    
        print("You are not a student.")
        
else:

    print("You are a minor.")


### Short hand statement
In Python, the shorthand if-else statement is also known as a conditional expression or ternary operator. It allows you to write a concise if-else statement on a single line, returning a value based on a condition  
    
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)


# 1.While_Loop
It is control flow statement in python which allows code to be executed repeatedly as long as the condition is true.

**Syntax**

	While condition:
	
## Infinite loop
If the condition never becomes false, then the loop will run forever called and infinite loop.
# 2. For_Loop
A for loop in python is used to iterate over a sequence and execute block of code for each item in iteration.

**Syntax**
		for item in sequence:
		
## Nested Loop
A loop inside another loop is called nested loop. You can nest for loops, while loops, or mix them.

**Syntax**

	For outer in outer sequence:
	
	For inner in inner sequence:
	
## Loop Control Statements
Loop control statements help you change the normal flow of loop. They help you:
-	Break the loop
-	Exit the certain iteration of loop
-	Add placeholder
-	
### 1.Break Statement
Break statement stops the loop completely, even if the condition is still True.
### 2. Continue statement
Continue statement skips the current iteration and move to the next one.
### 3. Pass statement
Pass statement does nothing. It’s used when a statement is syntactically required but you don’t want any action.
 ## Range Function
Range function in python is used to generate a sequence of numbers, which is commonly used in loops especially for loops.
The purpose of range function is to provide a sequence of numbers to iterate over in loop.

**Syntax**

range(stop)

range(start, stop)

range(start, stop, step)

## Else Clause
In python, for loop and while loop can have an else clause which is executable only if the loop is not terminated by break statement.


**Syntax**

for item in iterable:

    ***loop body***
	
    if condition:
	
        break
else:

    *** runs only if the loop wasn't broken***
	
	
**Syntax**

while condition:

    ***loop body***
	
    if condition_to_break:
	
        break
else:

    *** runs only if loop ended normally (not by break)***










