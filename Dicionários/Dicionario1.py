# Dictionaries are another collection type and allow you to map arbitrary keys to values.
# Dictionaries can be indexed in the same way as lists, using square brackets containing keys.


car = {
    'brand':'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
}

a = input(car['brand'])
print(a)


# To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.
nums = {
    1: "one",
    2: "two",
    3: "three",
}
print("Determinando se os valores pertencem ao dicionario utilizando in e not in", "\n")
print("Aqui temos uma pegadinha, three pertence ao dicionário, porém é um valor e não chave, dará False:", "three" in nums)
print("Aqui dará true pq 4 não pertence ao dicionario:", 4 not in nums, "\n")


print("--"*40)

# Podemos utilizar a função dicionario.values() para determinar se um termo faz parte ou não
print("Utilizando a função dicio.values()")
nums = { 1: "one", 2: "two", 3: "three",} 
print("Aqui dará verdadeiro, pois three faz parte do dicionário", "three" in nums.values(), "\n") 

print("--"*40)

print("MÉTODO GET() para acessar os valores")
# Nos dicionários python, a seguir está um método convencional para acessar um valor para uma chave.

dic = {"nome": "Hugo", "idade": 26, "bairro": "Abolição"}
print(dic["nome"])
print("Se eu quiser acessar uma chave que não existe, dará erro dic[numero]")
print("Utilizamos o metodo get() para isso", dic.get("numero","Not Found !"), "\n")


print("--" * 10, "Exercicio Sololearn", "--" * 10)

# You are working on data that represents the economic freedom rank by country.
# Each country name and rank are stored in a dictionary, with the key being the country name.

# Complete the program to take the country name as input and output its corresponding economic freedom rank.
# In case the provided country name is not present in the data, output "Not found".

data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

a = input()
print(data.get(a, "Not found"))


contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
name = input("John")

for x in contacts:
    if name in x:
        print(str(x[0]) + "is" + str(x[1]))
        break
else:
    print("vai a merda")