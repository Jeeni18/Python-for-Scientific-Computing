#tuple is not changable i.e unmutable.for tuple we use () 

#creating a tuple
tuple1 = () #empty tuple
print(tuple1)
print(type(tuple1))

tuple2 = ("Ram",20,50)
first_element = tuple2[0]
last_element = tuple2[-1]
print(f"First element : {first_element}")
print(f"last element : {last_element}")
print(f"first two elements of tuple : {tuple2[:2]}")

for item in tuple2:
    print(item)