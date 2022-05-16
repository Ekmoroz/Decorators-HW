import datetime
import functools

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def upper(way):
    def decor(func):
        """
        Date, time, name, args, return
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            date, time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S").split()
            with open(f'{way}\\func_call.txt', 'w') as f:
                f.write(str({'Date': date, 'Time': time, 'Name': func.__name__, 'Arguments': args, 'Return': func(*args, **kwargs)}))
            return func(*args, **kwargs)
        return wrapper
    return decor


to_go = input("Enter path to save: ")
# /Users/katerinamorozova/Documents/PYTHON/Project-Decorator


@upper(to_go)
# add
def new_document(number, typ, name, shelf):
    res = 'Такой полки не существует'
    for k in directories.keys():
        if k == shelf:
            new_dict = {"type": typ, "number": number, "name": name}
            documents.append(new_dict)
            directories[k].append(number)
            res = 'Документ номер ' + number + ' добавлен на полку ' + shelf
    return res


print(new_document('25', 'passport', 'kate', '3'))
