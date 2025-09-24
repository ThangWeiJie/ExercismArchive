"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        current_cart[item] = 1 + current_cart.setdefault(item, 0)

    return current_cart
        


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    new_cart = {}

    for item in notes:
        new_cart[item] = 1 + new_cart.setdefault(item, 0)

    return new_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas |= recipe_updates
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))

def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    fulfillment_cart = {}

    all_keys = cart.keys()

    for key in all_keys:
        quantity = cart[key]
        aisle =  aisle_mapping[key][0]
        refrigeration = aisle_mapping[key][1]

        fulfillment_cart[key] = [quantity, aisle, refrigeration]

    return dict(sorted(fulfillment_cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for key, value in fulfillment_cart.items():
        ordered = value[0]

        if store_inventory[key][0] != 'Out of Stock':
            updated_quantity = store_inventory[key][0] - ordered
            print(updated_quantity)

            if updated_quantity <= 0:
                store_inventory[key][0] = 'Out of Stock'
            else:
                store_inventory[key][0] = updated_quantity

    return store_inventory
