# plik - obiekty na dysku twadym
# wszytsko na czym chce pracowac musze to wrzucic do pamieci ram
# plik = open("Sciezka do pliku", tryb)
# python prosi nas juz na samym poczatku prosi o deklaracje
#  tego co chcemy z plikiem robic, chodzi o pamiec i jej wykorzystanie
# w - nadpisuje
# a - dopisuje
# python czysci plik tuz po odpaleniu skryptu i realizacji komendy open(,w)
#plik.read(), plik.readline() - wyswietla pokolei  zwraca string
# plik.readlines()- > zwraca liste

# aby wyswietlic wszystkie linie w pliku - readlines lub petla for
# domyslnie read czyta nam caly plik odrazu
# wrirte zapisuje od zera, append zapisuje na koncu
# obiekt plik jest tworzony raz natomiast metode mozemy na nim wywolywac kilka razy
# jak plik otwieramy to tez go zamykamy --> plik.close()
# "with" pozwala na automatyczne zamkniecie pliku
# kontekst manager - alternatywny sposob na zdefiniowanie wartosci,
#   wszedzie tam gdzie mamy ciągły dostęp do duzego obiektu,
# np do bazy danych, sesja ssh,
# domyslny tryb jest read

# w pliku mozemy zdefiniowac liste nazwisk