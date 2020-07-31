from .base_model import Base

class Person(Base):
    def __init__(self, name:str = '', date_of_birth:str = '', id:int = 0):
        self.__name = name
        self.__date_of_birth = date_of_birth
        super().__init__(name, date_of_birth, id)

    # Getters and Setters Name
    @property
    def name(self)->str:
        return self.__name

    @name.setter
    def name(self, name:str):
        self.__name = name

    # Getters and Setters Date of Birth
    @property
    def date_of_birth(self)->str:
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth:str):
        self.__date_of_birth = date_of_birth

