class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    # def __add__(self, other):
    #     return Complex(self.real+ other.real,
    #                    self.img+other.img)

    # def __sub__(self, other):
    #     return Complex(self.real- other.real,
    #                    self.img-other.img)

    # (a,b)(c,d)= (ac-bd,ad+bc)
    # def __mul__(self, other):
    #     return Complex((self.real*other.real)-(self.img*other.img),
    #                    (self.real*other.img)+(self.img*other.real))

    def __pow__(self,power,modulo=None):
        if power == 2:
            return self ** self



a = Complex(1,2)
b = Complex(3,4)
c = a**2
print(c.real,c.img)


