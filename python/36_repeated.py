s = "progr"
found = False
for i in s:
    s.count(i)
    if s.count(i)>1:
        print(i)
        found = True
        break
if found == False:
        
    print("No repeated character")


