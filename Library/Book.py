from Interface.I_Product import I_Product

class Book(I_Product):
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

