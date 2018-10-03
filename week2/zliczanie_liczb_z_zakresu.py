# ile jest liczb parzystych i nieparzystych w zakresie do 10

liczba_parzysta = 0
liczba_nieparzysta = 0

for number in range(10):
    if number % 2 == 0:
        # Pamietaj na jakich zmiennych operujesz :P
        liczba_parzysta = liczba_parzysta + 1
        #liczba_parzysta +=1
    else:
        liczba_nieparzysta = liczba_nieparzysta + 1
a = "ilosc przystych"+ str(liczba_parzysta)
b = "ilosc parzystych {}".format(liczba_parzysta)
c = f"ilosc parzystych {liczba_parzysta}"

print("ilość nieprzystych", liczba_nieparzysta)


