l = [1,1,2,3,4,5,6,5,4,6,7,8,9]
new_list = []
for i in l:
    if i not in new_list:
        new_list.append(i)
print("Unique value =",new_list)
for i in new_list:
    count = 0
    for j in l:
        if j == i:
            count += 1
    print(i,  "=" ,count)
                    
    