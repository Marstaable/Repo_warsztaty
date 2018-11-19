class Samochod(object):
    def __init__(self,user_model):
        self.model = user_model
        self.predkosc = 0
    def zatrab(self):
        print("honk honk")
    def przyspiesz(self, wartosc):
        self.predkosc += wartosc

# samochod1 = Samochod()
# samochod1.model = "VP"
# print(samochod1.model)
#
# samochod2 = Samochod()
# samochod2.model = "Seat"
# print(samochod2.model)
# przypisac mu wartosc

samochod1 = Samochod("VP")
# samochod1.model = "VP"
print(samochod1.model)