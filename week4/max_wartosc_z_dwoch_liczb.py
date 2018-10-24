# jakie argumenty = dwie liczby
# co ma zwracac = tą większą??
#jak ma wyglądać


def max_dwoch_liczb(a,b):
    if a > b:
        return a
    return b


#print(max_dwoch_liczb(5,1))

lista = [1,10,5]
m = lista[0]

for number in lista:
     if max_dwoch_liczb(m,number) != m:
         m = number

print(m)



