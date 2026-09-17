item_1 = "Laptop"
item_2 = "Coffee"

warehouse = {
    "Shelf_A": {},
    "Shelf_B": {}
}


def put_away(shelf_name, item, quantity):

    warehouse[shelf_name] = {item, quantity}
    print("Put away", quantity, "items into", shelf_name)


put_away("Shelf_A", item_1, 10)
put_away("Shelf_B", item_2, 5)


print("Warehouse:", warehouse)



