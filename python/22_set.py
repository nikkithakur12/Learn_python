# s = {1,2,5,7,4}
# s.add(6)
# print(s)
# s = {1,3,5,6,7,4}
# s.update({9,12.45,78})
# print(s)
# s = {1,3,5,6,7,4}
# s.remove(5)
# print(s)
# s = {1,3,5,6,7,4}
# s.discard(5)
# print(s)
# s = {1,3,5,6,7,4}
# x= s.pop()
# print(x)
# print(s)
# s = {3,5,6,7,4}
# x= s.pop()
# print(x)
# print(s)
# numbers = {1,2,3}
# numbers.clear()
# print(numbers)
# numbers = {1,2,3}
# numbers2 = numbers.copy()
# numbers2.add(40)
# print(numbers)
# print(numbers2)
# colors = {"Red","Green"}
# colors2 = colors.copy()
# colors2.add("Yellow")
# print("colors=",colors)
# print("colors2=",colors2)
# set1 = {1,2,3}
# set2 = {3,4,5}
# result = set1.union(set2)
# print(result)
# a = {"Red","Blue"}
# b = {"Blue","Green"}
# c = a.union(b)
# print(c)
# a = {1,2,3,4}
# b = {3,4,5,6}
# print(a.intersection(b))
# colors = {"Red","Blue","Green"}
# colors2 = {"Blue","Black","Green"}
# result = colors.intersection(colors2)
# result2 = colors.union(colors2)
# print(result)
# print(result2)
# a = {10,20,30,40}
# b = {30,40,50}
# c = a.difference(b)
# print(c)
x = {"Apple","Banana","Mango"}
y = {"Banana"}
result = x.difference(y)
print(result)

# a = {10,20,30}
# b = {30,40,50}
# print(a.symmetric_difference(b))
# colors1 = {"Red","Green","Blue"}
# colors2 = {"Blue","Black"}
# result = colors1.symmetric_difference(colors2)
# print(result)
# a = {10,20}
# b = {10,20,30}
# print(a.issubset(b))
# x = {"Red","Blue","Green"}
# y = {"Red","Blue"}
# print(x.issuperset(y))
# a = {10,20}
# b = {30,40}
# print(a.isdisjoint(b))
x = {"Red","Blue","Green"}
y = {"Blue","Green"}
print(x.isdisjoint(y))