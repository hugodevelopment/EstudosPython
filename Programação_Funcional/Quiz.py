
# 1 What is the result of this code?

# Aqui temos um conjunto
nums = {1, 2, 3, 4, 5, 6}
# Agora temos outro conjunto que faz intersecção com o 1º, isto é, os elementos em comum {1,2,3}
nums = {0, 1, 2, 3} & nums
# Agora aplicamos um filter para separar os elementos maiores que 1
nums = filter(lambda x: x > 1, nums)
# Transformando em lista e verificando seu tamanho
print(len(list(nums)))

# for i in nums:
#     print(i)



def power(x, y):
  if y == 0:
    # Se y == 0 a função se torna 1
    return 1
  else:
    # O retorno sempre é chamado enquanto y == 0
    return x * power(x, y-1)
		
print(power(2, 3))


def func(**kwargs):
  print(kwargs["a"])

func(a = 0, zero = 8)


# nome = "Hello"
# print(nome[:-2])

# i = 0
# j = len(nome) - 1
# while i < len(nome):
#     print(nome[j])
#     i +=1 
#     j -= 1





def spell(txt):
    #your code goes here
    if len(txt) == 0:
        return 
    else:
        print(txt[-1])
        return spell(txt[:-1])
         

txt = "Hello"
spell(txt)    
    

