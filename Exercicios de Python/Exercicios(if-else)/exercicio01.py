import sys

valor1 = int(sys.argv[1])
valor2 = int(sys.argv[2])

if valor1 > valor2:
    print(f"{valor1}")
elif valor1 == valor2:
    print(f"{valor1} = {valor2}")
else:
    print(f"{valor2}")
