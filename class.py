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
    def calculate_sp(self):
        self.sp = self.price - (self.price * self.discount /100)
        # return sp

#Instantiating the class or creating an object of the class
book1 = Book(title="Python",author_name="Rossum",price=1000,discount_rate=10)
book2 = Book("Java","James Gosling",2000,20)

#Accessing object attributes
#we can access object attributes and methods using dot(.) operator
print(book1.title)
print(book1.author)
print(book1.price)
print(book1.discount)
print(book1.class_variable)
print(book2.class_variable)

book1.calculate_sp()
print("Selling price of book1:",book1.sp)

book2.calculate_sp()
print("Selling price of book1:",book2.sp)
