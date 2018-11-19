class Osoba:
    ilosc_osob = 0
    # ten atrybut jest taki sam dla wsztskich
    def __init__(self, imie, nazwisko):
        # te atrybuty maja rozna wartosc dla kazzdego stworzonego obiektu
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(self.imie,self.nazwisko)
        #weź moje imie i moje nazwisko z tego obiektu, \
        # jak bedziemy to wywolywac na klasie to nie zadziala bo nie ma obiektu brak "self"
        # to jest metoda obiektu nie klasy

jan = Osoba('Jan','Kowalski')

jan.przedstaw_sie()


class Osoba:
    ilosc_osob =0

    @classmethod
    def zeruj_licznik(cls):
        cls.ilosc_osob = 0
        #metoda zerje licznik - aby ja wywolac nie potrzebuje obiektu, wywoluje ja bezposrednio na klasie

        #jan.przedstaw_sie() - wywołuję na obiekcie
        # Osoba.zeruj_licznik()

