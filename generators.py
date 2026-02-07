#generators
#returns iterator
#same as regular function but instead of return there is yield

#generator definition
def my_generator(num):
    for i in range(num):
        yield i

#calling generator function
my_iterator = my_generator(5)
print(my_iterator)

#accessing generator elements using next() method
print(next(my_iterator))
print(next(my_iterator))

#accessng generator eleemnts using for loop
for num in my_iterator:
    print("Using loop:",num)

#creating generator using generator expression
my_generator_from_gen_expr = (i for i in range(5))
for val in my_generator_from_gen_expr:
    print(f"using generator expression:{val}")