lista1 = [1, 2, 3, 4, 5, 6, 7, 9]
lista2 = [1, 2, 3, 4, 5]
lista3 = [1, 2, 3]

def sumator(lista):

    suma = 0
    for i in lista:
        suma = suma + i
    return suma


wynik1 = sumator(lista1)
wynik2 = sumator(lista2)
wynik3 = sumator(lista3)


print(wynik1)
print(wynik2)
print(wynik3)
