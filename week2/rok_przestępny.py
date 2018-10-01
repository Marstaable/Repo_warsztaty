year = int(input("Podaj rok: "))


if (year%4 == 0 and year%100 == 1) or year%400 == 0:
    print("Rok przestępny")
else:
    print("Rok nie jest przestępny")


