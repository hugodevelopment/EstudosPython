# Expressões matemáticas em Python podem obedecem as 
# mesmas regras de sinal com as quais estamos acostumados:

expressao = (1 * -2 * 3) * (-4 * 5 * -6)
print(expressao)

# Regras de Precedência
# Quando criamos uma expressão em Python, existe em uma ordem em que as subexpressões são avaliadas. 
# Essa ordem é determinada por algo que chamamos de precedência de operadores.

# 1º Operador é a potência(**), 2º multplicação(*) e divisão(%) (inteira / ou decimal //) e 3º soma(+) e subtração (-)

# Ex1: Qual é o valor da expressão abaixo? 
expressão1 = 16 - 2 * 5 // 3 + 1

# 1º Fazemos a multiplicação por aparecer antes lendo a equação da esquerda para a direita
Operação_1 =  (2 * 5)
# 2º Fazemos a divisão após realizar a multiplicação (2*5) que chamamos de operação_1
Operação_2 =  (Operação_1 // 3)
# 3º  Após fazer a divisão subtraimos de 16 por ser mais a esquerda
Operação_3 =  (16 - Operação_2)
# 4º Para finalizar somamos a operação_3 com o 1 e chamamos de operaçã0_4
Operação_4 = Operação_3 + 1
# 5º Printando nosso resultado
print("Nosso calculo", Operação_4)


print("Resultado expressão",expressão1)

