from AccountingBase import directories, documents


class Accounting:

    def __init__(self, document, directory):
        self.document = document
        self.directory = directory

    def get_human_doc(self, doc_number):
        # doc_number = input('Введите номер документа: ')
        result = 'Номер документа введен неверно!'
        for doc in self.document:
            if doc_number == doc['number']:
                name = doc['name']
                return f'Владелец документа: {name}'
        return result

    def get_doc_shelf(self, doc_number):
        # doc_number = input('Введите номер документа: ')
        result = 'Номер документа введен неверно!'
        for shelf in self.directory.items():
            if doc_number in shelf[1]:
                return f'Документ сохранён на {shelf[0]} полке.'
        return result

    def get_doc_list(self):
        for all_docs in self.document:
            doc_type = all_docs['type']
            doc_number = all_docs['number']
            doc_owner = all_docs['name']
            print(f'{doc_type} "{doc_number}" "{doc_owner}"')

    def add_new_doc(self, doc_number, doc_type, doc_owner, doc_shelf):
        # doc_number = input('Введите номер документа: ')
        # doc_type = input('Введите тип документа: ')
        # doc_owner = input('Введите имя владельца: ')
        new_doc = {"type": doc_type, "number": doc_number, "name": doc_owner}
        for doc in self.document:
            if doc['type'] == doc_type and doc['number'] == doc_number and doc['name'] == doc_owner:
                return 'Такой документ уже существует.'
        # doc_shelf = input('Введите номер полки для хранения: ')
        if doc_shelf in self.directory.keys():
            list1 = self.directory[doc_shelf]
            list1.append(doc_number)
            self.document.append(new_doc)
            return f'Новый документ успешно добавлен и сохранён на {doc_shelf} полке!'
        else:
            return 'Извините, но такой полки не существует.'

    def delete_doc(self, doc_number):
        # doc_number = input('Введите номер документа: ')
        for doc in self.document:
            if doc_number == doc['number']:
                self.document.remove(doc)
                for list_1 in self.directory.values():
                    if doc_number in list_1:
                        list_1.remove(doc_number)
                        return 'Документ удалён.'
        return 'Такого документа не существует!'

    def move_doc(self, doc_number, doc_shelf):
        # doc_number = input('Введите номер документа: ')
        result = 'Такого документа не существует!'
        for doc in self.document:
            if doc_number == doc['number']:
                # doc_shelf = input('Введите новый номер полки для хранения: ')
                if doc_shelf not in self.directory:
                    return 'Такой полки не существует!'
                elif doc_shelf in self.directory.keys() and doc_number in self.directory[doc_shelf]:
                    return 'Документ уже сохранён на этой полке.'
                else:
                    for list_1 in self.directory.values():
                        if doc_number in list_1:
                            list_1.remove(doc_number)
                    self.directory[doc_shelf].append(doc_number)
                    return f'Документ успешно перенесён на {doc_shelf} полку!'
        return result

    def add_new_shelf(self, doc_shelf):
        # doc_shelf = input('Введите номер полки для добавления: ')
        if doc_shelf in self.directory.keys():
            return 'Такая полка уже существует.'
        else:
            self.directory.setdefault(doc_shelf, [])
            return 'Новая полка успешно добавлена!'


def main_function(document, directory):
    user = Accounting(document, directory)
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            print(user.get_human_doc(''))
            print()
        elif user_input == 's':
            print(user.get_doc_shelf(''))
            print()
        elif user_input == 'l':
            user.get_doc_list()
            print()
        elif user_input == 'a':
            print(user.add_new_doc('', '', '', ''))
            print()
            print(documents)
            print(directories)
        elif user_input == 'as':
            print(user.add_new_shelf(''))
            print()
            print(documents)
            print(directories)
        elif user_input == 'm':
            print(user.move_doc('', ''))
            print()
            print(documents)
            print(directories)
        elif user_input == 'd':
            print(user.delete_doc(''))
            print()
            print(documents)
            print(directories)
        else:
            print('Такой команды не существует!')
            print()


# if __name__ == '__main__':
    # print(main_function())
