## Zmienne sa dostepne sa wcieciami w dol
# do typow zlozonych mam zawsze dostep , nie ma potrzby deklaracji dodatkowej global

imie = "Ania"
imiona= []
def foo():
    global imie
    print(imie)
    imie = "Jola"
    print("Wewnatrz", imie)
    imiona.append("Ania")
foo()

print(imie)



#docstring - sluzy do opisywania
"""
Komentarz
"""