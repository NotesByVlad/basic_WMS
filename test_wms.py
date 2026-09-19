from wms import Item, Location, basic_receiveing, putaway, picking, packing

def test_warehouse_flow():
    print("Running Tests:")

    # Setup
    test_laptop = Item("Gaming Laptop", "LAP01")
    test_rec_zone = Location("RECEIVE")
    test_shelf_a = Location("shelf_a")
    test_pack_zone = Location("PACKING")
    test_ship_zone = Location("SHIPPING")

    # Receiving
    basic_receiveing(test_rec_zone, test_laptop, 7)
    assert test_rec_zone.inventory[test_laptop] == 7, "Error: Receiving did not add 7 items."

    # Putaway
    putaway(test_rec_zone, test_shelf_a, test_laptop, 7)
    assert test_laptop not in test_rec_zone.inventory, "Error: Putaway left stock in Receiving Zone."
    assert test_shelf_a.inventory[test_laptop] == 7, "Error: Putaway did not add stock to Shelf A."

    # Picking
    picking(test_shelf_a, test_pack_zone, test_laptop, 7)
    assert test_laptop not in test_shelf_a.inventory, "Error: Picking left stock on Shelf A."
    assert test_pack_zone.inventory[test_laptop] == 7, "Error: Picking did not move stock to Packing."

    # Packing
    packing(test_pack_zone, test_ship_zone, test_laptop, 7)
    assert test_laptop not in test_pack_zone.inventory, "Error: Packing left stock in Pack Zone."
    assert test_ship_zone.inventory[test_laptop] == 7, "Error: Packing did not move stock to Shipping."

    print("\nALL TESTS PASSED!")

test_warehouse_flow()