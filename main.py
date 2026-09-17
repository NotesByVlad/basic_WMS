class Item:
    def __init__(self, name, sku):
        self.name = name
        self.sku = sku

    def __repr__(self):
        return f"{self.name} ({self.sku})"


class Location:
    def __init__(self, name):
        self.name = name
        self.inventory = {}  

    def add_stock(self, item, qty):
        if item in self.inventory:
            self.inventory[item] += qty
        else:
            self.inventory[item] = qty

    def remove_stock(self, item, qty):
        self.inventory[item] -= qty
        if self.inventory[item] == 0:
            del self.inventory[item]

    def show_stock(self):
        print(self.inventory)
        
laptop = Item("Gaming Laptop", "LAP01")
shelf_a = Location("shelf_a")
shelf_a.add_stock(laptop, 5)

shelf_a.show_items() 

