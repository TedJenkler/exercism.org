"""Functions to keep track and alter inventory."""


def create_inventory(items):
    inventory_dict = {}
    for item in items:
        if item in inventory_dict:
            inventory_dict[item] += 1
        else:
            inventory_dict[item] = 1
    return inventory_dict


def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    result = []
    for item in inventory:
        if inventory[item] > 0:
            result.append((item, inventory[item])) 
    return result