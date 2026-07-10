l = [2,4,5,6,87,-1,-4,5,6,6,2,4,5,43,67,45,23]
my_list = []
for i in l:
    if i not in my_list:
        my_list.append(i)
for i in my_list:
    count = 0
    for j in l:
        if i == j:
            count += 1
    print(i,"=",count)

        