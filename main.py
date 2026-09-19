from wms import Item, Location, basic_receiveing, putaway, picking, packing

def sep():
    print(20 * "*")


laptop = Item("Gaming Laptop", "LAP01")
shelf_a = Location("shelf_a")
rec_zone = Location("RECEIVE")
pack_zone = Location("PACKING")
ship_zone = Location("SHIPPING")


basic_receiveing(rec_zone, laptop, 7)
rec_zone.show_stock()
sep()

putaway(rec_zone, shelf_a, laptop, 7)
shelf_a.show_stock()
sep()

picking(shelf_a, pack_zone, laptop, 7)
pack_zone.show_stock()
sep()

packing(pack_zone, ship_zone, laptop, 7)
ship_zone.show_stock()
sep()