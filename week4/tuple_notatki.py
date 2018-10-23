# prymitywne int string float bool None
# tuple - lista niemutowana ,niezmienna
# nawiasy okrągłe "krotka"
# jak nie ma nawiasow to konczy sie przecinkiem
# jak dac pythonowi do zrozumienia ze mamy jednoelementowa tuple dodajemy przecinek (1,)

a=(1,)
b = a + (2,3)
print(b)

# po co nam tuple?
# gdy nie chcemy aby nam ktos czegos modyfikował,\
#  sa bardziej optymalne pamieciowo bo z gory jest znana wielkosc/dlugosc

l =(1,2,3,[])
# tupla jest czteroelementowa, i nie zmienia sie -- tylko lista puchnie ...
l[3].append("B")
print(l)
