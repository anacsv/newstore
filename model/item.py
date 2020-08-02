from .base_model import Base

class Item(Base):
    def __init__(self, name: str = '', price: float = 0.0, description: str = '', id: int = 0):
        self.__name = name
        self.__price = price
        self.__description = description
        super().__init__(id)

    # Getters and Setters Name
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    # Getters and Setters Price
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        self.__price = price

    # Getters and Setters Description
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        self.__description = description

