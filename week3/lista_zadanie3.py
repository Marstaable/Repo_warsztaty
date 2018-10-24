# wyszukiwanie najwiekszej i najmniejszej wartości


lista = [3, 4, 5, 6, 7, 9,10,11,12,13,14,15,16]
#
# a = min(lista)
# b = max(lista)
#
# print(a,b)


max_a = 0
# val_min = lista[0]

for i in lista:
    if i > max_a:
        max_a = i

min_a = 9

for i in lista:
    if i < min_a:
        min_a = i

print(max_a)
print(min_a)
