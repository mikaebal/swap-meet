class Vendor:
    def __init__(self, item):
        self.inventory = []
        self.item = item

    def add_item(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.append(item)
            return item
    
    def remove_item(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    