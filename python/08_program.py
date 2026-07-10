a = int(input("Enter a number:"))
factorial = 1
for i in range(1,a+1):
    if i == 5 :
         continue
    factorial *= i
    print(factorial)