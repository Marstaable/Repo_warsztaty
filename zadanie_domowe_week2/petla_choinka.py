# Rysujemy piramidę z gwiazdek za pomocą pętli. Jako input przyjmujemy wysokość pętli np.dla liczby 3
# powinniśmy dostać coś takiego:
#
#   *
#  **
# ***

star = 0

for number in range(16):
    number+=1
    star = " *" * number
    print(star)




