i = 1
while i < 6:
    print(i)
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# else
i = 1
while i < 6:
    print(i)
else:
    print(f"{i} pos while")
    print("i is no longer less than 6")