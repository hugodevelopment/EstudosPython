# 1) What is the result of this code ?

# temos um tupla
nums = (55, 44, 33, 22)
# a função max é mais externa, que será o max entre min(nums[:2] e modulo de 42)
print(max(min(nums[:2]), abs(-42)))


# 2 Drag and drop from the options below to print only the items in the set "a" that are not in the set "b".
  
a = {1,4,5}
b = {9,5,1}

print(a - b)


# 3 Fill in the blanks to create a list of numbers multiplied by 10 in the range of 5 to 9.

lista = [i *10  for i in range(5,9)]
print(lista)


# nome = "amanda"
# count = 0
# for i in nome:
#     if i == nome[0]:
#         count += 1
# print(count)


def count_letters(word, to_find):
    count = 0
    for char in word:
        if char == to_find:
            count += 1
    return count

print(count_letters("amanda","a"))
