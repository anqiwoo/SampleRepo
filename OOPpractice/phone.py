from item import Item
import csv


class Phone(Item):
    all = []

    def __init__(self, name, price, quantity, color='blue'):
        super().__init__(
            name, price, quantity
        )
        self.color = color
        print(Phone.all)
        Phone.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name}, {self.price}, {self.quantity}, {self.color})"
