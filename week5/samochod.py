# marka, model
#Krok pierwszy - definicja, krok drugi= inicjalizacja/wywołanie - stworzenie egzemplarza
from week5.silnik import Silnik

class Samochod(object):

    def __init__(self,kolor,marka,model,Silnik):
        self.kolor = kolor
        self.marka = marka
        self.model = model
        self.silnik = Silnik

    def zaparkuj(self):
        print("OK")
        return "Poważnie?"
    def zatrab(self):
        print("honk honk")






# print(samochod1.kolor)
# print(samochod2.model)
# print(samochod2.zaparkuj())
# print(silnik1.pojemnosc)
# print(silnik1.ilosc_koni)
# print(silnik2.pojemnosc)
# print(silnik2.ilosc_koni)

#print(samochod1)
