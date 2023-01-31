# Utilizar o terminal como entrada de dados

import sys  # biblioteca para automação com entrada de argumentos diretamente da linha de comando

nome = sys.argv[3]
print(nome)

print("Argumento 1: " + sys.argv[0])
print("Argumento 2: " + sys.argv[1])
print("Argumentos: " + str(sys.argv))

valor = int(sys.argv[1])
valor2 = int(sys.argv[2])
valor3 = int(sys.argv[3])
valor4 = int(sys.argv[4])
print(f"Média: {(valor + valor2 + valor3 + valor4)/4}")

