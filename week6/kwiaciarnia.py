class Flower(object):

    def __init__(self,name,price):
        self.name = name
        self.price = price


class Bouquet(object):
    def __init__(self,):
        self.flowers = {""}
    pass


class FloristShop(object):
    pass


flower = Flower("rose",2.5)
print(flower.name)
print(flower.price)