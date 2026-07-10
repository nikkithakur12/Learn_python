l = [2,4,5,6,76,8,9,5,56,45,34,6765,564,4646]
smallest = l[0]
largest = l[0]
for i in l:
    if i < smallest:
        smallest = i 
    if i > largest:
        largest = i
print("Largest number =",largest)
print("Smallest =",smallest)
second_smallest = largest
for i in l:
    if i!=smallest and i < second_smallest:
     second_smallest = i
print("Second smallest =",second_smallest)
third_smallest = largest
for i in l:
    if i != smallest and i!= second_smallest and i < third_smallest:
        third_smallest = i
print("Third smallest number =",third_smallest)