#Dictionary represented by {}
# dict1 = {}
# print(dict1)
# print(type(dict1))

student = {
    "name" : "Jeeni",
    "age" : 21,
    "courses" : ["Maths","Physics","Chemistry"]
}
print(f"Student : {student}")

#accessing elements in a dictionary
#accessing using keys
# student_name = student["name"]
# print(f"Name:{student_name}")
# student_courses = student["courses"]
# print(f"Name:{student_courses}")

#accessing using get() method
student_name = student.get("name")
print(f"Name: {student_name}")

student_address = student.get("address","Not available") #if we dont know key available or not
print(f"Address:{student_address}")

#adding new item in the dictionary
student["address"] = "Kathmandu"
print(f"Dictionaary after adding address: {student}")

#updating values
student["address"] = "Bhaktapur"
print(f"Dictionaary after changing address: {student}")


#Dictionary methods
#keys method will return list of all keys
student_keys = student.keys()
print(f"keys: {student_keys}")

#values() method will return list of all the values
student_values = student.values()
print(f"Values: {student_values}")

#items() method will return list of tuples and each tuple contains key and value pair
student_items = student.items()   #for both key and values
print(f"Items : {student_items}")

#looping over key-value pairs
# for x in student.items():
#     key , value = x            #unpacking
#     print(f"{key} : {value}")


#OR this method can be uses
for key, value in student.items():  
    print(f"{key} : {value}")

#Deleting an item from the dictionary
del student["address"]
print(f"Dictionary after deleting address :{student}")    

#looping over two list of same length
list1 = [1,2,3]
list2 = [1,2,3]
for v1,v2 in zip(list1 , list2):
    print(v1 * v2)