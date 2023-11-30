string = "hugosLuca"
string2 = "hmsmLfdm"
count = 0
# for i in string:
#     for x in string2:
#         if i == x:
#             print(x)
#             count += 1
# print(count)

# i = 0
# j=0
# while i < len(string):
#    while j < len(string2):
#        if string2[i] == string[j]:
#          print(string[i])
#     j+= 1
# i+=1

i=0
while i < len(string):
    j= 0
    while j < len(string2):
        if string[i] == string2[j]:
            print(string[i])
            count += 1
        j += 1
    i += 1
print(count)




