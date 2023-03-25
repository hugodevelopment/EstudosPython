a = float(input('Valor da ação:'))

b =  int (input ('Quantas pretende comprar:'))

s = a * b

print ('0 total é R$ {}'.format (s)) 

c = float(input('Valor da ação hoje:'))

b =  int (input ('Quantas têm:'))

M = c * b
 
T = M - s 

W = s + T

if (M >= s): 
  
   print('Seu lucro foi de', T)

else: 
   print('Seu prejuízo foi de', T)


print('Seu total é R$', W )
