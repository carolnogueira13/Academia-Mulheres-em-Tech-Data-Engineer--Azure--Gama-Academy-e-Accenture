maior = 0
for i in range(5):
    valor = int(input("Digite um número: "))
    if i == 0:
        maior = valor
    elif valor > maior:
        maior = valor
print(maior)
