class Vendor:
    def __init__(self, inventory=None):
        # if no inventory, default to empty list
        self.inventory = inventory if inventory is not None else []

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

        # DRY - call swap_items using the first items in each inventory
        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])


    # wave 5
    # Create 3 additional modules: Clothing, Decor, and Electronics


    # wave 6
    def get_by_category(self, category):
        matching_items = []

        # finds matching items in inventory by category
        for item in self.inventory:
            if item.category == category:
                matching_items.append(item)
        return matching_items


    def get_best_by_category(self, category):
        # gets all items of category
        matching_items = self.get_by_category(category)

        # if no matches, return none
        if not matching_items:
            return None

        # find best item without using max
        best_item = matching_items[0]
        for item in matching_items:
            if item.condition > best_item.condition:
                best_item = item

        return best_item


    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        # find my best item in their priority category
        my_best_item = self.get_best_by_category(their_priority)

        # find their best item in my priority category
        their_best_item = other_vendor.get_best_by_category(my_priority)

        # if vendors don't have items return false
        if not my_best_item or not their_best_item:
            return False

        # DRY - swap items using swap_items(wave 3)
        return self.swap_items(other_vendor, my_best_item, their_best_item)

