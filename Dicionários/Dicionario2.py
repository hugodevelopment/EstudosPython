"""O dicionário Python é uma coleção não ordenada de itens. Cada item de um dicionário tem um par chave/valor.
Os dicionários são otimizados para recuperar valores quando a chave é conhecida. """

#Criar um dicionário é simples, só precisa usar {} com chaves e valores:
meu_dicionario = {"Nome":"Hugo", "Idade":"26", "Cidade": "Rio de Janeiro"}
print(meu_dicionario) 

#Acessando um item no dicionário, no caso o valor Hugo com a chave Nome
valor = meu_dicionario["Nome"]
print(valor)

#Adicionando novos valores no dicionário:
meu_dicionario["email"] = "hugoalves@gmail.com"
print(meu_dicionario)

#Verificando se os valores estão no dicionário
if "Idade" in meu_dicionario:
    print("Idade está no dicionário")
else:
    print("Não está") 

#Loops no dicionário para percorrer as chaves e os valores no dicionário
for key, value in meu_dicionario.items():
    print(key,value) 

#Percorrendo as chaves como por exemplo Nome
for key in meu_dicionario.keys():
    print(key)

#Percorrendo os valores como por exemplo Hugo 
for value in meu_dicionario.values():
    print(value)              

#Criando uma cópia do um dicionário, mas é importante se atentar para não criar modificar o dicionário original
#meu_dicionario_copy = meu_dicionario

"""Incluindo a chave Profissao e o valor Desenvolvedor
meu_dicionario_copy["Profissao:"] = "desenvolvedor"

#Na hora de printar, ambos serão modificados: O original e a cópia
print(meu_dicionario_copy)
print(meu_dicionario)"""

#Para que isso não ocorre, fazemos:
meu_dicionario_copy = meu_dicionario.copy()
#Adicionamos uma nova chave e valor apenas para a cópida
meu_dicionario_copy["Profissao:"] = "desenvolvedor"
#Será modificado
print(meu_dicionario_copy)
#Não será modificado
print(meu_dicionario)

#Criando novos dicionários
Dados_Notas = {"Nome": "Lucas", "Nota1": 10, "Nota2": 9, "Nota3": 5}
#Printando sem as média e situação
print(Dados_Notas)
Dados_Media = {"Media:": 8, "Situação:": "Aprovado"}
#Atualizando os dados da média e situação no dicionário das notas
Dados_Notas.update(Dados_Media)
#Printando com a média e situação
print(Dados_Notas)

#Delentando chaves e valores

#Podemos deletar utilizando o metodo pop e especificando a chave
Dados_Notas.pop("Nota3")
#Vai printar sem a Nota 3
print(Dados_Notas)

#Podemos também dele o último item do dicionário com o pop item
Dados_Notas.popitem()
#Vai deletar a chave situação
print(Dados_Notas)