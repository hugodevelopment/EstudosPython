# Tuple

# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets:

amigos = ("Adonai", "Marcio", "Fernanda", "Lucas", "Lucas")
print(amigos)

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
print(amigos[0])

# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created, 
# But,Since tuples are indexed, they can have items with the same value:
amigos = ("Adonai", "Marcio", "Fernanda", "Lucas", "Lucas", "Adonai")
print(amigos)

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
gols = (1,)
print(gols)


print("--"*15)

print("Access itens")

# We can access tuple items by referring to the index number, inside square brackets:
thistuple = ("apple", "banana", "cherry")
print("Vai ser banana: ",thistuple[1])


# Negative indexing means start from the end 
# -1 refers to the last item, -2 refers to the second last item etc.
print(thistuple[-1])


# Range of Indexes

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# Importante notar que o 5 não faz parte do intervalo
print("Irá de cherry até kiwi",thistuple[2:5])

# By leaving out the start value, the range will start at the first item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("Lembrando que o ultimo item não faz parte ", thistuple[:4])

# By leaving out the end value, the range will go on to the end of the list:

# Example
# This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

tuple = (1, (1, 2, 3))
print(tuple[0])

