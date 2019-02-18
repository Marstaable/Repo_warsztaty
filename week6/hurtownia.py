# fakturowanie w hurtowni
# hurtownia, lista zakupow, rozne sztuki zakupow, niektorych produktow nie ma, rachunek faktura
# ewidencja produktow i ich stanow magazynowych. Opcja pobierania listy zakupow i wyswietlania faktury z pozycjami
# lista zakupów - produkty, sztuki
# magazyn : produkty sztuki
# 
# lista zakupów - input
# magazyn - produkt ilość

class Warehouse(object):
    def __init__(self,products_dict):
        self.poducts_dict = products_dict


class Product(object):
    def __init__(self,nazwa,cena,ilosc):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc



class Invoice(object):

    def __init__(self, warehouse):
        self.warehouse = warehouse


    def menu(self):
        print("Witamy w Hurtowni Take-online")
        print('Menu:')
        print('1.Złóż zamówienie')
        print('2.Stan Magazynów')
        print('3.Cennik')

        numer_opcji = input('Podaj numer opcji,ktorą wybrałeś: ')
        if numer_opcji == '1':
            pass
        elif numer_opcji == '2':
            produkt = input("Wybierz produkt 1.Jablko,2.Marchewka,3.Pomidor,4.Papryka Czerwona")
            if produkt == "1":
                self.products_dict
                print(jablko)




warehouse = Warehouse({
    "jablko":Product("jablko",2.50,300),
    "marchewka":Product("marchewka",1.70,200),
    "pomidor":Product("pomidor",2.30,75),
    "papryka_czerwona":Product("papryka czerwona",5.60,20)
})


invoice = Invoice(warehouse)
invoice.menu()