#Przelicznik C => F i C <= F
# a. C = (F - 32) * 5/9
# b. F = C * (9/5) + 32

temperatura = input("podaj temperature:")

if temperatura[-1].upper() == "C":
    temp = int(temperatura[:-1]) * (9 / 5) + 32
    F = round(temp,2)
    print("Temperatura w Fahrenheit wynosi:" + str(F))
elif temperatura[-1].upper() == "F":
    temp = (int(temperatura[:-1]) - 32) * 5 / 9
    C = round(temp,2)
    print("Temperatura w stopniach Celsjusza wynosi:" + str(C))
else:
    print("Nie podałeś odpowiedniej wartości do przeliczenia")