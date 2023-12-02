
# A função para calcular o mdc, nesse caso ate que y seja diferente de 0
def __mdc_(x,y):
    while(y):
        x,y=y,x%y
    return x

# Aplica a função mdc na lista
def mdc(nums):
    # se a lista tiver tamanho 2, 2 elemntos, aplica a função nos 2 elementos
    if len(nums) == 2:
        return __mdc_(nums[0], nums[1])
    # Caso seja maior
    else:
        # 1º calcula o mdc entre 2 numeros
        mdc_val = __mdc_(nums[0], nums[1])
        # substitui o 1º valor da lista pelo mdc
        nums[0] = mdc_val
        print(nums)
        # deleta  o 2º valor da lista
        del nums[1]
        print(nums)
        # retorna a lista
        return mdc(nums)
 
print(mdc([30, 54, 50]))
