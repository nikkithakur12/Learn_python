# s = "my name is nikki"
# print(s.replace(" ",""))
s = "nikkin"
n = ""
for i in s:
    n = i+n
print(n)
if n in s:
    print("palindrome")
else:
    print("Not palindrome")
    
    