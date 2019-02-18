class Bank(object):

    def __init__(self, account_dict):
        self.accounts = account_dict


class Card(object):
    pass


class Account(object):
    def __init__(self, number, passwd, balance=0):
        self.number = number
        self.balance = balance
        self.passwd = passwd


class ATM(object):

    def __init__(self, bank):
        self.bank = bank

    def menu(self):
        password = input("Podaj haslo: ")
        number = input("Podaj nr konta: ")

        for account_number in self.bank.accounts:
            if account_number == number:
                if password == self.bank.accounts[account_number].passwd:
                    self.account = self.bank.accounts[account_number]

        if not self.account:
            print('Hej nie znalazłem konta')
        else:
            print('Menu:')
            print('1.Wyświetl saldo')
            print('2.Wplata')
            print('3.Wyplata')

            numer_operacji = input('Podaj co chcesz ')
            if numer_operacji == '1':
                print(self.account.balance)
            elif numer_operacji == '2':
                wplata = input("Podaj kwotę jaką chcesz wpłacić: ")
                kwota_po_wplacie = int(wplata) + self.account.balance
                print(kwota_po_wplacie)
            elif numer_operacji == '3':
                wyplata = input("Podaj kwotę jaką chcesz wypłacić: ")
                kwota_po_wyplacie = self.account.balance - int(wyplata)
                if kwota_po_wyplacie < 0:
                    print("Brak wystarczających środków na koncie")
                    small_menu = input("Czy chcesz spróbować jeszcze raz? 1.TAK,2.NIE ")
                    if small_menu == '1':
                        atm = ATM(bank)
                        atm.menu()
                    elif small_menu == '2':
                        print("Dziękujemy za wizytę.Życzymy Miłego Dnia")
                elif kwota_po_wyplacie >= 0:
                    print(" Transakcja Zrealizowana: Pozostało na koncie " + str(kwota_po_wyplacie))
                else:
                    print("Nie wybrano odpowiedniej opcji")


bank = Bank({
    "1111": Account('1111', 'abcd', 200),
    '2222': Account('2222', 'efgh'),
    '3333': Account('3333', 'ijkl', 100)

})

atm = ATM(bank)
atm.menu()
