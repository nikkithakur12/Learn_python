
# numbers =[]

# for i in range (0,5):
#     a = int(input("Enter the number:"))
#     numbers.append(a)
# print(numbers)
# count = 0
# for i in numbers:
#         if i%2==0:
#             print(i)
#             count +=i
# print("count=",count)
    
# numbers = []
# for i in range(5):
#     num = int(input ("Enter the number:"))
#     numbers.append(num)
# print(numbers)
# largest = numbers[0]
# smallest = numbers[0]
# for i in numbers:
#     if i > largest:
#         largest= i
#     if i < smallest:
#         smallest = i
           
# print("largest",largest)
# print("smallest",smallest)

# string = input("Enter a string:")
# count = 0
# for i in string:
#     if i=="a" or i == "e" or i == "i" or i == "o" or i == "u" :
#         print(i)
#         count += 1
# print("count",count)

# numbers = []
# odd_numbers = []
# for i in range(0,5):
#     num = int(input("Enter the number:"))
#     numbers.append(num)
# print(numbers)

# for i in numbers:
#     if i%2!=0:
#         odd_numbers.append(i)
    
# print("odd list =",odd_numbers)
        
# print("count=",len(odd_numbers))     

# numbers = []
# for i in range(0,5):
#     num = int(input("Enter the number:"))
#     numbers.append(num)
# largest = numbers[0]
# print(numbers)
# for i in numbers:
#     if i > largest:
#         largest = i 
        
# print("largest",largest)
# second_largest = -1
# for i in numbers:
#     if i != largest and i > second_largest:
#         second_largest = i
# print("Second Largest:",second_largest)
# numbers = []
# even_numbers = []
# odd_numbers = []
# for i in range(10):
#     num = int(input("Enter the number:"))
#     numbers.append(num)
# print(numbers)
# even_largest = numbers[0]
# odd_largest = numbers[0]      
# for i in numbers:
#     if i%2 == 0 :
#         even_numbers.append(i)
#     if i %2!=0 :
#         odd_numbers.append(i)
# for i in even_numbers:
#     if i >even_largest:
#         even_largest = i
# for i in odd_numbers:
#     if i>odd_largest:
#         odd_largest=i
        
# print("even list=",even_numbers)
# print("largest number=",even_largest)
# print("odd list=",odd_numbers)
# print("largest number=",odd_largest)
# print("even list count=",len(even_numbers))
# print("odd list count=",len(odd_numbers))

       
        
# numbers = []
# positive_numbers = []
# negative_numbers = []

# for i in range(10):
#     num = int(input("Enter the numbers:"))
#     numbers.append(num)
# print(numbers)

# for i in numbers:
#     if i > 0:
#         positive_numbers.append(i)
#     if i < 0 :
#         negative_numbers.append(i)
# largest_positive = numbers[0]
# second_largest_positive = -1
# for i in positive_numbers:
#     if i>largest_positive:
#         largest_positive = i
# for i in positive_numbers:
#     if i != largest_positive  and i >second_largest_positive:
#         second_largest_positive = i
        
        
        
# print("Positive Numbers=",positive_numbers)
# print("Largest Positive Numbers=",largest_positive)
# print("Second largest positive number=",second_largest_positive)
# for i in negative_numbers:
#     if i<smallest_negative:
#         smallest_negative = i


       
# print("Positive Numbers=",positive_numbers)
# print("Negative Numbers=",negative_numbers)
 
# print("Largest Positive Numbers=",largest_positive)
# print("Smallest Negative Numbers=",smallest_negative)

numbers = []
for i in range (5):
    num = int(input("Enter the number:"))
    numbers.append(num)
print("numbers=",numbers)
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] == numbers[j] and i!=j and i < j :
          print("Duplicate=",numbers[i])
          found = True
if found == False:
    print("No duplicate found")
        