from week5.samochod import Samochod
from week5.silnik import Silnik

# samochod ma miec silnik :P
silnik = Silnik(1.7,2000)
samochod1 = Samochod("czerwony","opel","astra",silnik)
# samochod2 = Samochod("zielony","VW","Najnowszy:P")

silnik = Silnik(5.4, 1000)
samochod2 = Samochod("zielony","VW","Najnowszy",silnik)

# silnik1 = Silnik(1.7,2000)
# silnik2 = Silnik(5.4,10000)

# def porownaj():
# #     if samochod1.silnik.ilosc_koni > samochod2.silnik.ilosc_koni:
# #         print("samochod1")
# #     elif samochod2.silnik.ilosc_koni > samochod1.silnik.ilosc_koni:
# #         print("samochod2")
# #     else:
# #         print("Błąd - Sprobuj jeszcze raz")
# #
# # porownaj()
# fromsrting
# tostring
def ktory_szybszy(s1,s2):
    if s1.silnik.ilosc_koni>s2.silnik.ilosc_koni:
        return s1
    else:
        return s2