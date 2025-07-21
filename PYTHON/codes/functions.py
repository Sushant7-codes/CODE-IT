# def whaat(a,b):
#     print(a+b)

# whaat(10,12)
 #////////////////////////////////////////////////////////////////
# for num in range(1,11):
#     print(f"2 x {num}={2*num}")
#////////////////////////////////////////////////////////////////
# def mu_num():
#     num=int(input("Enter the number for multiplication table:"))
    
#     for i in range(1,11):
#         print(f"{num} x {i}= {num*i}")
        
# mu_num()  #Calling of fucntion over here [Function Call]


#////////////////////////////////////////////////////////////////


# def multiple_of_2():
#     for num in range(2,5):
#         print(f"2x {num} = {2*num}")
# multiple_of_2()

#////////////////////////////////////////////////////////////////


# def greet_user(name): #parameters 
#     print("Welcome Here,",name)
    
    
# name=input("Enter your name:") #backend ma garda kheri somewhere other bata aauxa name,maybe database
# greet_user(name) #argument

#////////////////////////////////////////////////////////////////

# names=['Pra','Prab','Prabe','Prabes','Prabesh']

# def likethis(abc):
#     print("DO LIKE THIS,",abc)

# for person in names:
#     likethis(person)

#////////////////////////////////////////////////////////////////
# def greet_user(name,greetings="Welcome here",abc="abccc"):
#     message=f"{greetings},{name} {abc}"
#     print(message)
    
# name=input("Enter you name:")
# # greet_user(greetings="Good evening",name=name) #can be done like this 

# greet_user(name,"Good morning")

#////////////////////////////////////////////////////////////////

# import math
# def add_nums(*args):#any or arbitary number of arguments

#     sum=0
#     for number in args:
#         # print(number)
#         sum +=number
    
#     print(f"Fiunal result of sum is {sum}")
        
#     # print(args)

# add_nums(2,3,4,334,5,666777) 

#////////////////////////////////////////////////////////////////

# def show_details(**kwargs):  #keyword arguments is shown here , lke key and value in dictionary
    
#     # print(kwargs)
#     for k,s in kwargs.items():
#         print(f"{k}=>{s}")
    
# show_details(name="Susnant",age=21,campus="Pn", what="whatsover")

# # num=100,200,233
# # print(num)

