class Vendor:
    # def __init__(self, item):
    #     self.inventory = []
    #     self.item = item

    def __init__(self, inventory=None):
        # if no inventory, default to empty list
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        # if item not in self.inventory:
        #     return False
        # else:

        # always add item to inventory
        self.inventory.append(item)
        return item

    def remove(self, item):
        # if item not in self.inventory:
        #     return False
        # else:
        #     self.inventory.remove(item)
        #     return item

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