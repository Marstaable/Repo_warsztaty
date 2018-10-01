number = input("Podaj liczbe:")

if number.isdigit():

    if int(number)%3 == 0:
        print("Liczba podzielna przez 3")
    elif int(number)%5 ==0:
        print("Liczba podzielna przez 5")
    elif int(number)%7 ==0:
        print("Liczba podzielna przez 7")
    else:
        print("Liczba nie jest podzielna ani przez 3 ani przez 5 ani przez 7 ")
else:
    print("To nie jest liczba!")
