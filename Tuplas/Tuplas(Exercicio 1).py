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



'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------'

contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

while True:
    name = input("Digite um nome")
    
    def contatos(x):
        if x[0] == name:
            print("Esta na lista ", name, " com idade ", x[1])
            
    for x in contacts:
        contatos(x)
    
    op = int(input("Deseja continuar 1 para sim"))
    if op != 1:
        print("Valeu!")
        break


