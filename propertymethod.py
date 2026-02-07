class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    #getter methods
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def set_name(self,name):
        self._name = name 
    
    def set_age(self,age):
        self._age = age

person1 = Person("Hari",25)
print(person1.get_name())
print(person1.get_age())

person1.set_name("Ram")
person1.set_age(30)
print(person1.get_name())
print(person1.get_age())




##Using @property decorator for getter and setter methods

class Student:
    def __init__(self,name,age) :
        self._name = name
        self._age = age

    @property
    def name(self):
        #getter method for name
        print("Inside getter method for name")
        return self._name
    
    @property
    def age(self):
        #getter method for age
        print("Inside getter method for age")
        return self._age
    
    @name.setter
    def name(self,name):
        #setter method for name
        print("inside setter method for name")
        self._name = name

    # @age.setter
    # def name(self,age):
    #     #setter method for age
    #     print("inside setter method for age")
    #     self._age = age

student1 = Student("Ram",22)
print(student1.name)
print(student1.age) 

student1.name = "Hari"
# student1.age = 30
print(student1.name)
# print(student1.age) 