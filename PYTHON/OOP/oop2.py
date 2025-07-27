############ 4 PILLARS OF PYTHON-OOP ###############

## 1. Encapsulation
## 2. Inheritance
## 3. Abstraction
## 4. Polymorphism

## 1. ENCAPSULATION
## Encapsulation of any data/protection of data is known as encapsulation
## Birami huda khani capsule, the main element, or say medicine is capsulated inside of it properly, i.e is protected properly

## Access modifiers 
### 3 access modifiers are public,protected and private

# class A:
#     def __init__(self):
#         self.a=10 # a=> public 
#         self._b="Sushant" #b => protected (_b)
#         self.__c="Sushant" #c=>private(__c) ,it can't be changed further
#         #self._A__c= "private c" # => name managling (name lai nai change gardinxa)
    
#     def get_c(self):  #method to get the private "c", using getter ,said as getter method to get the value inside private and protected
#         return self.__c
    
#     @property      # yo property le access gardinxa easily as below #the better way for setter 
#     def c(self):
#         return self.__c
    
    
# a1=A()

# a1.a=55   ###it is being modified easily, so we can protect it 
# print(a1.a) 


# a1._b="Prakash"  # protect ta gareko xaina, but it is a convention only
#                  # we must understand it by seeing the underscore before the variable so that we can understand it, can be changed , but we must remember and follow it 
# print(a1._b)

# print(a1.__c) #it is wronf and it is not accessible 
# print(a1._A__c) #python le private lai chai esari save gareara rakhxa internally

## private or protected ma changes garnu paryo i.e value chaiyo vane getter() use garxam vane change garna setter() use garxam

# print(a1.get_c())  ##for code in line 22's output

# print(a1.c)  #for code line number 25 for @property 


#########################AN EXAMPLE IS BETWEEN HERE ############################################


# class BankAccount:
#     def __init__(self,acc_no,first_deposit=0):
#         self.__acc_no = acc_no
#         self.__balance = first_deposit 
        
#     @property          ## best to use this @property method 
#     def acc_no(self):  ## this is the getter used 
#         return f"XXXX{self.__acc_no[-4:]}"  ##Bank haru ma use huni concept ho yo, full nadekhiwos vanera tyo bank account detail
    
#     @acc_no.setter   ## value change/set garne process chai yo ho 
#     def acc_no(self,new_value):
#         print("You can't set the new account number on your own",new_value)
    
#     @property
#     def balance(self):
#         return self.__balance
    
#     @balance.setter
#     def balance(self,new_value):
#         if not isinstance(new_value,(int,float)):
#             raise Exception ("Deposit balance must be a number")
#         if new_value<0:
#             raise Exception("Deposit value can't be less than 500")
#         self.__balance += new_value

# a1=BankAccount("123456789",6000)

# print("Before:",a1.balance)
# try:
#     # a1.balance=2000
#     a1.balance="two thousand"
# except Exception as e:
#     print(e)
# finally:
#     print("After deposit:",a1.balance)

######################################################

# a1=BankAccount("11294589")
# a1.acc_no="22222222222222222222"  ### set garna namilni  for the setter above  #
# print(a1.acc_no)

##########################################################################################

####  INHERITANCE  ###

## child inheriting characteristics from parents 

# class Animal:   
#     def __init__(self,name):
#         self.name=name
        
#     def speak(self):
#         #codes here
#         return "Animal Produces Sound !!"

# ##ANIMAL IS SUPER CLASS OF DOG AND DOG IS SUB CLASS OF ANIMAL


# class Dog(Animal):  ##animal ko sav kura as a copy paste garxa dog vitra
    
#     def speak(self):  ##esle mathi ko lai override garyo
#         return f"{self.name} barks"  ### gives output as tompson barks 

# ## DOG LAI BARK GARAUNA PARY OVANE 

# class Cat(Dog): # esle dog lai inherit garyo  that means Animall---->Dog---->Cat   Hajurba--> Ba--> Nati 
#                 # tara sidhai animal ni lyauna milxa cat ma   Hajurbaa--> Nati
#     def speak(self):
#         return f"{self.name} does MYAUUUUUU"

# e=Cat("Myauu garne wala")

# d = Dog("Tompson") 
# print(d.name)
# print(d.speak())
# print(e.speak())

# class A:
#     def show(self):
#         print("This is class A")

# class B:
#     def show(self):
#         print("This is class B")

# class C(B,A):  #multiple inheritance , inheriting from 2 parent classes
#     pass
#     # def show(self):
#     #     print("This is class C")

# c=C()
# class D(A,B):  #multiple inheritance , inheriting from 2 parent classes
#     pass
#     # def show(self):
#     #     print("This is class C")

# c=C()
# d=D()

# c.show()  # DUIRAI lai inherit garda kheri "" DIAMOND PROBLEM "" aauxa inheritance ma 
# d.show()  # Duitai ma same xa ani duitai bata aako lai call garda k hunxa vanni nai diamond problem consider garinxa 
#           # Java haru ma chai arkai k xa
#           # Python ma MRO Method Resolution Order hunxa, junma LEFT-->TO-->RIGHT herinxa , ANI FIRST MA jun la iinherit gariyo tei nai aauxa 

########################################################

## ABSTRACTION - the act of hiding unwanted and inside things are hidden , encapsulation also provides the abstraction

### POLYMORPHISM ####

## One thing acting as More Form of itself
## like + is used as addition and concatenation both

# class Animal:   
#     def __init__(self,name):
#         self.name=name
        
#     def speak(self):
#         #codes here
#         return "Animal Produces Sound !!"

# ##ANIMAL IS SUPER CLASS OF DOG AND DOG IS SUB CLASS OF ANIMAL

# class Dog(Animal):  ##animal ko sav kura as a copy paste garxa dog vitra
    
#     def speak(self):  ##esle mathi ko lai override garyo
#         return f"{self.name} barks"  ### gives output as tompson barks 

# a=Animal("Animal")
# d=Dog("Tommyy")
# a.speak()
# d.speak()

# def speak(obj):
#     print(obj.speak())

# speak(a)
# speak(d) 


###ANOTHER EXAMPLE OF POLY 

## another eg

# class BankAccount:
#     def __init__(self,acc_no,first_deposit=0):
#         self.__acc_no = acc_no
#         self.__balance = first_deposit 
        
#     @property          ## best to use this @property method 
#     def acc_no(self):  ## this is the getter used 
#         return f"XXXX{self.__acc_no[-4:]}"  ##Bank haru ma use huni concept ho yo, full nadekhiwos vanera tyo bank account detail
    
#     @acc_no.setter   ## value change/set garne process chai yo ho 
#     def acc_no(self,new_value):
#         print("You can't set the new account number on your own",new_value)
    
#     @property
#     def balance(self):
#         return self.__balance
    
#     @balance.setter
#     def balance(self,new_value):
#         if not isinstance(new_value,(int,float)):
#             raise Exception ("Deposit balance must be a number")
#         if new_value<0:
#             raise Exception("Deposit value can't be less than 500")
#         self.__balance += new_value
        
#     def __eq__(self,other):  ## also called as magic or dunder method 
#         return self.__balance == other.__balance

# a1=BankAccount("123456789",6000)
# a2=BankAccount("222243231",6000)

# print(a1 == a2)

# Write class Name is PascalCase (eg. class PascalCaseIsShowmHere ) , best use 