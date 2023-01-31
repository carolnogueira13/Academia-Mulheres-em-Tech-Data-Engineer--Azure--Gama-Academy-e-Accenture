
nomes = ["Ana", "maria", 3]

lista_nomes_nova = nomes.copy()  # copia, não aponta para o endereço de memória

print(nomes)
print(lista_nomes_nova)

nomes[0] = "Simba"

print(nomes)
print(lista_nomes_nova)


print(nomes[0])  # Indexação

print(len(nomes))  # Length/tamanho


# Podemos criar uma lista atraves de um range
num_seq = range(0, 10)  # sequencia de 0 a 9
num_list = list(num_seq)
print(num_list)

num_list2 = list(range(3, 20, 3))
print(num_list2)


# Podemos juntar duas listas com o +
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
lista = part_A + part_B  # as listas part_A e part_B se mantém integras, elas são adicionadas em uma terceira
print(lista)


# Podemos também juntar com o extend
part_A.extend(part_B)  # nesse caso a part_A é modifica, e a part_B continua com era antes
print(part_A)


# adicionar num indice numa posição especifica
num_list = [1, 2, 3, 5, 6]
num_list.insert(3, 4)  # insere o '4' na posição 3
print(num_list)


# remover
cidades = ["Londres", "Paris", "NY"]
last = cidades.pop()  # o pop() retira o último item da lista(default), mas ele aceita indice e pode retornar o item
# retirado para uma variavel
print(cidades)
print(last)
cidades.pop(0)  # Retira o elemento da posição 0
print(cidades)

cidades = ["Londres", "Paris", "NY"]
print(cidades)
cidades.remove("Paris")  # remove um item especifico da lista na primeira ocorrência
print(cidades)

# pegar uma sublista
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[2:5])
print(num_list[0:3:3])


# buscar
cidades = ["Londres", "Paris", "NY", "Londres", "Paris"]
print(cidades.index("Paris"))  # Nesse caso a primeira ocorrência de "Paris"
indice = cidades.index("Paris")
print(cidades.index("Paris", indice + 1))  # Nesse caso seria a segunda ocorrência, porque só irá mostrar posições
# acima do indice + 1
