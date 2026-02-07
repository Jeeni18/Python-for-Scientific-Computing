class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print("I am displaying person info")
        print("Name :",self.name)
        print("Age:",self.age)
        print("Address:",self.address)

class Student(Person):
    def __init__(self, name, age, address,university):
        super().__init__(name, age, address)
        self.university = university
   
   #person class has same method display_info().so this will override that method 
   #to call the overrided method of python class
    def display_info(self):
        super().display_info()
        print("I am displaying student info")
        print("Name :",self.name)
        print("Age:",self.age)
        print("Address:",self.address)
        print("university:",self.university)
    
    def student_method(self):
        print("I am a student and I can study")
       
#creating objects of subclass
student1 = Student("Hari",25,"Bhaktapur","Tribhuwan University")
student1.display_info()
# student1.person_method()      #correct this error
student1.student_method()