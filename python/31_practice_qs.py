l   = [2,3,4,5,6,7,8,9,54,67,32,54,21,51,87]
count = 0
for i in l:
    if i < 2:
        continue
    prime = True
    
    for j in range(2,i):
        if i%j == 0:
            prime = False
            break
    if prime:
         count += 1
    
print(count)