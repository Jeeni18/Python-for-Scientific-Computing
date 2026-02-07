#CALCULATION
"""
In this program various opeartions are performed(like addition,substraction,multiplication,division,etc) in two numbers of user's choice.
"""
num1 = input("Enter first number :")
num2 = input("Enter second number :")
num1 = int(num1)    #type casting
num2 = int(num2)    #type casting
print("choose an operation to perform","\n1.Add","\n2.Substract","\n3.Divide","\n4.Multiply","\n5.Power")
operation = input("Enter choice :")
operation = int(operation)    #type casting
if operation == 1:
   print("Sum =",num1 + num2)

elif operation == 2:
   print("Subtraction result =",num1 - num2)

elif operation == 3:
   print("Division result =",num1 / num2)   

elif operation == 4 :
   print("Product =",num1 * num2)

elif operation == 5 :
   print("Result =",num1 ** num2)      

else :
   print("Invalid choice")