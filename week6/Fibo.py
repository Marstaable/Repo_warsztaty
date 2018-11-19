
class Fib:
    def __init__(self,n):
        self.a = 0
        self.b = 1
        self.max = n


# iter - zwraca obiekt iterowalny?
# next - stopIteration?

    def __iter__(self):
        return self
    def __next__(self):
        while self.a <= self.max:
            t = self.a
            self.a = self.b
            self.b += t
            return self.a
        raise StopIteration

    def __enter__(self):
        pass
    #pozwala nam definiwanie
    # naszych wlasnych kontekst managerow

for i in Fib(10):
    print(i)