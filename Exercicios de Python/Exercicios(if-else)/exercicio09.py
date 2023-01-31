perguntas = ["Falou com a vitima no dia do crime? [S/N]",
             "Esteve no local do crime? [S/N]",
             "Mora perto da vitima? [S/N]",
             "Devia dinheiro para a vitima? [S/N]",
             "Já trabalhou com a vítima? [S/N]"]

positivo = 0

for item in perguntas:
    resp = " "
    while resp not in ("S", "N"):
        resp = input(item).upper()[0]
    if resp == "S":
        positivo += 1

if positivo == 2:
    print("Suspeita")
elif positivo in (3, 4):
    print("Cúmplice")
elif positivo == 5:
    print("Assasssina")
else:
    print("Inocente")
