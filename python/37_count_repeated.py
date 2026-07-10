# s = input("Enter  a string:")
# found =True
# l = []
# for i in s:
#     count = s.count(i)
#     if s.count(i)>1 and i not in l:
#         print( i ,"=" ,count)
#         l.append(i)
#         found = True
#     elif found == False:
#         print("No repeated character")
s = input("Enter a string:")
freq = {}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
for key in freq:
    print(key,"=",freq[key])        