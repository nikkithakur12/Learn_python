l =  list(map(int,input("Enter Numbers:").split()))
print("List =",l)
even = []
odd = []
for i in l:
    if i%2==0:
        even.append(i)
    if i%2!=0:
        odd.append(i)
even_smallest = even[0]
for i in even:
    if i < even_smallest:
        even_smallest = i
odd_smallest = odd[0]
for i in odd:
    if i < odd_smallest:
        odd_smallest = i
even_largest = even[0]
for i in even:
    if i >even_largest:
        even_largest = i
odd_largest = odd[0]
for i in odd:
    if i > odd_largest:
        odd_largest = i
    
print("Odd Numbers =",odd)       
print("Even Numbers =",even)
print("even smallest =",even_smallest)
print("odd smallest =",odd_smallest)
print("even largest =",even_largest)
print("odd largest =",odd_largest)


