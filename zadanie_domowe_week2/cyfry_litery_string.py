# Program obliczajacy liczbe liter i cyfr w stringu. np. dla Tomek36 zwróci 2 liczby i 5 liter

login = input("Podaj słowo:")
number = 0
letter = 0

for letters in login:
    if letters.isdigit():
        number = number +1
    else:
        letter = letter +1

print(f"W podanym słowie {login} jest {letter} liter i {number} cyfry")