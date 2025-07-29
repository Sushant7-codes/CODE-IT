'''
1. Class and __init__
Question 1: Create a Book class with title, author, and year of publication.
● When creating an object, these 3 values should be initialized using the
__init__ method.
● Then, print the book details using a method.
Hint:
● Use self.title, self.author, self.year in the __init__.
● Create a method show_details(self) to print details.
'''

# class Book:
#     def __init__(self,title,author,pub_year):
#         self.title=title
#         self.author=author
#         self.pub_year=pub_year
        
#     def show_details(self):
#         print(f"The book {self.title} , which was written by {self.author} was published on the year {self.pub_year}")

# b1=Book("Game of Thrones","Ned Stark","2002")
# b2=Book("Muna Madan","Laxmi Prasad Devkota ","1998")
# b1.show_details()
# b2.show_details()

########################################################

'''
2. __init__ with Default Arguments
Question 2: Create a class Student with name and grade. If no grade is
given, use "Not Assigned" as default.
Hint:
● Define def __init__(self, name, grade="Not Assigned").
'''

# class Student:
#     def __init__(self,name,grade="Not Assigned"):
#         self.name=name
#         self.grade=grade
        
#     def show_details(self):
#         if self.grade=="Not Assigned":
#             print(f"The grade of student named {self.name} is not assigned")
#         else:
#             print(f"Student with name {self.name} studies in grade {self.grade} ")

# s1=Student("Ram",10)
# s1.show_details()

# s2=Student("Ramesh")
# s2.show_details()

################################################################

'''
3. Simple Methods
Question 3: Create a class Calculator that takes two numbers and
provides methods:
● add(self)
● subtract(self)
● multiply(self)
● divide(self)
Hint:
● Store numbers in __init__, and create a method for each operation using
self.num1 and self.num2.
'''

# class Calculator:
#     def __init__(self,num1=int(input("Enter a number1:")),num2=int(input("Enter a number2:"))):
#         self.num1=num1
#         self.num2=num2
        
#     def add(self):
#         return self.num1+self.num2
#     def sub(self):
#         return self.num1-self.num2
#     def mul(self):
#         return self.num1*self.num2
#     def div(self):
#         return self.num1/self.num2

# c1=Calculator()
# print(c1.add())
# print(c1.sub())
# print(c1.mul())
# print(c1.div())

######################################################################

'''
4. Instance Attribute vs Class Attribute
Question 4: Create a class Dog:
● Every dog has a name (instance attribute).
● All dogs belong to species "Canine" (class attribute).
Hint:
● Define species = "Canine" outside __init__.
● Define self.name = name inside __init__.
● Try printing dog1.species and Dog.species.
# '''

# class Dog:
#     dog_species="Canine"
    
#     def __init__(self,dog_name):
#         self.dog_name=dog_name
        
#     def show_detail(self):
#         print(f"The dog with name {self.dog_name} belongs to {self.dog_species} species.")
        
# dog1=Dog("Puppy")
# # dog1.show_detail()

# print(dog1.dog_species)
# print(Dog.dog_species)

###########################################################################

'''
5. Instance Method vs Class Method
Question 5: Create a class School:
● Instance attribute: student_name
● Class attribute: school_name = "ABC Public School"
● Instance method: get_student_info(self) → prints student name and
school
● Class method: change_school_name(cls, new_name) → changes
school name
Hint:
● Use @classmethod decorator for class method.
● Use cls.school_name = new_name inside class method
'''

# class School:
#     school_name="ABC Public School"
    
#     def __init__(self,student_name):
#         self.student_name=student_name
        
#     def get_student_info(self):
#         print(f"Student with name {self.student_name} studies in {self.school_name} ")
        
#     @classmethod
#     def change_school_name(cls,new_sc_name,student_name=None):
#         cls.school_name=new_sc_name
        
#         # if student_name:
#         #     print(f"Student with name {student_name} changed school to {new_sc_name}")
#         # else:
#         print(f"School name has been changed to {new_sc_name}")
# s1=School("Sushant")
# s1.get_student_info()

# s1.change_school_name("SSHA")

######################################################

'''
Bonus Real-Life Scenario Based (Combining above)
Question 6: Create a class BankAccount:
● On creation, accept name and balance (default: 0).
● Method: deposit(self, amount)
● Method: withdraw(self, amount)
● Method: display_balance(self)
Hint:
● Initialize balance to 0 if not given.
● In deposit, add amount to balance.
● In withdraw, subtract only if enough balance exists.
● Use self.balance.
'''


# class BankAccount:
#     def __init__(self,name,balance=0):
#         self.name=name
#         self.balance=balance
    
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print(f"The balance after depositing {amount} becomes: {self.balance}")
        
#     def withdraw(self,amount):
#         if amount<self.balance:
#             self.balance=self.balance-amount
#             print(f"The balance after withdrawing {amount} becomes: {self.balance}")
#         else:
#             print ("Insufficient Balance")
            
#     def display(self):
#         print(f"The residing balance in your account is: {self.balance}")
        
# b1=BankAccount("Sushant")
# b1.display()
# b1.deposit(12000)
# b1.withdraw(11999.99)
# b1.display()

# b1.deposit(120000)
# b1.withdraw(14000)
# b1.display()

#####################################################################