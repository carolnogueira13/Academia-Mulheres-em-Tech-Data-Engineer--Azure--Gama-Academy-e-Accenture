'''
def funcao_teste():
    x = 0
    return x


def soma(a, b):
    total = a + b
    print(total)


def soma2(*valores):  # função que recebe paramentros variados (*)
    total = 0
    for i in valores:
        total += i
    return total

soma(10, 20)
soma(20, 20)
soma(30, 20)
print(soma2(4, 9, 0))
print(soma2(4, 9, 0, 7, 10, 2))
print(soma2(20, 50))
print(soma2(0))



def parametros_nomeados(v1, v2, v3):
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v3 = {v3}")


parametros_nomeados(3, 6, 9)
parametros_nomeados(v3=9, v1=3, v2=6) # parametros nomeados



def parametros_nomeados_variaveis(*nome, **endereco):
    print(endereco)
    print(endereco["rua"])
    print(endereco["num"])
    print(endereco["bairro"])
    print(nome)


parametros_nomeados_variaveis("Camis", "Banguela", rua="Rua 01", bairro="Bairro ABC", num=4, cidade="SP")



def nome_dog(idade, nome="Astolfo"):  # função com um valor default, quando não passo nada ele que é usado
    print(nome)


nome_dog(3)
nome_dog(5, "Pipoca")



def nome_dog(nomes):
    for nome in nomes:
        print(nome)
    print(nomes)


lista = ["Kiara", "Astolfo", "Rex"]
nome_dog(lista)



def soma_dois_numeros_e_media(valor1, valor2): # pode retornar o valor de mais de uma variavel como uma lista
    soma = valor1 + valor2
    media = (valor1 + valor2)/2

    return soma, media

totais = soma_dois_numeros_e_media(32,15)
print(totais)
print(totais[0])
print(totais[1])
'''


def calculo_media(valor1, valor2):  # funções com mais de uma instrução de return
    media = (valor1 + valor2) / 2
    if media < 3:
        return "Reprovada"
    elif media < 7:
        return "Segunda chance"
    # else:
    return "Aprovada"
