from math import pi

figura = input("Podaj numer figury, której obwód chcesz obliczyć 1. trojkąt 2. kwadrat 3.koło: ")


if int(figura) == 1:
    podstawa = input("Podaj długość podstawy:")
    wysokosc = input("podaj wysokość trojkąta:")
    wynik = 0.5 * int(podstawa) * int(wysokosc)
    print('Obwód Twojego trojkąta to: ' + str(wynik) + ' cm')
elif int(figura) == 2:
    bok = input("Podaj długość boku:")
    wynik = 4 * int(bok)
    print("Obwód Twojego kwadratu to: " + str(wynik)+"cm")
elif int(figura) == 3:
    promien = input("Podaj długość promienia:")
    wynik = 2 * pi * int(promien)
    wynik = round(wynik,2)
    print('Obwód Twojego koła wynosi:' + str(wynik) +"cm")
else:
    print("Wybrałeś nieodpowiedni numer")