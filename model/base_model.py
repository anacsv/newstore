class Base:
    def __init__(self, id:int = 0):
        self.__id = id

    # getters and setters
    @property
    def id(self)->int:
        return self.__id

    @id.setter
    def id(self, id:int)->None:
        self.__id = id
