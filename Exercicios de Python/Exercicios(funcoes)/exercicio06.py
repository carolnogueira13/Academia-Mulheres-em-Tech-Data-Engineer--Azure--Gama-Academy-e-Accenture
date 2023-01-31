def media(valor1, valor2, valor3, valor4):
    valores = (valor1, valor2,  valor3,  valor4)
    sum = 0
    for v in valores:
        if 10 >= v > 0:
            sum += v
        else:
            return "Você deve colocar notas de 0 a 10"
    sum /= 4
    if sum < 5:
        return "Reprovada"
    elif sum <= 7:
        return "Está na média"
    return "Aprovada"


print(media(10, 9.25, 9, 10))
print(media(12, 3, 5, 6))
print(media(2, 3, 4, 5))
print(media(4, 6, 7, 8))
