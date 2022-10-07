# Expressões matemáticas em Python podem obedecem as 
# mesmas regras de sinal com as quais estamos acostumados:

expressao = (1 * -2 * 3) * (-4 * 5 * -6)
print(expressao)

# Regras de Precedência
# Quando criamos uma expressão em Python, existe em uma ordem em que as subexpressões são avaliadas. 
# Essa ordem é determinada por algo que chamamos de precedência de operadores.

# 1º Operador é a potência(**), 2º multplicação(*) e divisão(%) (inteira / ou decimal //) e 3º soma(+) e subtração (-)

# Ex1: Qual é o valor da expressão abaixo? 
expressão1 = 16 - 2 * 5 / 3 + 1

Operação_1 =  (2 * 5)
Operação_2 =  (Operação_1 // 3)
Operação_3 =  (16 - Operação_2)
Operação_4 = Operação_3 + 1
print(Operação_4)


print(expressão1)

