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
    amount_needed = 0
    in_inventory = 0
    list_of_warehouses = []
    # go through the order and get the first value
    for value in order.values():
        # add it to a variable
        amount_needed = value
        # go through the list of warehouses and get the index of each one
        for index in range(len(warehouses)):
            # go through each warehouse inventory distribution
            for warehouse in warehouses[index]:
                # get the amounts available for each element in inventory
                amounts_available = list(warehouses[index][warehouse].values())
                # for each index in the list of amounts available
                for amount in amounts_available:
                    while amount_needed != 0 and warehouses[index] not in list_of_warehouses:
                        # check if the amount in the inventory >= amount for the first item in the order
                        if amount >= amount_needed:
                            # there's enough inventory, so we add the warehouse to the returning list
                            list_of_warehouses.append(warehouses[index])
                        else:
                            # add the warehouse to list of warehouses needed to complete the order
                            # list_of_warehouses.append(warehouses[index])
                            # decrease the amount needed
                            amount_needed -= amount

            if amount < amount_needed:
                list_of_warehouses = []
    return list_of_warehouses



    # go through the inventory and get the first value
    # check if the first value of the order >= first value of inventory
    # if true, add warehouse to a list
    # if false, go to the next warehouse
    pass

# allocate_inventory({}, []) # tipos correctos

# allocate_inventory(1, "lol")  # tipos incorrectos


print(allocate_inventory({"apple": 5, "banana": 5, "orange": 5}, [ { "owd": { "apple": 5, "orange": 10 } }, { "dm": { "banana": 5, "orange": 10 } } ]))

print(allocate_inventory({ "apple": 10 }, [ {"owd": { "apple": 5 } }, { "dm": { "apple": 5 } } ]))

print(allocate_inventory({ "apple": 2 }, [{ "owd": { "apple": 1 } }]))