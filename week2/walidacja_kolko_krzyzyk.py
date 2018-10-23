dane = "xxxoxoxox"
# 012
# 345
# 678
# 036


# TODO: Zrób modyfikację - dla parzystych i nieparzystych; empty string;replace()

wygrana = None

for n in range(int(dane)):
    if n % 2 != 0:
        print("nieparzyste")
    elif n % 2 == 0:
        print("parzyste")
    else:
        pass

if dane[0] == dane[1] == dane[2]:
    print("Wygrana 012")

elif dane[3] == dane[4] == dane[5]:
    print("Wygrana 345")

elif dane[6] == dane[7] == dane[8]:
    print("Wygrana 678")
elif dane[0] == dane[3] == dane[6]:
    print("Wygrana 036")
elif dane[1] == dane[4] == dane[7]:
    print("Wygrana 147")
elif dane[2] == dane[5] == dane[8]:
    print("Wygrana 258")
elif dane[0] == dane[4] == dane[8]:
    print("Wygrana 048")
    wygrana = dane[0] + dane[4] + dane[8]
    # nie da sie wymienic, trzeba odwołac się za każdym razem :(
    print(wygrana)
elif dane[2] == dane[4] == dane[6]:
    print("Wygrana 246")
else:
    print("Nic z tego :P")

if wygrana == "xxx":
    print("wygrał X")
else:
    print("wygrał O")
