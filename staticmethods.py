class Book:
    class_variable = "I am class variable"
    #attribute or property section
      #In this section we will define the state/properties of the object
    # title = ""
    # author = ""
    # price = 0.0
    # discount = 0.0

    #constructor
    def __init__(self, title, author_name, price, discount_rate):
        #usage: constructor is used for initialization of object properties
        self.title = title
        self.author = author_name
        self.price = price
        self.discount = discount_rate
        self.sp = None
        print("I am constructor of Book class :",self)

    #behaviour or method section
    @staticmethod
    def add_two_numbers(num1,num2):
        return num1 + num2

    def calculate_sp(self):
        self.sp = self.price - (self.price * self.discount /100)
        # return sp

#calling static method
sum = Book.add_two_numbers(10,20)
print(sum)