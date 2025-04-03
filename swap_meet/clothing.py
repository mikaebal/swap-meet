from .item import Item

class Clothing(Item):
    def __init__(self, id, fabric="Unknown"):
        self.fabric = fabric
        super().__init__(self, id=None)
    
    # on item.py
    # Clothing attributes: id, fabric (default "Unknown")
    
    
    # return f"An object of type Clothing with id {id_value}. It is made from {fabric_value} fabric."
    def get_category(self):
        # return self.__class__.__name__
        return "Clothing"

    # has a function get_category to returns Clothing
    def __str__(self):
        id = self.id
        fabric = self.fabric
        
        result = f"An object of type Clothing with id {id}. It is made from {fabric} fabric."
        return result