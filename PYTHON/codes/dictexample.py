###CACHING AND MEMOIZATION !!!!!!!#####
import time

CACHE={}

def heavy_task(a):
    
    if a in CACHE.keys():
        print("result already calculated as")
        return CACHE[a]
    
    time.sleep(3) #to represent time taken by a certain task
    res = a**2
    
    
    CACHE[a]= res
    
    return res

print("First TIME:",heavy_task(5)) #takes time cause there is no 5 in cache
print("sECOND time:",heavy_task(5)) #esle time khann casue cache ma already xa 5 
print("FOR another number:",heavy_task(7))  ##esle time khanxa cause 7 is not in cache

print(CACHE) 