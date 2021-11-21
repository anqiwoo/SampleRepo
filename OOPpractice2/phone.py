from item import Item
import csv


class Phone(Item):
    all = []

    def __init__(self, name, price, quantity, color='blue'):
        super().__init__(
            name, price, quantity
        )
        self.color = color
        Phone.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Phone(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))
            )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity}, {self.color})"
