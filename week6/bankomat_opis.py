# Cel - Bankomat
# - skrzynka ?,konto bankowe?,karta?,Bank?,My?
# jakie sa relacje miedzy tymi obiektami
# uzytkownik ma karte , wprowadza ja do bankomatu, nastepuje uwierzytelnieie, bankomat 'zczytuje' nr konta,\
#  wysyla nr i haslo do banku,bank wysyla stan konta do bankowmatu


# nr konta - int
# haslo - string
# class Card - number,passwd
# class ATM - Menu -pętla - pobiera hasło,numer konta, wyswietla stan konta,obsluguje wplaty i wyplaty
# class Account - numer,balance
# class Bank - sklada sie z kont - lista kont


# TODO:
# warunek na unikalność nr kont - sposob to słownik
# zainmplementowanie salda
# aplata i wyplata pieniedzy
# fakturowanie w hurtowni
# hurtownia, lista zakupow, rozne sztuki zakupow, niektorych produktow nie ma, rachunek faktura
