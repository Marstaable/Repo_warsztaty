# Fibonacci do 100

# While
# prog < 100
a = 0
b = 1


while a + b < 1000:
    c = a + b
    a = b
    b = c
    print(c)
