### INPUT AND CONDITIONAL ASSIGNMENTS ####

#Basic Level Questions

# 1. Even or Odd
# 🔸 Ask the user for a number. Use the modulo operator % to check if it's
# divisible by 2.
# Hint: number % 2 == 0 means the number is even.

# a = int(input("Enter a number:"))

# if a%2==0:
#     print("Even")
    
# else:
#     print("Odd")

############################################################

# 2. Positive, Negative, or Zero
# 🔸 Input a number and use if–elif–else to compare it with 0.
# Hint: Use conditions like > 0, < 0, and == 0.

# a = int(input("Enter a number:"))

# if a>0:
#     print("Positive number !")
    
# elif a<0:
#     print("Negative number !")
# else:
#     print("Number is zero !")


############################################################

# 3. Largest of Two Numbers
# 🔸 Ask the user for two numbers and compare them using if and else.
# Hint: Use if a > b: to find the larger number.

# a = int(input("Enter first number:"))

# b = int(input("Enter second number:"))

# if a>b:
#     print(f" {a} is larger than {b}")
# else:
#     print(f" {b} is larger than {a}")


############################################################

# 4. Check Voting Eligibility
# 🔸 Input age and check if it’s 18 or more.
# Hint: if age >= 18:

# age= int(input("Enter your age:"))

# if age>18:
#     print("You're eligible to vote")
    
# else:
#     print("You must be greater than 18 to vote")

############################################################

# 5. Divisible by 5 and 11
# 🔸 Take a number and check if it's divisible by both 5 and 11.
# Hint: Use if number % 5 == 0 and number % 11 == 0:

# number=int(input("Enter a number:"))

# if number%5==0 and number%11==0:
#     print(f"Number {number} is divisible by both 5 and 11")
    
# else:
#     print(f"Number {number} is not divisible by both 5 and 11")

############################################################

# 6. Leap Year Checker
# 🔸 Input a year and check leap year using proper conditions.
# Hint: A year is leap if:
# ○ Divisible by 4, and not divisible by 100,
# ○ or divisible by 400

# year=int(input("Enter the year you'd like to check if it is leap year or not :"))

# if (year%4==0 and year%100!=0) or (year%400==0):
#     print(f"The year {year} is leap year")
    
# else:
#     print(f"The year {year} is not leap year")

############################################################

# 7. Character Type Checker
# 🔸 Input a single character. Use built-in string methods or ASCII ranges.
# Hint: Use .isalpha(), .isdigit(), or check ASCII code with ord().

# abc=input("Enter anything:")

# if abc.isalpha():
#     print("Given input is alphabet")
    
# elif abc.isdigit():
#     print("Given number is digit")
    
# else:
#     print("It is neither alphabet nor digit")
   
   
############################################################

# 8. Uppercase or Lowercase Alphabet
# 🔸 Input a character and determine its case.
# Hint: Use .isupper() or compare ASCII values:
# ○ A–Z: 65–90
# ○ a–z: 97–122

# inp=input("Enter string:")

# if inp.isupper():
#     print("Input string is UpperCase")
# elif inp.islower():
#     print("Input string is Lowercase")
# else:
#     print("NEITHER")

############################################################

# 9. Weekday Name by Number
# 🔸 Input a number (1–7) and print the weekday.
# Hint: Use a chain of if, elif, else statements for 1 to 7.

# weeknum=int(input("Enter the day of the week:"))

# if weeknum<=0 or weeknum>7:
#     print("Out of week")
#     exit()
# else:
#     if weeknum==1:
#         print("Sunday")
#     elif weeknum==2:
#         print("Monday")
#     elif weeknum==3:
#         print("Tuesday")
#     elif weeknum==4:
#         print("Wednesday")
#     elif weeknum==5:
#         print("Thursday")
#     elif weeknum==6:
#         print("Friday")
#     else:
#         print("Satuday, Hoorrayy")

############################################################

# 10. Grade Assigner
# 🔸 Input marks (0–100) and assign grades accordingly.
# Hint: Use multiple conditions like if 90 <= marks <= 100: and so on.

# marks=int(input("Enter your marks obtained:"))
# if marks<0 or marks >100:
#     print("Dude, don't go out of syllabus, sybau and enter your real marks")
#     exit
# else:  
#     if marks>0 and marks<40:
#         print("You failed dude, grind harder")
#     elif marks==40:
#         print("Lucky lucky guy, go harder")
#     elif marks>40 and marks<60:
#         print("You can do better")
#     elif marks>=60 and marks<70:
#         print("NIce, Keep it up, B")
#     elif marks>=70 and marks<80:
#         print("Great, push a bit and no one can stop you, B+")
#     elif marks>=80 and marks<90:
#         print("Great, guy behind you is pushing to get over you, dont let him do it, A")
#     elif marks>=90 and marks<100:
#         print("Great,a few more and You'll be on the top of list, A+")
#     else:
#         print("You're on the top, 4 GPA")
    

##############################################################
