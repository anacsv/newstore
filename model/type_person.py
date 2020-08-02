from .person import Person


class TypePerson(Person):
    def __init__(self, nome: str = '', date_of_birth: str = '', cpf: str = '', cnpj: str = '', type_person: str = '', id:int = 0):
        self.__cpf = cpf
        self.__cnpj = cnpj
        super().__init__(nome, date_of_birth, id)

    # Getters and Setters CPF
    @property
    def cpf(self)->str:
        return self.__cnpj

    @cpf.setter
    def cpf(self, cpf:str):
        self.__cpf = cpf

    # Getters and Setters CNPJ
    @property
    def cnpj(self)->str:
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj:str):
        self.__cnpj = cnpj

    # Getters and Setters Type Person
    @property
    def type_person(self) -> str:
        return self.__type_person

    @type_person.setter
    def type_person(self, type_person: str):
        self.__type_person = type_person

    # String interpolation
    def __str__(self):
        return f'{self.id, self.name, self.date_of_birth, self.__cpf, self.cnpj, self.__type_person}'