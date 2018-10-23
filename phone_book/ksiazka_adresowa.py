### Lista nazwisk imion nr tel
### dodaj usuń


user = input("Witaj, Wybierz numer\n"
             " 1.Wyszukiwanie użytkownika\n \
            2.Dodawanie nowego użtkownika\n\
              3.Edytowanie istniejącego użytkownika\n \
              4.Usuwanie nieaktywnego użytkownika(Be careful)\n")



# phonebook = '/Users/mstaroscik/PycharmProjects/Repo_warsztaty/phone_book/phone_book.txt'
# #
# #
# # with open(phonebook,"a") as plik:
# #     plik.write(user+"\n")


with open('phonebook.txt','a') as plik:
    plik.write(user+'\n')