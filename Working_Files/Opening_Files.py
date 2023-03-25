# file = open("/usercode/files/books.txt")

# for line in file.readlines():
#     print(line)
    
# file.close()


# # Primeiro ele escreve no arquivo
# file = open("newfile.txt", "w")
# file.write("This has been written to a file")
# file.close()

# # Depois ele le o novo arquivo com novos dados
# file = open("newfile.txt", "r")
# print(file.read())
# file.close()

# # Aqui eu adiciono um novo livro no arquivo
# file = open("/usercode/files/books.txt", "a")
# # Livro adicionado
# file.write("\nThe Da Vinci Code")
# file.close()
# # aqui é lido
# file = open("/usercode/files/books.txt", "r")
# print(file.read())
# file.close()


# n = int(input())

# file = open("numbers.txt", "w+")
# #your code goes here
# for i in range(1,n+1):
#     file.write(str(i))
# file.close()    

# f = open("numbers.txt", "r")
# print(f.read())
# f.close()

string = 'Naruto e Sasuke'
j=0
new_word = ""
while j < 3:
   word = string.split()
   new_word += word[j][0]
   j+=1
print(new_word)

# print(j)   
# print(word[j][0])
# list = [string.split('-')[0][0] for i in string]
# print(list)

l = ['element1\t0238.94', 'element2\t2.3904', 'element3\t0139847']
list = [i.split('\t', 1)[0][0] for i in l]
print("".join(list))
print(list)

