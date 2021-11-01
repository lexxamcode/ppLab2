import json
import re


class Person(object):
    """
        Класс для одной записи с информацией с полями:
        Attributes
        --------
            telephone : string
                Поле для номера телефона
            weight : str
                Поле веса
            snils: string
                Снилс
            passport_series : str
                Серия паспорта
            occupation : str
                Поле профессии
            political_views : str
                 Политические предпочтения
            worldview : str
                Мировоззрение
            address : str
                Адресс
    """

    def __init__(self, telephone: str = '+7-(000)-000-00-00', weight: int = 0, snils: str = '00000000000',
                 passport_series: str = '00 00', occupation: str = 'None', age: int = 0,
                 political_views: str = 'None', worldview: str = 'None', address: str = 'None') -> None:
        """
        Parameters
        ---------
        telephone: str
            Параметр номера телефона
        weight: int
            Параметр веса
        snils: str
            Параметр снилса
        passport_series: str
            Параметр серии паспорта
        occupation: str
            Параметр профессии
        age: int
            Параметр возраста
        political_views: str
            Параметр политических предпочтений
        worldview: str
            Параметр мировоззрения
        address: str
            Параметр адресса
        """
        self.telephone = telephone
        self.weight = weight
        self.snils = snils
        self.passport_series = passport_series
        self.occupation = occupation
        self.age = age
        self.political_views = political_views
        self.worldview = worldview
        self.address = address


class Validator(object):
    collection: list
    """
        Класс-валидатор списка записей,
        который считывает записи из файла и 
        проводит их валидацию
        Attributes
        --------
            collection: list
                Контейнер записей типа Person
    """

    def __init__(self, path: str = None) -> None:
        """
        Конструктор класса-валидатора
        считывает из файла с путем path
        записи и сохраняет их в контейнер записей
        валидатора.
        Parameters
        ---------
        path: Путь к файлу с записями в формате JSON
        """
        if not path:
            return
        self.collection = []
        data = json.load(open(path, encoding='windows-1251'))
        for item in range(len(data)):
            new = Person()
            new.telephone = data[item]['telephone']
            new.weight = data[item]['weight']
            new.snils = data[item]['snils']
            new.passport_series = data[item]['passport_series']
            new.occupation = data[item]['occupation']
            new.age = data[item]['age']
            new.political_views = data[item]['political_views']
            new.worldview = data[item]['worldview']
            new.address = data[item]['address']

            self.collection.append(new)

    def __len__(self) -> int:
        return len(self.collection)

    # def validate(self) -> None:
       # for item in self.collection:
          #  match = re.match(r'\+7-\(9\d{2}\)-\d{3}-\d{2}-\d{2}', item.telephone)
           # if match is None:
            #    item.telephone = re.sub('a', '9', item.telephone)
            #    item.telephone = re.sub('^7', r'+7', item.telephone)
            #    item.telephone = re.sub(r'\(', r'-(', item.telephone)
            #    item.telephone = re.sub(r'\)', r')-', item.telephone)
            #    item.telephone = re.sub(r'--', '-', item.telephone)
            #    print(item.telephone + '\t<-')


if __name__ == '__main__':
    main_validator = Validator('82.txt')
    print(main_validator.collection[1].telephone)

    main_validator.validate()
