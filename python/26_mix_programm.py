# l = [1,2,3,4,5,6,7]
# def even(a):
#     if a%2==0:
#         return True
#     return False
# onlyEven = filter(even,l)
# print(list(onlyEven))

# def check_even_odd(nums):
#     even =[]
#     odd = []
#     for i in nums:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return even,odd
# l = [2,4,6,8,5,7,9]
# even,odd = check_even_odd(l)
# print("even = ",even)    
# print("odd = ",odd)    
# n = int(input("Enter the number:"))
# count = 1
# for i in range(1,n+1):
#     count *= i
    
# print("Factorial =", count)
# s = input("Enter a string:")
# rev = ""
# for i in s:
#     rev = i + rev
# print(rev)
    
# s = input("Enter a string:")
# count = 0
# vowels = "aeiouAEIOU"
# for i in s:
#     if i in vowels:
#         count += 1
# print("Total Vowels  :",count)
# l = [1,2,6,7,89,56,765,453,5666556]
# max = l[0]
# for i in l:
#     if i >= max:
#         max = i
# print("Max value =", i)
# l = [1,2,3,4,5,3,2,4,5,6,7,8,98]
# my_list = []
# for i in l:
#     if i not in my_list:
#         my_list.append(i)
# print(my_list)
# l = [1,2,3,4,5,3,2,4,5,6,7,8,98]
# my_list = []

# for i in l:
#     if i not in my_list:
#         my_list.append(i)
# print("Unique list:",my_list)
# for i in my_list:
#     freq  = 0
#     for j in l:
#         if j == i: 
#            freq += 1
#     print(i, "=" , freq)                


