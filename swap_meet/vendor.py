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
    def swap_items(self, item, id_value, other_vendor, my_item, their_item):
        # stringify an instance of Item using str()
        # calling str() on a class instance will cause:
        # overriding, known as "operator overloading"
        # the same method exhibits different behavior across instances of different classes
        
        str(self.item) = item
        str(self.id_value) = id_value

        result = f"An object of type {item} with id {id_value}."
        # result = "An object of type" + str(item) + "with id" + str(id_value)
        # return result

        #  removes my_item from this Vendor inventory and adds to friend inventory
        # removes their_item from other Vendor inventory and adds it to this inventory
        # method returns True
        # If vendor inventories do not contain my_item or their_item
        # return False

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
    
    # Clothing attributes: id, fabric (defailt "Unknown")
    # has a function get_category to returns Clothing
    # return f"An object of type Clothing with id {id_value}. It is made from {fabric_value} fabric."

    #  Decor attributes: id(unique integer)