s = input("Enter a string:")
vowels = "aeiouAEIOU"
n = ""
c = ""

for i in s:
    if i in vowels:
        n += i
    
    if i not in vowels:
        c += i
print("vowels=",len(n))
print("consonants=",len(c))
    