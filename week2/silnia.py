# czy mamy zakres?
# pętla for
# obliczyc silnie do 10 ...

"""
iloczyn wszystkich liczb naturalnych dodatnich nie większych niż n
"""
liczba = input("Podaj liczbę:")

# silnia = 1
#
# for number in range(int(liczba)):
#     number +=1
#     silnia = silnia*number
#     #print(number)
#
# print(silnia)

silnia = 1

for number in range(int(liczba)):
    number+=1
    silnia = silnia*number

print(silnia)