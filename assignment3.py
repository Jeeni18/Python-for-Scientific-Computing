#Use a custom defines decorator to meature the execution time of any function.Use time module to compute time
import time
def time_func(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args, **kwargs)   #calling a function
        stop = time.time()
        print(f"Execution time: {stop - start}seconds")
    return wrapper    

@time_func
def number_generator(num):
    for i in range(num):
        print(i)

@time_func
def sum_of_list(input_list):
    sum = 0
    for item in input_list:
        sum = sum + item
    return sum

number_generator(20) #calling
input_list = [1,2,3,4,5,6,7,8,9,10,11,12]
sum_of_list(input_list)