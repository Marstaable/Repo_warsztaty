# liczba perfekcyjna - naturalna - ktorej suma jej dzielnikow jest równa tej liczbie


# test czy to dzielnik

# lista(kubelek)

# sumator(inny plik)*

# trzeba porownać

# ile argumentow? jeden - liczba testowana
# Co bedzie zwraca - True albo False
# jak znaleźć dzielniki
# ustalic zakres
#if , modulo
# sumator
# sum == n

dzielniki =[]

def liczba_perfekcyjna(a):
    suma = 0
    for i in range(1,a):
        # if i !=0 and a%i == 0 :
        if a%i == 0 :
            dzielniki.append(i)
    for n in dzielniki:
        suma += n
    return suma  == a
    #     return True
    # else:
    #     return False


l = liczba_perfekcyjna(6)
liczba_perfekcyjna(8)
liczba_perfekcyjna(12)
n = liczba_perfekcyjna(17)

print(n)
print(l)






