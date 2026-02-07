#QUES 1 CALCULATE AVERAGE MARKS
# avg = 0
# marks=[10,20,30,40,50,60]
# for i in range(len(marks)):
#     avg = avg + marks[i]
# print(f"average marks : {avg/len(marks)}")    

#QUES 2 MULTIPLICATION TABLE
# num = input("Enter the number for multiplication table :")
# num = int(num)
# for i in range(1,11):
#      mul = i * num
#      print(f"{num} * {i} = {mul}")

# #QUES 3 palindrome or not
# x = int(input("Enter a number to check palindrome or not :"))
# temp = x
# new = 0
# while x>0:
#     rem = x % 10
#     new = new * 10 +rem
#     x = x // 10
# if temp == new:
#     print("The number is a palindrome.")
# else:
#     print("The number is not a palindrome")


#QUES 4 TO FIND THE GREATEST NUMBER FROM A LIST OF NUMBERS
# lst = []
# n = int(input("Enter the number of elements in the list :"))
# for i in range(n):
#     num = int(input("Enter a number :"))
#     lst.append(num)
# print(f"The List : {lst}")
# ele1 = lst.pop()
# for i in range(n-1):
#     ele2 = lst.pop()
#     if ele2>ele1:
#         ele1=ele2
# print(f"The greatest bumber : {ele1}")


#QUES 5 TO FIND THE PEAK ELEMENT
# lst = []
# n = int(input("Enter the number of elements in the list :"))
# for i in range(n):
#     num = int(input("Enter a number :"))
#     lst.append(num)
# print(f"The List : {lst}")
# for i in range(n-2):
#     if (lst[i+1]>lst[i] and lst[i+1]>lst[i+2]):
#         print(f"Peak={lst[i+1]}")

#ques 6 TO COUNT THE NUMBER OF VOWELS IN A STRING

# word = input("Enter a string :")
# vowels = "aeiouAEIOU"
# count = 0
# for char in word:
#     if char in vowels:
#       count = count + 1
# print(count)


#ques 7 TO FIND THE SUM OF DIGITS IN AN INTEGER
# num = input("Enter a number :")
# new = 0
# for digit in num:
#     new = new + int(digit)
# print(f"The sum of digits in {num} : {new}")

# #ques 8 GIVE A ROMAN NUMERICAL(I=1,V=5,X=10,L=50,C=100,D=500,M=1000) AND CONVERT IT TO AN INTEGER.
# num = input("Enter a roman numerical: ")

# total = 0
# prev_value = 0

# for digit in reversed(num):
#     if digit == "I":
#         value = 1
#     elif digit == "V":
#         value = 5
#     elif digit == "X":
#         value = 10
#     elif digit == "L":
#         value = 50
#     elif digit == "C":
#         value = 100
#     elif digit == "D":
#         value = 500
#     elif digit == "M":
#         value = 1000
    
#     if value < prev_value:
#         total -= value
#     else:
#         total += value
    
#     prev_value = value

# print(f"The integer value of {num} is {total}")

    

#ques 9 Balanced parenthesisi checking
# str1 = input("Enter a string")
# for i in range(len(str1)):
#     if "()" in str1:
#         str1 = str1.replace("()","")
#     if "{}" in str1:
#         str1 = str1.replace("{}","")
#     if "[]" in str1:
#         str1 = str1.replace("[]","")    
# if str1 == "" :
#     print(True)
# else:
#     print(False)    

#ques 10 t find the frequency of character
# word = input("Enter a string")
# lst = [" "]
# for i in word:
#     count = 0
#     if i not in lst:
#         for j in word:
#             if i == j:
#                 count = count + 1   
#     else:
#         continue
#     lst.append(i)
#     print(f"The frequency of {i} : {count}")

#or
# word = input("Enter a string: ")
# frequency = {}
# for char in word:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1
# for char, count in frequency.items():
#     print(f"The frequency of {char} : {count}")


#ques11
# grades_dict = {
#     "Alice":{"Maths":90, "Science":85,"Literature":88},
#     "Bob":{"Maths":78, "Science":82,"Literature":80},
#     "charlie":{"Maths":92, "Science":91,"Literature":94},
# }

# for key,value in grades_dict.items():
#     # print(key , value)
#     v1 = 0
#     for k ,v in value.items():
#         v1 = v1 + v
#         pass
#     print("The percentage of",key,v1*1/3 )