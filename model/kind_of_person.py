from .person import Person

class KindOfPerson(Person):
    def __init__(self, nome:str = '', date_of_birth:str = '', cpf:str = '', cnpj:str = '', id:int = 0):
        self.__cpf = cpf
        self.__cnpj = cnpj
        super().__init__(nome, date_of_birth, id)

    # getters and setters CPF
    @property
    def cpf(self)->str:
        return self.__cnpj

    @cpf.setter
    def cpf(self, cpf:str):
        self.__cpf = cpf

    # getters and setters CNPJ
    @property
    def cnpj(self)->str:
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj:str):
        self.__cnpj = cnpj

    # String interpolation
    def __str__(self):
        return f'{self.id, self.name, self.date_of_birth, self.__cpf, self.cnpj}'