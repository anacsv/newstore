def __init__(self, class_):
    # Create and nominate archive in the database
    self.__path_archive = f'newstore/dao/db/{class_.__name__}.txt'

    # CRUD - Create
    def create(self, model):
        fields_missing = self.__validate_fields(model)
        if len(fields_missing) > 0:
            return 'error'
        with open(self.__path_archive, a) as file:
            file.write(str(model)+"\n")
        return 'Save'

    # Ready by Id
    def __read_by_id(self, id, lines):
        index = self.__find_by_id(id, lines)
        if index >= 0:
            item = lines[index]
            return item.strip()
        return 'Not found'

    # Find by id
    def __find_by_id(self, id, lines, model = None):
        for line in lines:
            line_id = line.split(';')[0]
            if line_id == str(id):
                index = lines.index(line)
                return index

    # Read all
    def __read_all(self, lines) -> list:
        formated = []
        for line in lines:
            formated .append(line.strip())
            return formated

    # CRUD - Read
    def read(self, id = None):
        lines = self.__read_file()
        if id:
            return self.__read_by_id(id, lines)
        return self.__read_all(lines)

    # CRUD - Update
    def update(self, model):
        fields_missing = self.__validate_fields(model)
        if len(fields_missing) > 0:
            return 'error'
        lines = self.__read_file()
        if lines:
            index = self.__find_by_id(model.id, lines, model)
            lines.pop(index)
            line = str(model)+"\n"
            lines.insert(index, line)
            self.__rewrite_file(lines)
            return 'Successfully changed'
        return 'Empty document'

    # CRUD - Delete
    def delete(self, id):
        lines = self.__read_file()
        if lines:
            index = self.__find_by_id(id, lines)
            lines.pop(index)
            self.__rewrite_file(lines)
            return 'Successfully deleted'
        return 'Empty document'

    def __rewrite_file(self, lines):
        with open(self.__path_archive, 'w') as file:
            file.writelines(lines)

    def __read_file(self):
        with open(self.__path_archive, 'r') as file:
            lines = file.readlines()
            return lines



