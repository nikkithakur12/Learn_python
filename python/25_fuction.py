# def add(a,b):
#     return a + b
# result = add(10,20)
# print(result)
# def square(num):
#     return num*num
# answer = square(5)
# print(answer)

# def multiply(a,b):
#     return a * b
# result = multiply(5,4)
# print(result)
# print(result+10)
# print(result-20)
# def subtract(a,b):
#     return a - b
# print(subtract(9,8))
# print(subtract(9,8)+100)
# def average(a,b,c):
#     return (a+b+c)/3
# result = average(20,30,40)
# print(result)
# print(result +5)
# def student_info():
#     return "Nikki",20,"Saharanpur"
# name,age,city = student_info()
# print("Name = ",name)
# print("Age = ",age)
# print("City = ",city)
def multiple_all(*X):
    total = 1
    for i in X:
        total *= i
    return total
result = multiple_all(2,4,3,4,5)
print(result)