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


          

    


