soma = 0
for i in range(5):
    valor = int(input("Digite um número: "))
    soma += valor
media = soma/(i+1)
print(f"A soma dos valores é {soma} e a média é dos valores é {media}")