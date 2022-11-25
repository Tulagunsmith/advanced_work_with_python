documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_people(document):
    answer = True
    while answer:
        number = input('Введите номер документа: ')
        for person in document:
            if person['number'] == number:
                return person['name']
        else:
            print('Человек с таким номером документа не зарегистрирован.')
            answer = ask_again()
    if not answer:
        return 'Не найден.'


def ask_again():
    answer = (input('Повторить запрос? Д/Н ')).upper()
    return True if answer.startswith('Д') else False


def get_shelf(shelves):
    answer = True
    while answer:
        number = input('Введите номер документа: ')
        for shelf, document in shelves.items():
            if number in document:
                return shelf
        else:
            print('Такого документа нет ни на одной полке.')
            answer = ask_again()
    if not answer:
        return 'Не найдено.'


def get_list_documents(docs):
    for person in docs:
        for item in person.values():
            print(item, end=' ')
        print()


def add_person(docs, shelves):
    document_type = input('Введите тип документа: ')
    document_number = input('Введите номер документа: ')
    person_name = input('Введите имя и фамилию клиента: ')
    new_commer = dict()
    new_commer["type"] = document_type
    new_commer["number"] = document_number
    new_commer["name"] = person_name
    docs.append(new_commer)
    (shelves[get_shelf_number(directories)]).append(document_number)
    print('Данные добавлены.')


def get_shelf_number(catalogue):
    answer = True
    while answer:
        request = input('Введите номер полки, на которой будут храниться документы: ')
        if request in catalogue.keys():
            return request
        else:
            print(f'К сожалению, такой полки нет. Для вас доступны полки {" ".join(key for key in catalogue.keys())}')
            answer = ask_again()
    if not answer:
        request = '3'
        print('По умолчанию, документы будут сложены на 3-ю полку.')
        return request


def delete_doc(catalogue):
    request = delete_shelf_item(directories)
    while request:
        for person in catalogue:
            if request == person['number']:
                catalogue.remove(person)
                print('Данные удалены.')
                return

    if not request:
        print('Изменений не внесено.')


def delete_shelf_item(shelf):
    answer = True
    while answer:
        request = input('Введите номер документа, который необходимо удалить: ')
        for number, item in shelf.items():
            if request in item:
                item.remove(request)
                return request
        else:
            print('К сожалению, такого документа нет.')
            answer = ask_again()


def move_doc(shelves):
    doc = get_doc_number(directories)
    shelf = check_shelf_number(directories)
    if doc and shelf:
        for number, item in shelves.items():
            if doc in item and shelf in number:
                print('Вы пытаетесь переместить данные на то же место.')
                return
            if doc in item:
                item.remove(doc)
                break
        shelves[shelf].append(doc)
        print('Изменения внесены.')
    else:
        print('Такого документа или такой полки не существует. Попробуйте еще раз.')


def get_doc_number(shelves):
    document = input('Введите номер документа, который вы хотите переместить: ')
    for number, item in shelves.items():
        if document in item:
            return document


def check_shelf_number(shelves):
    shelf = input('Введите номер полки, на которую вы хотите переместить документ: ')
    for number, item in shelves.items():
        if shelf in number:
            return shelf


def add_shelf(shelves):
    new_shelf = input('Введите номер новой полки для документов: ')
    for number in shelves.keys():
        if new_shelf == number:
            print('Такая полка уже существует.')
            break
    else:
        shelves.setdefault(new_shelf, [])
        print('Изменения внесены.')


def user_help():
    print(
        'Список комманд:',
        '"p" - выведет имя человека по номеру документа',
        '"s" - выведет номер полки, на которой он находится документ',
        '"l" - выведет список всех документов',
        '"a" - добавит новый документ в каталог и в перечень полок',
        '"d" - спросит номер документа и удалит его из каталога и из перечня полок',
        '"m" - спросит номер документа и целевую полку и переместит его с текущей полки на целевую',
        '"as" - спросит номер новой полки и добавит ее в перечень',
        '"h" - выведет список команд',
        sep='\n'
    )


def lets_rock():
    user_help()
    while True:
        command = input('Введите вашу команду: ')
        if command == 'p':
            print(f'Владелец документа: {get_people(documents)}')
        elif command == 's':
            print(f'Документ на полке № {get_shelf(directories)}')
        elif command == 'l':
            get_list_documents(documents)
        elif command == 'a':
            add_person(documents, directories)
        elif command == 'd':
            delete_doc(documents)
        elif command == 'm':
            move_doc(directories)
        elif command == 'as':
            add_shelf(directories)
        elif command == 'h':
            user_help()
        elif command == 'q':
            print('Выход')
            break


print(lets_rock())
