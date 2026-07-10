# s = int(input("Enter the marks :"))
# name = input("Enter the name:")
# if s >= 90:
#     print("name",name)
#     print("Marks",s)
#     print("Grade A")
# elif s >= 75:
#     print("name",name)
#     print("Marks",s)
#     print("Grade B")
# elif s >= 65:
#     print("name",name)
#     print("Marks",s)
#     print("Grade C")
# elif s >= 50:
#     print("name",name)
#     print("Marks",s)
#     print("pass")
# else:
#     print("fail")
markslist = []
for i in range (1,6):
    marks = int(input("enter the marks"))
    markslist.append(marks)
# print(markslist)
average = 0
for i in markslist:
    average += i
    if (i >= 33):
        passed = True
    if (i <= 33):
        passed = False
if (passed==True):
    print("you are passed")
else:
    print("you are fail")
    
average_marks = average/5
print("your average marks=",average_marks)