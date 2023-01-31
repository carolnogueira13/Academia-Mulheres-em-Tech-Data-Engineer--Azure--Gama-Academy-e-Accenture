x = 13
if x > 10:
    print(f"{x} > 10")
elif x == 10:
    print(f"{x} = 10 ")
else:
    print(f"{x} < 10")

tipo = "par" if x % 2 == 0 else "ímpar"
print(tipo)

a = 7
b = 5
if a > b: print("a > b")  # um if de apenas uma linha, pode ser declarado dessa forma sem precisar da identação
