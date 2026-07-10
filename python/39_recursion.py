def even(n):
    if n == 1:
        return 1
    even(n-1)
    if n%2 == 0:
        print (n)

value = even(11)
    
    