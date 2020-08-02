import sys
from model.person import Person
from dao.base_dao import BaseDao

class PersonDao(BaseDao):
    def __init__(self):
        super().__init__(Person)

    def read(self, id = None):
        result = super().read(id)
        if type(result) == list:
            list_person = []
            for item in result:
                p = self.__obj_converter(item)
                list_person.append(p)
                return list_person
            return self.__obj_converter(result)

    def __obj_converter(self, item_str: str) -> Person:
        person = Person()
        obj_array = item_str.split(';')
        person.id = obj_array[0]
        person.name = obj_array[1]
        person.date_of_birth = obj_array[2]
        person.type_person = obj_array[3]
        person.cpf = obj_array[4]
        person.cnpj = obj_array[5]
        return person