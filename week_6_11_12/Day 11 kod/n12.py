# class Foo():
#     def __priv33(self):
#         print("Jestem metodą prywatną")
#     def jawny(self):
#         self.__priv()
#
# f = Foo()
#
# f.jawny()
#
# print(f.__dict__)
# print(f._Foo__priv33)
# print(dir(f))
# def property(fn):
#     return fn

class Person:
    def __init__(self,fn,ln):
        self.__fn = fn
        self.__ln = ln
        

    @property
    def fn(self):
        return self.__fn

    @fn.setter
    def fn(self,val):
        print("Hej ktoś zmienia wartość")
        #self.__fn = val

    @fn.deleter
    def fn(self):
        #print('deleter')
        self.__fn = None

    @property
    def ln(self):
        return self.__ln

    @ln.setter
    def ln(self, val):
        print("Hej ktoś zmienia wartość")
        # self.__fn = val

    @ln.deleter
    def ln(self):
        #print('deleter')
        self.__fn = None

    @property
    def fullname(self):
        return f"{self.fn}{self.ln}"



    # @property
    # def ln(self):
    #     return self.__fn
    #
    # @property   #tracimy mozliwosc przekazywania argumentow, sposob wywolania zamieniamy \
    #             # jak wywolanie na atrybut
    # def full_name(self):
    #     return f"{self.__fn}{self.__ln}"

p = Person("Jan"," Kowalski")
# print(p.ln)
#del p.ln
#del p.fn
#del p.ln
# p.fn = "Maria"
print(p.fullname)


