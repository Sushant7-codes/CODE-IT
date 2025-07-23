# ####DECORATORS ######################

# def test_decor(func): ##helps to decorate and is decorator function
#     def wrapper_func():
#         print("This is before test function.")
#         func()
#         print("This is after text function")
#     return wrapper_func


# @test_decor
# def test():
#     print("This is the test function")
    
    
    
# test()


##########  FOR EXAMPLE   ####################
# def login_required(func):
#     def wrapper(*args, **kwargs):
        
#         user_role="admin"
        
#         if user_role=="admin":
#             func(**args, **kwargs)
            
#         else:
#             print("You ain't admin dude !!")
#             login_view()
            
#         user_logged_in = False
        
#         if user_logged_in:
#             func(*args, **kwargs)
            
#         else:
#             print("Please login first")
       
#     return wrapper

# @login_required
# @admin required 
# def home_view():
#     print("This is home page")
    
# def admin_view():
#     print("This is admin page")
    
# def login_view():
#     print("You came to login site")
    
##eg: https://sushantpahari.com.np/home/  
# home_view()

#eg: https://domain/admin/



####Simple example
# import csv
import time

# def exe_time(func):
#     def wrapper(*args, **kwargs):
        
#         start_time=time.time()
#         func(*args, **kwargs)
#         end_time=time.time()
#         time_taken =end_time-start_time
#         print(f"{func.__name__} took {time_taken} seconds")
        
#     return wrapper


# @exe_time
# def tc_task():
#     time.sleep(2)
#     print("Completed the Task")
    
# @exe_time
# def read_students():
#     with open("students.csv", "r") as file:
#         reader=csv.reader(file)
#         for row in reader:
#             print(row)
    
# tc_task()
# read_students()

###################################################################
###################################################################

##  GENERATORS 
# def test_gen():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     yield 6
    
# gen_obj =test_gen()

# # print(next(gen_obj))
# # print(next(gen_obj))
# # print(next(gen_obj))
# # print(next(gen_obj))
# # print(next(gen_obj))
# # print(next(gen_obj))
# # print(next(gen_obj))

# for value in gen_obj:
#     print(value) 

###############
# def inf_even_num_gen():
#     even =2
#     while True:
#         yield even #pauses here until next task is asked
#         even+=2


# even_number= inf_even_num_gen()

# # print(next(even_number))
# # print(next(even_number))
# # print(next(even_number))
# # print(next(even_number))
# # print(next(even_number))
# # print(next(even_number))
# # print(next(even_number))

# for _ in range(100):
#     print(next(even_number))

# def password_gen(filename):
#     with open(filename, "r") as file:
#         for line in file:
#             # yield time 
#             yield line.strip()
            
# password=password_gen("passwords.txt")

# # print(next(password))
# # print(next(password))
# # print(next(password))

# pass_to_crack = "admin123"

# while True:
#     try:
#          p = next(password)

#          if p == pass_to_crack:
#              print("Cracked password is :",p)
#              break
         
#            except StopIteration:
#              print("Dictionary scan completed, password not cracked")
#              break

######################################

### LAMBDA FUNCTION -- ONE LINER CODE 

#Lamda function (anon-function, one-liner function, any number of arguments can be taken, but can return only one value )


# def tet(a,b):
#     return a+b

# test= lambda a,b:(a+b,a-b)
# # test(6,9)
# print(test(9,6))

####################################

# USED IN FILTERS AND MAPS 

#Filter (HIGHER ORDER FUNCTION)
# numbers = [1,2,3,4,5,6,7,8,9]
# odd_nos= list(filter(lambda x: x%2==1, numbers))
# even_nos= list(filter(lambda x: x%2==0, numbers))

# print(odd_nos)
# print(even_nos)


#Map
# a= [1,2,3,4,5,6,7,8,9]
# b= list(map(lambda x:x**2, a))
# print(b)

# a=[1,2,3,4]  ##roll numbers
# b=["suhsnat","ram","sushantttt","hari"]   #name of students

# for rollno,name in zip(a,b): #zip use garera use garna skainxa esto ma , 2ta ko lai combine garera single output nikalna xa vane esto garinxa 
#     print(rollno,name)


###############################################
###############################################

### COMPREHENSIONS ######
##alternate way to create a new data structure from a exisiting data structure

#LIST COMPREHENSIONS

# l1=[1,2,3,4,5,6,7,8,9]
# # l2=[num**2 for num in l1]
# l2=[num**3 for num in l1 if num%2==0]
# l3=[num**3 for num in l1 if num%2==1]

# print(f"l2 is {l2} which gives even")
# print(f"l3 is {l3} which gives odd")



###Dictionary Comprehension


d1={"name":"sushant","roll":21, "address":"Pokhara-32"}

# # d2={key: value for key,value in d1.items() if len(key)>6}

# d2={value: key for key, value in d1.items()}
# print(d2)



# gen = {num for num in range(2)}
# print(gen)

d1_sorted = sorted(d1.items(), key=lambda item: item[0])
print(d1_sorted)