string = "hugoeLucas"
string2 = "hmdmsLfdm"

# Converte as strings para conjuntos
set1 = set(string)
set2 = set(string2)

# Encontra a interseção dos dois conjuntos
common_chars = set1.intersection(set2)

# Imprime os caracteres comuns
for char in common_chars:
    print(char)

# Imprime o número de caracteres comuns
print(len(common_chars))