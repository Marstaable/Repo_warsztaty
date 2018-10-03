haslo = input("Wpisz Haslo:")

while len(haslo) < 6:
    print("Hasło jest za krótkie")
    # pamiętaj o tym aby wpływac na warunek - modyfikowac wartość - aby miec nowe dane do analizy
    haslo = input("Wpisz Haslo:")
# w innym przypadku wychodzi z pętli
print("Dziękuję za hasło")