import json
import argparse
from tqdm import tqdm
import time
import sys


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


if __name__ == '__main__':
    person = Person()
    help(Person.__init__)
