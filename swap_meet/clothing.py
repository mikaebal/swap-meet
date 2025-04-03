from .item import Item

# Clothing Class extends Item Class
class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown", condition=0.0):
        super().__init__(category="Clothing", condition=condition, id=id)
        self.fabric = fabric
        self.condition = condition

    
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