# Models
# ---
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

# Processes
# ---
def basic_receiveing(location, item, qty=1):
    location.add_stock(item, qty)
    print(f"Received: \n{item} \nQuantity: {qty}")

def putaway(item, qty, location):
    print(f"putaway: {item.name} qty: {qty}")
    location.add_stock(item, qty)
    print(f"added on {location.name}")

def picking(from_location, to_location, item, qty):
    from_location.remove_stock(item, qty)
    to_location.add_stock(item, qty)

def packing(from_location, to_location, item, qty):
    from_location.remove_stock(item, qty)
    to_location.add_stock(item, qty)

# - - -
# - -
# -

laptop = Item("Gaming Laptop", "LAP01")
shelf_a = Location("shelf_a")

rec_zone = Location("RECEIVE")
basic_receiveing(rec_zone, laptop, 7)
rec_zone.show_stock()

pack_zone = Location("PACKING")

ship_zone = Location("SHIPPING")

# putaway(laptop, 5, shelf_a)
# shelf_a.show_stock() 