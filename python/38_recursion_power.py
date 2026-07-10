def power(x,n):
    if n == 0:
        return 1
    return x * power(x,n-1)
value = power(2,5)
print(value)
    