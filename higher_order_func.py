# #Iterators and Iterable
# #Iterables
#     #Iterables are those objects whose elements can be accessed using loops
#     #eg: list,tuple,set,dictionary,etc
#     #Iterables have methods like _iter_()

# #Iterators
#     #Iterators are those objects which stores string of data
#     #Iterators are methods like _next_() and _iter()_
     
# my_list = {1,2,3,4,5}
# #my_list is iterable because we can access its elements using loops
# for num in my_list:
#     print(num) 

# #my_list as iterable
# my_ierator = iter(my_list)
# print(my_ierator)

# first_element = next(my_ierator)  #after accessing the element it is removed so it is memory efiicient
# print(first_element)
# second_element = next(my_ierator)
# print(second_element)
# print(next(my_ierator))
# print(next(my_ierator))
# print(next(my_ierator))

# #converting Iterator to list(Iterable)
# new_iterator = iter(my_list)
# first_element = next(new_iterator)
# print(first_element)
# new_list = list(new_iterator)
# print(new_list)

# #map function in python
#     #map is the higher order function which takes two arguments viz.
#     #1.function
#     #2.Iterable 
#     #and applies the function to each element of iterable and returns an Iterator
#     #usage : we use map function when we have to apply a function to each element of iterable

# #Q.write a function which returns square of a number and use it to calculate square of numbers in a list
# #calculate square of a number in a list

# def square_funct(num):
#     return num**2
# input_list = [1,2,3,4,5]
# output_list = []
# for num in input_list:
#     square_of_num = square_funct(num)
#     output_list.append(square_of_num)
# print(output_list)

#  # list_of_sq_of_num = [expression for item in sequence]  #syntax
# list_of_sq_of_num = [num**2 for num in input_list]
# print(f"Usinf Comprehension :{list_of_sq_of_num}")

# square_using_map_func = map(square_funct,input_list)
# square_using_map_func = list(square_using_map_func)
# print(f"Using map function: {square_using_map_func}")

# #using lambda function inside map
# square_using_map_lambda_func = list(map(lambda num: num**2, input_list))
# print(f"Using map and lambda function: {square_using_map_func}")

# #filter function  #return type is boolean
# list1 = [1,2,3,4,5]
# list2 = []
# def even_func(num):
#     if num % 2 == 0:
#         return num
# for num in input_list:
#     even_nums = even_func(num)
#     list2.append(even_nums)
# print(list2)

# even_num_func = filter(even_func,list1)
# even_num_func = list(even_num_func)
# print(f"Using filter function: {even_num_func}")

# #using lambda function inside filter
# even_num_using_map_lambda_func = list(filter(lambda num: num%2 == 0, list1))
# print(f"Using map and lambda function: {even_num_using_map_lambda_func}")

#reduce,generator and decorator tomorrow

#reduce function
#syntax : reduce(funct,iterable)
#To add all the elements of a lsit 
from functools import reduce
list1 = [1,2,3,4,5]
def add_two_numbers(num1,num2):
    return num1+num2

cumulative_sum = reduce(add_two_numbers, list1)
print(cumulative_sum)


