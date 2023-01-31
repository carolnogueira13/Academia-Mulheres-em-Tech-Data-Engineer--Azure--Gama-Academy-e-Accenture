# iterar em uma lista
nomes = ["ana", "miguel"]
for nome in nomes:
    print(nome)

# iterar pelos caracteres numa string
for letra in "gato":
    print(letra)

# exemplos com range
for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)

# break
nomes = ["ana", "camis", "talita"]
for x in nomes:
    print(x)
    if x == "camis":
        break

print()
for x in nomes:
    if x == "camis":
        break
    print(x)

# continue
nomes = ["ana", "camis", "talita"]
for x in nomes:
    if x == "camis":
        continue
    print(x)

# pass
for x in [0, 1, 2]:
    pass

# else:
for x in range(6):
    print(x)
else:
    print("Terminou")

# for aninhado
substantivo = ["casa", "pessoa", "carro"]
adjetivo = ["grande", "pequena", "verde"]

for x in substantivo:
    for y in adjetivo:
        print(x, y)


