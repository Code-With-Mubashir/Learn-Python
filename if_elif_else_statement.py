# If elif Else & nested statement
# 1.If else statement
# Example No.01
age = 18
if age <= 18:
    print("Not Adult")
else:
    print("Adult")
 
# Example No.02
age = 20
if age <= 18:
    print("Eligible to cast vote")
else:
    print("Not eligible to case vote")   
    
# Example No.03
x = 20

if x < 10:
    print("x is less than 10")
elif x < 30:
    print("x is between 10 and 29")
else:
    print("x is 30 or more")

    
# 2.If elif else statement
# Example No.01
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Example No.02

num = -7

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# Example No.03
temperature = 15

if temperature > 30:
    print("It's hot outside")
elif temperature > 20:
    print("It's warm outside")
elif temperature > 10:
    print("It's cool outside")
else:
    print("It's cold outside")

# Nested Statement:
# Example No.01
age = 17

if age >= 18:
    print("You are an adult")
    if age >= 21:
        print("You can drink alcohol")
    else:
        print("You cannot drink alcohol yet")
else:
    print("You are a minor")
    if age >= 16:
        print("You can get a learner's permit")
    else:
        print("You cannot get a learner's permit")

# Example No.02
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    if score >= 85:
        print("Grade: B+")
    else:
        print("Grade: B")
else:
    print("Grade below B")

# Short Hand statement
# Example No.01
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
# Example No.02
a, b = 10, 15
smaller = a if a < b else b
print(smaller)  # 10
# Example No.03
score = 75
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)  # C


