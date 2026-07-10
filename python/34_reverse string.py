s = "dad"
name = ""
for i in s:
    name = i + name 
    if s == name:
        passed = True
    else:
        passed = False
if passed == True:
    print("Palindrome ,",name,"=",s)
else :
    print("Not palindrome ,",name,"!=",s) 
    

print(name)