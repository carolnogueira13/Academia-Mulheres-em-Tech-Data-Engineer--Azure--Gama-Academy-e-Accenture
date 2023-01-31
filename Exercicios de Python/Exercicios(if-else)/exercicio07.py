nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) /2

if media == 10:
    print("Aprovada com distinção")
elif media >= 7:
    print("Aprovada")
else:
    print("Reprovada")
