# utworz liste i usun duplikaty


lista = [1,2,3,4,5,5,2,6,7,9]

nowa_lista =[]


for i in lista:
    if i not in nowa_lista:
        nowa_lista.append(i)
    # else:
    #     pass



print(nowa_lista)
