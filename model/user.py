class User:
    def __init__(self, email: str = '', password: str = '', id : int = None):
        self.__id = id
        self.__email = email
        self.__password = password

    # Getters and Setters Id
    @property
    def id(self) -> None:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    # Getters and Setters Email
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email

    # Getters and Setters
    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password

    # String interpolation
    def __str__(self):
        return f'{self.__id};{self.__email};{self.__password}'