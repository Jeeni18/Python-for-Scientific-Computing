#SYNTAX OF FOR LOOP
# sequence = {}
# for item in sequence:
#     #body of for loop
#     pass
# fruits = {"apple","banana","mango"}
# for fruit in fruits:
#     print(fruit)

 #range() function returns sequence of values within that range   
# for i in range(5):
#     print(i)
# for i in range(2,10,2):
# #     print(i)
# fruits = {"apple","banana","mango"}
#  #for fruit in fruits:
# #      print(fruit)

# for i in range(len(fruits)):
#     print(i)


#break statement
# for i in range(10):
#     if i==5:
#         break
#     print(i)

#continue statement
# for i in range(10):
#     if i==5:                   #if this expression is true this one iteration is skipped
#         continue
#     print(i)

#enumerate() function (used for indexing)
# fruits = ["apple","mango","banana"]
# for idx, fruit in enumerate(fruits):
#     print(f"{idx}:{fruit}")