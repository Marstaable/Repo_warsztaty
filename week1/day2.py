# Czy liczba jest podzielna przez 2
"""
Pamiętaj input zawsze zwraca string :P
wczytac dane od usera
"""
number = input("Proszę podaj liczbę: ")
# uzuskac wynik reszty z dzielenia
result = int(number) % 2
# porownac reszte z dzielenia i dopisac komentarz
if result == 0:
    print("liczba podzielna przez 2")
else:
    print("Liczba niepodzielna przez 2")