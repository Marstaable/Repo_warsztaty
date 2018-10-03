slowo = input("Witaj w programie szyfrującym, wpisz slowo a zostanie ono zaszyfrowane:")

code_slowo = slowo.lower().replace("s","$").replace("a","@").replace("i","&").replace("o","#")
print(code_slowo)