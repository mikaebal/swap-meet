class Vendor:
    def __init__(self, inventory=None):
        # if no inventory, default to empty list
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        # always add item to inventory
        self.inventory.append(item)
        return item

    def remove(self, item):
        # remove item if it exists
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False


    # part of wave 2
    def get_by_id(self, id):
        # find item in inventory by its unique id
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    # wave 3
    # removes my_item from this Vendor inventory and adds to friend inventory
    # removes their_item from other Vendor inventory and adds it to this inventory
    # method returns True
    # If vendor inventories do not contain my_item or their_item
    # return False
    def swap_items(self, other_vendor, my_item, their_item):
        self.other_vendor = other_vendor
        self.my_item = my_item
        self.their_item = their_item
        
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True

    # wave 4
        def swap_first_item(self, other_vendor):
        # check if either inventory is empty
            if not self.inventory or not other_vendor.inventory:
                return False

        # store first items in temp variable
        self_first_item = self.inventory[0]
        other_first_item = other_vendor.inventory[0]

        # remove first item from inventory 
        self.inventory.pop(0)
        other_vendor.inventory.pop(0)

        # add swapped items 
        self.inventory.append(other_first_item)
        other_vendor.inventory.append(self_first_item)

        return True
    

    # wave 5
    # Create 3 additional modules: Clothing, Decor, and Electronics
    