def media(*num):
    cont = sum = 0
    for i in num:
        sum += i
        cont += 1
    return sum/cont


print(media(2, 3))
print(media(1, 4, 5, 6, 7, 8))
