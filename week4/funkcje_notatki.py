# Zanurkuj w Pythonie

#
# lista = [[[[]]]]
#
# new_lista = lista[:]
#
# lista.append(1)
# print(lista)
# print(new_lista)
# argumenty wymagane(pozycyjne), argumenty opcjonalne
#argumenty domyslne sa tworzone tylko raz w trakcie dzialania programu
#lista agrgumentow
def foo(a,l=[]):
    l.append(a)
    print(l)

foo(1)
foo(2)
foo(3)
foo(4)
foo(5)


def mech(b,n=None):
    if not n:
        n = []
    n.append(b)
    print(n)



mech(1)
mech(2)
mech(3)
mech(4)
mech(5)
mech(6)
mech(7)