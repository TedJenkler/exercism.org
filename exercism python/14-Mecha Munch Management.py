"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart

def read_notes(notes):
    return dict.fromkeys(notes, 1)
    
def update_recipes(ideas, recipe_updates):
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart

def send_to_store(cart, aisle_mapping):
    fulfillment_cart = {}
    for item in cart:
        if item in aisle_mapping:
            aisle, refrigeration = aisle_mapping[item]
            fulfillment_cart[item] = [cart[item], aisle, refrigeration]
    
    sorted_fulfillment_cart = dict(sorted(fulfillment_cart.items(), reverse=True))
    
    return sorted_fulfillment_cart
    

def update_store_inventory(fulfillment_cart, store_inventory):
    for item in fulfillment_cart:
        if item in store_inventory:
            ordered_quantity = fulfillment_cart[item][0]
            available_quantity = store_inventory[item][0]
            
            remaining_quantity = available_quantity - ordered_quantity
            if remaining_quantity <= 0:
                store_inventory[item][0] = 'Out of Stock'
            else:
                store_inventory[item][0] = remaining_quantity
    return store_inventory