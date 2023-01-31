import sys

lista = []

for i in range(1,4):
    valor = int(sys.argv[i])
    lista.append(valor)

lista.sort(reverse=True)

print("Números em ordem decrescente: ")
for i in lista:
    print(i, end=" ")
