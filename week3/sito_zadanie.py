# wypisanie liczb pierwszych z danego zakresu
# dziela sie tylko przez siebie

# zakres
# pętla
# tabela pomocnicza na wykreslenia
# nowy zakrs
# nowa pętla
from math import sqrt

lista = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,22,23,24,25,26,27,28,29,30]
odrzucone = []
liczby_pierwsze = []
for i in lista:
    if i not in odrzucone:
        liczby_pierwsze.append(i)
        for i in lista:
            i = i**1
        lista.remove(i)
    else:
        odrzucone.append(i)


# dlaczego 15?
# liczby mniejsze rowne pierwiastkowi kwadratowemu tej liczby ?????
# for i in range():
# if i not in liczby_wykreslone:
# print
# wielokrotnosci ???
print(odrzucone)
print(liczby_pierwsze)
