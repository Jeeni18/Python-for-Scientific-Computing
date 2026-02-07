#CREATING A LIST
#LIST IS REPRESENTED BY SQUARE BRACKETS
#LISTS ARE MUTABLE

# mylist = []   #empty list
# print(mylist)
# print(type(mylist))

fruits = ["apple","mango","banana","papaya"]
print(f"Length of fruits list is :{len(fruits)}")
print(fruits)

# #ADDING AN ELEMNT IN LIST(at last position)
# fruits.append("orange")
# print(f"Fruits after appending orange : {fruits}")

# #ADDING AN ELEMNT IN LIST(at any position,indexing starts from 0)
# fruits.insert(1,"guava")
# print(f"Fruits after inserting guava at position 1 : {fruits}")

# #REMOVING ELEMENT FROM THE LIST( by returning it)
# popped_element = fruits.pop()
# print(f"Popped elemnt is: {popped_element}")
# print(f"List of fruits after popping: {fruits}")

# #REMOVING ELEMENT FROM THE LIST(from any position,doesnot return it)
# fruits.remove("banana")
# print(f"List of fruits after removing: {fruits}")

# #CONCATENATION OF LIST
# list1 = [1,2,3]
# list2 = [4,5,6]
# list3 = list1 + list2
# print(f"List after concatenation: {list3}")

# #CONCATENATION USING EXTEND FUNCTION
# listA = [1,2,3]
# listB = [4,5,6]
# listA.extend(listB)
# print(f"new list: {listA}")

# #SLICING OF LIST
# list1 = [0,1,2,3,4,5,6]
# first_element = list1[2]
# sublist = list1[0:2]
# print(f"sublist1: {sublist}")
# sublist = list1[:3]
# print(f"sublist2: {sublist}")
# sublist = list1[2:]
# print(f"sublist3: {sublist}")
# sublist = list1[0:7:2]   #STEPSIZE 2
# print(f"sublist4: {sublist}")

# #NEGATIVE INDEXING(indexing start from end(-1,-2...))
# last_element = list1[-1]    #-1 is last element
# print(f"Last element : {last_element}")
# second_last_element = list1[-2]    #-2 is last element
# print(f"Last element : {second_last_element}")
# sublist = list1[-5:-2]
# print(f"sublist5: {sublist}")
# sublist = list1[-3:6]
# print(f"sublist6: {sublist}")

# reverse_list = list1[::-1]     #TO  REVERSE THE LIST
# print(f"Reversed list: {reverse_list}")

# #NESTED LIST
# nested_list = [[1,2],[3,4,5],6]
# print(f"length of list :{len(nested_list)}")
# print(f"First element of list: {nested_list[0]}")
# print(f"First element of list within list: {nested_list[0][0]}")
# print(f"Second element of list within list: {nested_list[0][1]}")
