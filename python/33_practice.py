s = input("Enter a string :")
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
count = 0 
for i in s:
    
    
    if i == consonants:
        
        count += 1
print(count)
vowels ="aeiouAEIOU"
count = 0
for i in s:
    if i not in vowels:
        count += 1
print(count)