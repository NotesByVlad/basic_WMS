# Models
# ---
class Item:
    def __init__(self, name, sku):
        self.name = name
        self.sku = sku

    def __repr__(self):
        return f"{self.name} ({self.sku})"

class LicensePlateNumber:
    """Represents a unique License Plate Number (LPN) or Handling Unit (HU).

    An LPN is a unique barcode sticker assigned to a physical container—such 
    as a box, tote, or pallet. This class acts as that container, allowing the 
    application to track the container itself rather than individual loose items.
    """

    def __init__(self, lpn_id):
        self.lpn_id = lpn_id
        self.inventory = {}

    def add_item_stock(self, item, qty):
        if item in self.inventory:
            self.inventory[item] += qty
        else:
            self.inventory[item] = qty

    def remove_item_stock(self, item, qty):
        self.inventory[item] -= qty
        if self.inventory[item] == 0:
            del self.inventory[item]

    def __repr__(self):
        return f"LPN [{self.lpn_id}] -> {self.inventory}"

class Location:
    def __init__(self, name):
        self.name = name
        self.containers = []  

    def add_container(self, lpn):
        self.containers.append(lpn)

    def remove_stock(self, lpn):
        if lpn in self.containers:
            self.containers.remove(lpn)

    def show_stock(self):
        print(self.containers)

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