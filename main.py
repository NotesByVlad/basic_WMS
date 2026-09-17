item_1 = "Laptop"
item_2 = "Coffee"

class Item:
    def __init__(self, name, sku):
        self.name = name
        self.sku = sku

laptop = Item("Gaming Laptop", "LAP01")

warehouse = {
    "Shelf_A": {},
    "Shelf_B": {},
    "Shelf_C": {}
}


def put_away(shelf_name, item, quantity):

    warehouse[shelf_name] = {item : quantity}
    print("Put away", quantity, "items into", shelf_name)


put_away("Shelf_A", item_1, 10)
put_away("Shelf_B", item_2, 5)
put_away("Shelf_C", laptop, 5)

print("Warehouse:", warehouse)



