def count(n):
    if n == 0:
        return 
    count(n-1)
    print(n)
count(11)

# def fibo(n):
#     if n== 0:
#         return 0
    
#     elif n == 1:
#         return 1
#     else :
#         return fibo(n-1)+fibo(n-2)
    
# print(fibo(5))

# def reverse(s):
#     if s == "":
#         return ""
#     return reverse (s[1:])+s[0]
# print(reverse("Nikki"))