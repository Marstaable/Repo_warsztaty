number = input("Podaj liczbe:")

if number.isdigit():
    checked = False
    if int(number) % 3 == 0:
        checked = True
        print("Liczba podzielna przez 3")
    if int(number) % 5 == 0:
        checked = True

        print("Liczba podzielna przez 5")
    if int(number) % 7 == 0:
        checked = True

        print("Liczba podzielna przez 7")

    if not checked:
        print("int niepodzielny przez 3,,5,7")
    # else:
    #     print("Liczba nie jest podzielna ani przez 3 ani przez 5 ani przez 7 ")
else:
    print("To nie jest liczba!")
