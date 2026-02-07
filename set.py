#elements cannot be repeated in set.represented by curly braces{}
#set is used when there are a lot of repeatitons of same element and it needs to be removed
#it is mutable

#set1 = {}              #if given in such way,it is dictionary not set
# set1 = set()
# print(set1)
# print(type(set1))

# set2 = {1,2,3,4,5}
# print(set2)
# print(type(set2))

# #Adding element in set
# set2.add(6)
# print(set2)

# #removing element in set
# set2.discard(3)        #doesnot throw error if there is not given element
# print(set2)

# set2.remove(5)        #throws an error if there is not given element
# print(set2)

# #operations on set
# set3 = {1,2,3,4}
# set4 = {3,4,5,6}

# intersection_set = set3.intersection(set4)
# print(f"Intersection set : {intersection_set}")

# union_set = set3.union(set4)
# print(f"Union Set : {union_set} ")

# difference_set = set3.difference(set4)
# print(f"Difference set = {difference_set}")

#use case of set
list1 = ["Ram","Hari","Sita","Jeeni"]
list2 = ["Hari","Jeeni"]

set1 = set(list1)
set2 = set(list2)
common_names = set1.intersection(set2)
common_names = list(common_names)
print(common_names)
