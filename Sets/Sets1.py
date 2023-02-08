# Sets are similar to lists or dictionaries.
# They are created using curly braces, and are unordered, which means that they can't be indexed.

# Due to the way they're stored, it's faster to check whether an item is part of a set using the in operator, rather than part of a list.

num_set = {1, 2, 3, 4, 5}
print(3 in num_set)

letters = {"a", "b", "c", "d"}
if "e" not in letters:
  print("Faz parte",1)
else: 
  print("Faz parte",2)

# Sets cant contain duplicate elements

'-------------------------------------------------------------------------------------------------------------------'

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
# Adicionando um novo elemento no conjunto
nums.add(-7)
# Removendo um elemento do conjunto
nums.remove(3)
print(nums)
'-------------------------------------------------------------------------------------------------------------------'

# Union of Two Sets
# The union  | of two sets A and B include all the elements of set A and B.

a = {1,3,4}
b = {2,5,6}

print("União dos conjuntos: ", a | b )

# The intersection & of two sets A and B include the common elements between set A and B.

a = {1,4,5}
b = {5,7,1}

print("Interseção dos conjuntos ", a & b)

# The difference - between two sets A and B include elements of set A that are not present on set B.
a = {3,5,7}
b = {2,5,3}
print("diferença dos conjuntos ", a - b)

# The symmetric difference between two sets A and B includes all elements of A and B without the common elements.

a = {1,3,4}
b = {2,3,8}

print("Simetria dos conjuntos", a ^ b)


skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

print(list(skills & job_skills)[0])


for i in skills:
    for x in job_skills:
        # print(i,x)
        if i == x:
            print("Bate certinho", x, i)



