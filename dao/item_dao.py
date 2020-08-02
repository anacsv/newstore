from model.item import Item
from dao.base_dao import BaseDao

class ItemDao(BaseDao):

    def __init__(self):
        super().__init__(Item)

    def read(self, id = None):
        result = super().read(id)
        if type(result) == list:
            list_item = []
            for it in result:
                item = self.__create_object(it)
                list_item.append(item)
                return list_item
            return self.__create_object(result)

    def __create_object(self, it_str: str) -> Item:
        item = Item()
        obj_array = it_str.split(';')
        item.id = obj_array[0]
        item.name = obj_array[1]
        item.price = obj_array[2]
        item.description = obj_array[3]
        return item


