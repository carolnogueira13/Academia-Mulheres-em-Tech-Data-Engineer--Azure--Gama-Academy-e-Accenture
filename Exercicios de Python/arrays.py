import array

initializer_list = [2, 5, 43, 5, 10, 52, 29, 5]
number_array = array.array('i', initializer_list)

print(number_array)
print(number_array[4])
print(number_array[len(number_array) -1])
print(number_array[-1])

number_array.append(4)  # adicionar um número na última posição

print(number_array[-1])

print(number_array[2:5])  # valores da posição 2 a 5 (a última posição não inclusiva)





