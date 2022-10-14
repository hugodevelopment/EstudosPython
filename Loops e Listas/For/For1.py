# A sequência começa com o número inicial.
# O termo seguinte da sequência é o anterior, somado a razão. E assim sucessivamente.

# Vamos super que temos o termo inicial:
# a1 = 1

# E razão:
# r= 3

# A sequência (PA) é:
# a1 = 1
# a2 = a1 + r = 1 + 3 = 4
# a3 = a2 + r = 4 + 3 = 7
# a4 = a3 + r = 7 + 3 = 10



r = 3

for i in range (2):
    a1 = 0
    if(i == 1):
        a1 = a1 + i
        a2 = a1 + r
        a3 = a2 + r
        a4 = a3 + r
        print("a2 com if = ", a2) 
        print("a3 com if = ", a3)
        print("a4 com if = ", a4)

for i in range(2):
    a1 = 0
    while(i == 1):
        a1 = a1 + i
        a2 = a1 + r
        a3 = a2 + r
        a4 = a3 + r
        i += 1
        print("a2 com while = ", a2) 
        print("a3 com while = ", a3)
        print("a4 com while = ", a4)
