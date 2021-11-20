from item import Item
from phone import Phone

Item.instantiate_from_csv()
print(Item.all)
Phone.instantiate_from_csv()
print(Phone.all)

# print(Item.__dict__)
# print(Phone.__dict__)
