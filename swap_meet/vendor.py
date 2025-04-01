class Vendor:
    # pass


    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    # part of wave 2
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    # wave 4
    def swap_first_item(self, other_vendor):
        # check if self or other has empty inventory
            # if yes return False bc can't swap if empty
        # store both self and other first item in temp variable
        # remove self and other first item from inventory 
        # add other first item to self inventory 
        # add self first item to other inventory 
        # return True
