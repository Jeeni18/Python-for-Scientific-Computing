# list_of_num = [1,2,3]
# list_of_sq_of_num = []
# for i in list_of_num:
#     list_of_sq_of_num.append(i*i)
# print(list_of_sq_of_num)

# #calculate square of number using list comprehension
# list_of_num = [1,2,3]
# # list_of_sq_of_num = [expression for item in sequence]  #syntax
# list_of_sq_of_num = [num**2 for num in list_of_num ]
# print(list_of_sq_of_num)


# #for square of even num only using list comprehension
# # list_of_sq_of_num = [expression for item in sequence if condition] #syntax 
# list_of_num = [1,2,3]
# list_of_sq_of_num = [num**2 for num in list_of_num if num % 2 == 0]
# print(list_of_sq_of_num)


#set of square w/o comprehension
set_of_num = {4,5,6}
set_of_sq_of_num = set()
for i in set_of_num:
    set_of_sq_of_num.add(i**2)
print(set_of_sq_of_num)

#set of square of num using comprehension
set_of_num = {4,5,6}
set_of_sq_of_num = {num**2 for num in set_of_num}
print(set_of_sq_of_num)

#set of square of num using comprehension for even num only
set_of_num = {4,5,6}
#set_of_sq_of_num = set()
set_of_sq_of_num = {num**2 for num in set_of_num if num % 2 == 0}
print(set_of_sq_of_num)


#dictionary comprehension
#to swap key and value w/o using dictionary comprehension
ori_dict = {"a":1 , "b":2 , "c":3}
swap_dict = {}
for key,value in ori_dict.items():
    swap_dict[value] = key
print(swap_dict)

#to swap key and valueusing dictionary comprehension
#new_dict = {key : expression for item in sequence.items() if condition}
ori_dict = {"a":1 , "b":2 , "c":3}
swap_dict = {}
swap_dict = {value:key for key,value in ori_dict.items()}    #for swapping
print(swap_dict)

#square even value only
ori_dict = {"a":1 , "b":2 , "c":3}
swap_dict = {key:value**2 for key,value in ori_dict.items() if value % 2 == 0}    #for swapping
print(f"New: {swap_dict}")