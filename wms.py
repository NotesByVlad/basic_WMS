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

def putaway(from_location, to_location, item, qty):
    from_location.remove_stock(item, qty)
    to_location.add_stock(item, qty)
    print(f"putaway: {item.name} qty: {qty}")
    print(f"added on {to_location.name}")

def picking(from_location, to_location, item, qty):
    from_location.remove_stock(item, qty)
    to_location.add_stock(item, qty)
    print(f"picking: {item.name} qty: {qty}")
    print(f"added to {to_location.name}")

def packing(from_location, to_location, item, qty):
    from_location.remove_stock(item, qty)
    to_location.add_stock(item, qty)
    print(f"packing: {item.name} qty: {qty}")
    print(f"added to {to_location.name}")
    print("Ready for shipment!")