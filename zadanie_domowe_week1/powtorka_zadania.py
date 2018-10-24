# zadanie z wyliczeniem pola powierzchni figur :)
import math
figure  = input("Proszę wybrać figurę 1.trójkąt;2.Kwadrat;3.Prostokąt;4.Koło: ")

result = int(figure)

if result == 1:
    """
    P=1/2ah
    """
    bok = input("Podaj długość boku w centymetrach: ")
    wysokosc = input("Podaj wysokość w centymetrach: ")
    pole = 1/2*int(bok)*int(wysokosc)
    print("pole trójkąta:"+str(pole) + " cm")
elif result == 2:
    """
    P = a2
    """
    bok = input("Podaj długość boku w centymetrach: ")
    pole = int(bok)*int(bok)
    print("Pole kwadratu:" +str(pole) + " cm")
elif result == 3:
    """
    P = a · b
    """
    bok = input("Podaj długość boku w centymetrach: ")
    bok2 = input("Podaj długość drugiego boku w centymetrach: ")
    pole = int(bok)*int(bok2)
    print("Pole prostokąta: " + str(pole) + " cm")
elif result == 4:
    """
    P = πr2
    """
    bok = input("Podaj długość promienia w centymetrach: ")
    pole = round(math.pi,2) * (int(bok)*int(bok))
    print("Pole Koła: " + str(pole) +" cm")
else:
    print("Spróbuj jeszcze raz")
