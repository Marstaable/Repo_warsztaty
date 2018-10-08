# Oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
# kolejne lata, psi rok to 4 ludzkie lata np. 15 ludzkich lat to 73 psie lata


age = int(input("Podaj wiek psa:"))

dog_age = 0

for years in range(age):
    years +=1
    if years == 1 or years == 2:
        dog_age += 10.5
    else:
        dog_age +=4

print(f"Prawdziwy wiek twojego psa to:{dog_age}")