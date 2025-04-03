import uuid

class Item:
    def __init__(self, id=None, condition=0, category=""):
        self.condition = condition
        self.category = category

        # if no given id, generate uuid
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id


    def get_category(self):
        # return class name
        # return self.__class__.__name__
        return "Item"

    
    def condition_description(self):
        if self.condition <= 2:
            return "pre-loved"
        if 3 <= self.condition <= 4:
            return "good condition"
        if self.condition >= 5:
            return "like new!"

    def __str__(self):
        # stringify an instance of Item using str()
        # calling str() on a class instance will cause:
        # overriding, known as "operator overloading"
        # the same method exhibits different behavior across instances of different classes
        id = self.id
        item = self.__class__.__name__

        result = f"An object of type {item} with id {id}."
        return result