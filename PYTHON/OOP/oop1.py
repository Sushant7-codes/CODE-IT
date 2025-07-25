## CLASS  ##OBJECTS
##ARE THE TWO MAIN TERMINOLOGIES##THAT ARE USED IN OBEJCT ORIENTED PROGRAMMING

## KUNAI PANI REAL WORLD OBJECT LAI REPRESENT GARNI WAY NAI OOP KO MAIN USE HO

## Python OOP= POOP 😂😂

### CLASS IS A BLUEPRINTOF AN OBJECT 
# CLASS is user defined data type 

## OBJECT ARE INSTANCES OF CLASS 

# print(type(5))
# print(type("ram"))
# print(type([1,2,3])) 

# class House:
#     pass

# ram_house=House()

# print(type(ram_house))


## --Book
##    |-Name
##    |-Author
##    |-Pages
##    |-Price 


## --Mobile
##    |-Name
##    |-Ram/rom
##    |-Refresh Rate
##    |-Price 
##    |-Color



# class Book:
#     def __init__(self,name,price):  # initialize  ## method vaneko class vitra function define gareko xa vane teslai method vaninxa, tyo function kunai euta specific class sanga related xa vane tyo method huna janxa 
#         print("Creating a new object of class 'Book'")
#         self.name=name
#         self.price=2000

# book1 = Book("Muna Madan",2000)   #instantiantion --> new instance of class "BOOK"
# print(book1.name)
# print(book1.price)

# book1.name = "Muna Madan" #attributes(eg. name, age, color, price)
# book1.price = 1000

# book2=Book()
# book2.name="Game of Thrones"
# book2.genre="History"
# book2.price=6800

# print(f"Book1 is: {book1.name}, which price is {book1.price}")
# print(f"Book2 is: {book2.name}, which price is {book2.price}")



# class Book:
#     def __init__(self,name,price):  # initialize  ## method vaneko class vitra function define gareko xa vane teslai method vaninxa, tyo function kunai euta specific class sanga related xa vane tyo method huna janxa 
#         print("Creating a new object of class 'Book'")
#         self.name=name
#         self.price=2000

# book1 = Book("Muna Madan",2000)   #instantiantion --> new instance of class "BOOK"
# print(book1.name)
# print(book1.price)

###########################################################

# class Bike:
#     def __init__(self,name,cc,color="Not Set"):
        
#         self.name=name
#         self.cc=cc
#         self.color=color
    
#     def show_info(self):
#         print(f"Name: {self.name}")
#         print(f"CC: {self.cc}")
#         print(f"Color: {self.color}")
        
        
# r15=Bike("R-1-5",cc=225)
# p150=Bike("Pulsar-150",cc=200,color="Blue")
# # print(r15.name, r15.cc, r15.color)
# # print(p150.name, p150.cc, p150.color)  

# p150.show_info()


###############################################

# l1=[1,2,3,4]
# l1.append(5)
# print(l1)

# print("ram".upper()) ##valid method here
# print(5.upper())  ## becomes invalid method here

########################################################

class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno= rollno
        
ram=Student("ram",20)

hari=Student("hari",20)
