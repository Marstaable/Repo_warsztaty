#slowo = 'kajak'
#slowo = "mleko"

# def czy_palindrom():
#     if slowo[:] == slowo[::-1]:
#         return "OK"
#
#
#
# x = czy_palindrom()
#
# print(x)

"""
while???
pierwszy element z ostatnim

x = 0
y = -1
while True:
    if slowo[x] == slowo[y]:
        x +=1
        y -=1
        print("OK")
    else:
        print("NOT")
# """
# slowo = 'kajak'
#
# def czy_palindrom1():
#     x = 0
#     y = -1
#     while  :
#         if slowo[x].lower() == slowo[y].lower():
#             x += 1
#             y -= 1
#             print("OK")
#
#         else:
#             print("NOT")
#
#
# czy_palindrom1()

# def isPalindrom(s):
#     return s ==s[::-1]


def isPalindrom(s):
    lewy_indeks = 0
    prawy_indeks = len(s)-1
    while prawy_indeks >= lewy_indeks:
        if s[lewy_indeks] != s[prawy_indeks]:
            return False
        lewy_indeks += 1
        prawy_indeks -=1
    return True

print(isPalindrom("niekajak"))