n = n_ = int(input('Número: '))
n_divisores = []
primos = []

# def divisores(x,y):
#     if x%y==0:
#         n_divisores.append(y)

while True:
    if n == 1:
        break
    for i in range(n, 0, -1):
        if n%i ==0:
            n_divisores.append(i)
    print(n_divisores)        
    if n_divisores == [n, 1]:
        primos.append(n)
        print(primos)
    n -= 1
    n_divisores = []

print(f'Os números primos presentes no intervalo {n_} - 0 são: ', end='')
for nums in primos:
    if nums != primos[-1]:
        print(nums, end=', ')
    else:
        print(nums, end='.')
# i=0
# while i < len(primos):
#     if i != primos[-1]:
#         print(primos[i], end=',')
#     else:
#         print(primos[i], end='.')
#     i += 1
 