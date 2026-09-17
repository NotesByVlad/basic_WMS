# item_1 = "Laptop"
# item_2 = "Coffee"

class Item:
    def __init__(self, name, sku):
        self.name = name
        self.sku = sku

    def __repr__(self):
        return f"{self.name} ({self.sku})"

laptop = Item("Gaming Laptop", "LAP01")

class Location:
    def __init__(self, name):
        self.name = name
        self.inventory = {}  

    def add_item(self, item, qty):
        if item in self.inventory:
            self.inventory[item] += qty
        else:
            self.inventory[item] = qty

    def show_items(self):
        print(self.inventory)
        
shelf_a = Location("shelf_a")
shelf_a.add_item(laptop, 5)
shelf_a.show_items() 

# warehouse = {
#     "Shelf_A": {},
#     "Shelf_B": {},
#     "Shelf_C": {}
# }

# def put_away(shelf_name, item, quantity):

#     warehouse[shelf_name] = {item : quantity}
#     print("Put away", quantity, "items into", shelf_name)


# put_away("Shelf_A", item_1, 10)
# put_away("Shelf_B", item_2, 5)
# put_away("Shelf_C", laptop, 5)


# print("Warehouse:", warehouse)



