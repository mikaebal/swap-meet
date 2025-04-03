from .item import Item

class Decor(Item):
    def __init__(self, id=None, width=0, length=0, condition=0):
        super().__init__(id, condition)
        self.width = width
        self.length = length

    def get_category(self):
        return self.__class__.__name__
        # return "Clothing"
    
    def __str__(self):
        id = self.id
        width = self.width
        length = self.length
        result = f"An object of type Decor with id {id}. It takes up a {width} by {length} sized space."
        return result
    # super? "using inheritance" --- YES
    # unique integer id is in item.py
    # Holds 2 integer attributes width and length
    # get_category is in item.py
    # Decor attributes: id(unique integer)
