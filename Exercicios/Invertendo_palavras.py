# def inverter_palavra(x):
#     nova_palavra=""
#     for i in range(0, len(x), 2):
#         if i + 1 < len(x):
#             nova_palavra += x[i+1] + x[i]
#             # print(i,nova_palavra)
#     return nova_palavra    
        
# print(inverter_palavra("mexico"))       

# def inverter_palavra(x):
#     nova_palavra=""
#     for i in range(0, len(x), 2):
#         if i + 1 <= len(x):
#             nova_palavra += x[i+1] + x[i]
#             print(i,nova_palavra)
#         else:
#             nova_palavra += x[i]
#             print(nova_palavra, "no else")    
#     return nova_palavra    
        
# print(inverter_palavra("mexico"))  



def inverter_palavra(x):
    nova_palavra = ""
    for i in range(0, len(x) - 1, 2):
        nova_palavra += x[i+1] + x[i]
        print(nova_palavra)
    if len(x) % 2 != 0:
        nova_palavra += x[-1]
    return nova_palavra

print(inverter_palavra("mexico"))