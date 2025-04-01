import uuid

class Item:
    def __init__(self, id=None):
        # if no given id, generate uuid
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def get_category(self):
        # return class name
        return self.__class__.__name__
