#ENUMERATE 

# fruits=['apple','banana',22,None]

# # enumerate(sequence, start=1) ######start=0 will be at default if start is not passed

# for num,name in enumerate(fruits, start=1):
#     print(num,name)
    
# for num,name in enumerate(fruits):  ###esma start nadida start ko num lai 0 set gareko hunxa 
#     print(num,name)


###################DICTIONARY######################################
#-----------------IS - MUTABLE ---------------#
# Set of words and meaning resembled through key:value here

# dict1 ={}  #empty dictionary is mentioned in this way 

dict1={
        "name":"Sushant",
        "age":21, 
        "campus":"PN",
        "abcd":"efgh",
        "key":"value"        
      }

# print(dict1)
# print(type(dict1))

# print(dict1["name"])  #just key can be use to extract values here , rather than index in lists 

# dict1["name"]="SSSSSSSSSSSS" ###in this way we can alter the data , keys and value
# del dict1["campus"]  ##both key and values of campus will be deleted in this way
# dict1.pop("age")  ##esari ni pop out garera delete garna milyo

# dict1["phone_no"]=980676767677677  ##last ma add garna milyo 

###existiing key use gariyo vane update garne kam garxa, and navaye naya key assign gareko hunxa yo mathi ko tarika bata 


# print(dict1.values()) ##value matra pauna ko lagi

# print(dict1.items())  ###in the form of tuple output dinxa 

# print(dict1)

#############################################################

# for item in dict1.items():
#     print(item[0],item[1])
    # print(dict1[item])
    
    
# for key, value in dict1.items():
#     print(key,value)

# print("name" in dict1.keys())  ##gives TRUE
# print("surnameee" in dict1.keys())  ##gives FALSE

# print("sushant" in dict1.values())  ##gives FALSE
# print("Sushant" in dict1.values())  ##gives TRUE
# print("" in dict1.keys())  ##gives FALSE

###################################################################

# for letter in "name":
#     print(letter)

#########################################################

##### REALITY-BASED TEST FOR DICTIONARY ##########

dict2={
    
    "name":{
        "firstname":"Sushant",
        "lastname":"Pahari"
       },
    "age":22,
    "address":{
        "temp":"Pokhara",
        "perm":{
            "Province":"Gandaki",
            "Ward":32,
            "City":{
                "name":"Rajakochautara",
                "street-no":12,
                "house-no":1292
            }
        }
    }
}

# print(dict2)

##TO ACCESS ITEMS IN DICT2-WE DO AS FOLLOWS BY GOING ONE BY ONE 

# person_info= dict2.keys()
# print(person_info)

# person_address= dict2["address"]
# print(person_address)

# person_perm_address= dict2['address']
# print(person_perm_address)

###tTO ACCESS DIRECTLY WE DO AS FOLLOWS AND IS EASY MEASURE

street= dict2["address"]["perm"]["City"]["street-no"]
print(street)


















