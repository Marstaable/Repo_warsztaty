def dodaj_imie(imie,imiona=None):
    if imiona is None:
        imiona =[]

    imiona.append(imie)
    return imiona
i = []
dodaj_imie("Adam",i)
dodaj_imie("Justyna")
dodaj_imie("Monika",i)

print(i)

# wartosci domysle tworzone sa tylko raz po odpaleniu porgramu
# przypisuje sie im typy niezmienne i proste