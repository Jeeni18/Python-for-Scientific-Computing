# # def function_name(lis_of_parameters):
# #     body
# #     return value

# #function to add two numbers
# #dunction definition
# def add_two_nums(num1,num2=15):
#     """
#     This function adds two numbers.

#     Arguments :
#        num1 : first number
#        num2 : second number
       
#     Return:
#        sum of num1 and num2   
#     """
#     sum = num1 + num2
#     return sum

# #function call
# sum = add_two_nums(10,20)        #positional argument
# print(f"Sum: {sum}")


# #Keyword arguments
# sum = add_two_nums(num1=20, num2=20)           #keyword argument
# print(f"Sum: {sum}")

# #for default argument
# sum = add_two_nums(10)       
# print(f"Sum: {sum}")

# #Unpacking of list, tuple
# list1 = [10,20,30,40,50]
# # x, y, z = list1
# # print(x,y,z)
# #to access only some elements we can use * operator t unpack sequence
# x,*y,z = list1
# print(x,y,z)

# add = 10             #global variable
# def sum(*args):
#     sum = 0                    #local variable
#     print(args)
#     for value in args:
#         sum = sum + value
#     return sum
# result = sum(10,20,30,40,50)
# print(add)
# print(result)

#**kwargs   keyword arguments
#**kwargs is used to pass arbitary number of keyword argument whereas *args is used to pass arbitary number of positional arguments

def student_details(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f"{key}: {value}")
student_details(name = "Har", age = 25,adderess = "ktm",course="python")

#aargs should be followed by kwargs
def student_details_new(name, *args , **kwargs):
    print(name)
    print(args)
    print(kwargs)

student_details_new("Ram",25,"Bhaktapur",courses="python")


#lamda functions 
#called as anonymous functions because it has no name
#syntax:
    #lambda arguments: expression
    #lambda arguments :values if condition else else_value

def square(num):
    return num**2
sq_of_10 = square(10)
print(sq_of_10)


#using lambda function
square : lambda num: num ** 2
sq_of_10 = square(10)
print(sq_of_10)


# print square of even numbers else print cube
square_lambda_func = lambda num: num ** 2 if num % 2 == 0 else num **3
print(square_lambda_func(3))