#  Popularna gra słowna FizzBuzz
# - wypisz liczby od 1 do 100 (wlacznie)
# - jesli podzielna przez 3 to napisz Fizz
# - jesli podzilena przez 5 to napisz Buzz
# - jesli podzielna przez 3 i przez 5 to napisz FizzBuzz



for number in range(100):
    if number % 5 == 0 and number % 3 == 0:
        print(f"FizzBuzz {number}")
    elif number % 5 == 0:
        print(f"Buzz {number}")
    elif number % 3 == 0:
        print(f"Fuzz {number}")
    else:
        print(number)