#passing function as an argument to another function

def function1():
    print("Hello from function 1")
def function2(func):
    print("Hello from function 2")
    func()

function2(function1)

#returning function from another function
def outer_func():
    print("Hello from outer function")
    def inner_func():
        print("Hello from inner function")
    return inner_func
func_var = outer_func()
func_var()

#decorators
#decorators are used for mostly repeated cases
#to calculate square root of a number
import math
def square_root(num):
    sq_root = math.sqrt(num)
    return sq_root

def decorator_positive_number_only(ori_func):
    def wrapper(num):
        if num < 0:
            print("Only positive numbers allowed")
            raise ValueError                          #raises an error
        else:
            sq_root = ori_func(num)
            return sq_root
    return wrapper 

#using a decorator
new_decorated_func = decorator_positive_number_only(square_root)
print(new_decorated_func(9))
# print(new_decorated_func(-9))    #error 

#shorthand notation to use decorator
@decorator_positive_number_only
def area_of_square_land(length):
    area = length ** 2
    return area

#new_area_decorated_func = decorator_positive_number_only(area_of_square_land)
# print("Area of land with length 10:", new_area_decorated_func(10))
# print("Area of land with length 10:", new_area_decorated_func(-10))
print("Area of land with length 9:", area_of_square_land(9))
print("Area of land with length -9:", area_of_square_land(-9))