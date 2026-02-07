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
    
    @classmethod
    def create_object(cls,title, author_name, price, discount_rate):
        #This method is used to create object
        print("Inside class method",cls.class_variable)
        return cls(title, author_name, price, discount_rate)


    #behaviour or method section
    def calculate_sp(self):
        self.sp = self.price - (self.price * self.discount /100)
        # return sp

#calling class method
book1 = Book.create_object("Python","Rossum",1000,10)
print(book1.title)