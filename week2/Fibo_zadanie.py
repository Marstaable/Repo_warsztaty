# Fibonacci do 100
"""
 ciąg liczb naturalnych określony rekurencyjnie w sposób następujący: Pierwszy wyraz jest równy 0, drugi jest równy 1, \
 każdy następny jest sumą dwóch poprzednich. Formalnie: Kolejne wyrazy tego ciągu nazywane są liczbami Fibonacciego.

"""

# While
# prog < 100
a = 0
b = 1


while a + b < 100:
    c = a + b
    a = b
    b = c
    print(c)
