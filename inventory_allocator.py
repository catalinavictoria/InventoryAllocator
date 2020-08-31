from typing import List, Dict

OrderType = Dict
WarehousesType = List[Dict]
ShipmentType = List[Dict]


def allocate_inventory(order: OrderType, warehouses: WarehousesType) -> ShipmentType:
    """
    Function to optimize the allocation of inventory into different warehouses
    :param order: An order to optimize
    :param warehouses: Warehouses to allocate inventory into
    :return: Optimized allocated inventory
    """
    # declare variables needed
    item_name = ''
    value_needed = 0
    list_of_warehouses = []
    # loop through keys of the dictionary
    for key in order:
        item_name = key
        # get the amount needed for that key
        value_needed = order.get(key)

        # loop through list of warehouses and get first warehouse inventory
        for warehouse in warehouses:
            for inv in warehouse:
                inventory = [warehouse.get(inv)]

            # loop trough items in the warehouse's inventory
            for i in range(len(inventory)):
                for name in inventory[i]:
                    # check if item and amount are available in inventory distribution
                    if item_name == name and inventory[i][name] > 0:
                        # declare a variable for amount of items fulfilled
                        amount_fulfilled = 0
                        # while amount_fulfilled != value_needed:
                            # check if the amount in inventory is greater than amount needed
                        if inventory[i][name] > value_needed:
                            # update amount fulfilled to be the amount needed
                            amount_fulfilled = value_needed
                            # set the value needed to 0, since we can complete the order with this inventory
                            value_needed = 0
                        else:
                            # add all the amount available in inventory to the amount fulfilled variable
                            amount_fulfilled = inventory[i][name]
                            # subtract amount available in inventory from value needed
                            value_needed -= inventory[i][name]

                            if amount_fulfilled >= value_needed:
                                list_of_warehouses.append(warehouse)
    return list_of_warehouses


print(allocate_inventory({"apple": 5, "banana": 5, "orange": 5},
                         [{"owd": {"apple": 5, "orange": 10}}, {"dm": {"banana": 5, "orange": 10}}]))
print(allocate_inventory({"apple": 10}, [{"owd": {"apple": 5}}, {"dm": {"apple": 5}}]))
print(allocate_inventory({"apple": 2}, [{"owd": {"apple": 1}}]))
