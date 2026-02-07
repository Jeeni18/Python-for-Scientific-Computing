#type: ignore
# string1 = "Hello world"
# print(string1)
# string2 = 'Hello world'
# print(string2)

# #accessing characters in a string
# first_char = string1[0]
# last_char = string2[-1]
# print(f"First character : {first_char}")
# print(f"Last character : {last_char}")

# #looping in string
# for characters in string1:
#     print(characters)

# #string concatenation
# Name = "Jeeni"
# Surname = "Shrestha"
# full_name = Name+" "+Surname
# print(full_name)

# #string slicing
# print(f"Name :{full_name[:6]}")
# print(f"Surname :{full_name[6:]}")


#split method
#split()   #makes list by removing delimeter

str5 = "Hello world"
list1 = str5.split()    #space is taken as default delimeter
print(list1)
list1 = str5.split("o")    #o is taken as default delimeter
print(list1)

#strip() removes unnecessary space
str6 = "    Hello      "
str7 = str6.strip()
print(str7)

#upper() and loswer()
print(str7.upper())
print(str7.lower())