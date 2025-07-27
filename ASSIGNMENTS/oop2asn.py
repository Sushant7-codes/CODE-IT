### OOP Fundamentals – Assignment Set
''' 
🔹 Topic Coverage:
● Class & Object
● __init__ constructor
● Instance attributes & methods
● Class attributes & methods
● Default arguments
● Object interactions
● Encapsulation (private variables)
● Real-life modeling problems
'''
#########################################################
'''
1. Create a class Laptop
Attributes:
● Brand
● Model
● Price
Methods:
● show_details() → print all information
Hint: Use __init__() to initialize and self.brand etc. to store values.
'''

# class Laptop:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
        
#     def show_details(self):
#         print(f"The '{self.brand}' brand of model '{self.model}' costs you Rs.{self.price:,}")
    
# a1=Laptop("Mac","m2",130000)
# a1.show_details()

# a2=Laptop("Dell","inspiron",110000)
# a2.show_details()

#######################################################

'''
2. Create a class Circle
Attributes:
● radius
Methods:
● area() → returns area (πr²)
● circumference() → returns circumference (2πr)
Hint: Use math.pi from the math module.
'''

# from math import pi

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
    
#     def area(self):
#         # print(f"The area of the circle is:{pi*(self.radius**2)}")
        
#         return pi*(self.radius**2)
        
#     def circumference(self):
#         # print(f"The circumference of the circle is:{2*pi*self.radius}")
        
#         return 2*pi*self.radius


# radius_input=float(input("Enter the radius of the circle:"))
# # a1.area()
# # a1.circumference()

# a1=Circle(radius_input)
# print("Area is:",a1.area())
# print("Circumference is:",a1.circumference())

##############################################################

'''
3. Create a class Employee with class attribute company_name
= "TechSoft"
Each employee has:
● name, position, salary
Methods:
● show_info() → print employee details
● change_company(cls, new_name) → class method to update
company name
Hint: Use @classmethod and cls.company_name = new_name.
'''
# class Employee:
#     company_name = "TechSoft"
    
#     def __init__(self, name, position, salary):
#         self.name=name
#         self.position=position
#         self.salary=salary
        
#     def show_info(self):
#         print(f"Employee with name {self.name} works at {Employee.company_name} on the position of {self.position} with salary of Rs.{self.salary:,} ")
     
#     @classmethod   ## class ko attribute lai change garna paryo vane chai @classmethod use garinxa  
#     def change_company(cls,new_name):  ## cls vaneko uta __init__ vanejastai rahexa, we can take it as reserved word or fixed word that doesnt require any changes inside it 
#         cls.company_name=new_name
    
        
# a1=Employee("Sushant","Manager",200000)
# a1.show_info()
# Employee.change_company("Sushant's Company")
# a1.show_info()

# a2 = Employee("Anita", "Developer", 150000)
# a2.show_info()


###########################################################

'''
4. Design a class ShoppingCart
Attributes:
● customer name
● cart (list of items)
Methods:
● add_item(item)
● remove_item(item)
● view_cart()
Hint: Use self.cart = [] in __init__.
'''
# class ShoppingCart:
    
#     def __init__(self,customer_name):
#         self.customer_name=customer_name
#         self.cart=[]

#     def add_item(self,item):
#         self.cart.append(item) 
        
#     def remove_item(self,item):
#         self.cart.remove(item) 

#     def view_cart(self):
#         if len(self.cart)<=0:
#             print("There is nothing on the cart yet")
#         else:
#             noi=len(self.cart)
#             print(f"{noi} Items currently on the cart are :")
#             for a,b in enumerate(self.cart,start=1):
#                 print(f"{a}.{b}")


# cart=ShoppingCart("Sushant")

# cart.add_item("Tshirt")
# cart.add_item("Pant")
# cart.add_item("Belt")
# cart.add_item("Shoes")
# cart.add_item("Bottle")

# cart.view_cart() 


#######################################################

''' 
5. Create a class BankAccount with balance initialized to 0
Methods:
● deposit(amount)
● withdraw(amount) (only if balance is sufficient)
● check_balance()
Hint: Keep self.balance private (i.e., self.__balance), and use
methods to access/modify it.
'''

# class BankAccount:
    
#     def __init__(self):
#         self.__balance=0   #private 
    
#     def deposit(self,amount):
#         self.__balance+=amount
#         print(f"The balance now available is: {self.__balance}")
        
#     def withdraw(self,amount):
#         if self.__balance<=500:
#             print("You can't have less than 500 on your account")
#         else:
#             self.__balance-=amount
#             print(f"The balance now available is: {self.__balance}")
        
#     def check_balance(self):
#         print(f"The balance on your account is :{self.__balance}")

# acc1=BankAccount()
# acc2=BankAccount()

# acc1.check_balance()# acc2.check_balance()
# print()

# acc1.deposit(2000)
# acc1.deposit(10000)
# print()
# acc1.withdraw(1000)
# acc2.withdraw(20000)


###############################################################

'''
6. Create a class Movie with attributes: title, director, rating
● Store all created movies in a class-level list.
● Add a method is_hit() that returns True if rating > 8.
Hint: Use a class attribute all_movies = [] and
Movie.all_movies.append(self) inside __init__.
'''

# class Movie:
#     all_movies=[]
    
#     def __init__(self,title,director,rating):
#         self.title=title
#         self.director=director
#         self.rating=rating
#         Movie.all_movies.append(self)
        
#     def is_hit(self):
#         if self.rating<8:
#             return False
#         else:
#             return True
        
# m1=Movie("Saiyara","I don't know",8.7)
# m2=Movie("Bahubali","Some Guy",9.9)
# m3=Movie("Bahubali2","Some Guy 2",7.99999999999)

# print(f"{m1.title}",m1.is_hit())
# print(f"{m2.title}",m2.is_hit())
# print(f"{m3.title}",m3.is_hit())

# for movie in Movie.all_movies:
#     print(f"Title: {movie.title}, Rating:{movie.rating}")


#################################################################

'''
7. Create a class Book with method set_discount(percent)
● price is an instance attribute
● discount is class-wide, applied on all books
Hint: Use a class attribute discount_percent = 0 and apply
@classmethod to update it.
'''

# class Book:
#     discount_percent=0
#     all_books=[]
    
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         Book.all_books.append(self)
        
#     @classmethod
#     def set_discount(cls,percent):
#         cls.discount_percent=percent
        
#     def get_discounted_price(self):
#         discount = (Book.discount_percent/100)*self.price
#         return self.price -discount
    
# b1=Book("Python",3400)
# b2=Book("AI-ML",2200)

# Book.set_discount(20)

# print(b1.get_discounted_price())
# print(b2.get_discounted_price())

# for index,books in enumerate(Book.all_books, start=1) :
#     print(f"{index}.{books.name}")


#########################################################################

'''
8. Create a class SchoolStudent
● Attributes: name, class_name, marks (dict)
● Method: add_marks(subject, score)
● Method: average()
Hint: Use a dictionary to hold subject-mark pairs
'''

# class SchoolStudent:
    
#     def __init__(self,name,class_name):
#         self.name=name
#         self.class_name=class_name
#         self._marks={}
        
#     @property
#     def marks(self):
#         for key,value in enumerate(self._marks,start=1):
#             return (f"{key}.{value}")
    
#     @marks.setter
#     def marks(self,subject_score):
#         subject,score= subject_score
#         self._marks[subject]=score
        
#     def average(self):
#         total=sum(self._marks.values())
#         return total/len(self._marks)

# s1=SchoolStudent("SUSHANT","10A")

# s1.marks =("Maths",99)
# s1.marks =("Science",95)

# print(s1.marks)
# print(s1.average())

# s2=SchoolStudent("Ramesh","12C")

# s2.marks =("Nepali",52)
# s2.marks =("English",75)

# print(s2.marks)
# print(s2.average())


###########################################################

'''
9. Create a class Temperature
● Accept temperature in Celsius
● Provide methods:
○ to_fahrenheit()
○ to_kelvin()
Hint:
● °F = (°C × 9/5) + 32
● K = °C + 273.15
'''

# class Temperature:
    
#     def __init__(self,celsius):
#         self.celsius=celsius
        
#     def to_fah(self):
#         return (self.celsius*9/5)+32

    
#     def to_kel(self):
#         return self.celsius+273.15
    
# c1=Temperature(34.4)
# print(c1.celsius,"C")
# print(c1.to_fah(),"F")
# print(c1.to_kel(),"K")

# c2=Temperature(38.6)
# print(c2.celsius,"C")
# print(c2.to_fah(),"F")
# print(c2.to_kel(),"K")


########################################################

'''
10. Build a class FlightBooking
Attributes:
● passenger_name
● flight_no
● destination
Keep a class attribute total_bookings, and increase it every time a new
booking is made.
Hint: Use FlightBooking.total_bookings += 1 in __init__.
'''



# class FlightBooking:
#     total_bookings=0
#     all_bookings=[]
    
#     def __init__(self,passenger_name,flight_no,destination):
#         self.passenger_name=passenger_name
#         self.flight_no=flight_no
#         self.destination=destination
#         FlightBooking.total_bookings+=1 
#         FlightBooking.all_bookings.append(self)
        
# f1=FlightBooking("Ssushant","1337A","Kathmandu")
# f1=FlightBooking("Rameshhh","1118A","Pokhara")
# f1=FlightBooking("Hamesh","1358A","Morang")

# print(f"Total Passengers={FlightBooking.total_bookings}")

# for key,value in enumerate(FlightBooking.all_bookings,start=1):
#     print(f"{key}.{value.passenger_name}-{value.flight_no} to {value.destination}")


#######################################################################################

##BONUS##

'''11. Class: TaskManager
You are building a CLI-based task tracker for your students.
Attributes:
● user_name
● task_list (initially empty)
Methods:
● add_task(task)
● remove_task(task)
● view_tasks()
Hint: Use a list to store tasks. Add/remove using list methods.
'''

# class TaskManager:
    
#     def __init__(self,user_name):
#         self.user_name=user_name
#         self.task_list=[]
        
#     def add_task(self,task):
#         self.task_list.append(task)
    
#     def remove_task(self,task):
#         if task in self.task_list:
#             self.task_list.remove(task)
#         else:
#             print(f"Task '{task}' not in task list.")
    
#     def view_tasks(self):
#         for no,task in enumerate(self.task_list,start=1):
#             print (f"{no}.{task}")
    
# t1=TaskManager("Sushant")
# t1.add_task("Finish Math Homenwork")
# t1.add_task("Clean your room")

# t1.view_tasks()

# t1.remove_task("Suiiii")

# t1.remove_task("Finish Math Homenwork")

# t1.view_tasks()

##############################################################