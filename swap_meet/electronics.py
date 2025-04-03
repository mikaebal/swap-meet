from .item import Item

class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type


    def get_category(self):
        return self.__class__.__name__
        # return "Electronics"

    def __str__(self):
        id = self.id
        type = self.type
        result = f"An object of type Electronics with id {id}. This is a {type} device."
        return result