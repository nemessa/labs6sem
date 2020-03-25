from psycopg2 import sql
import psycopg2
import config

from models import *

'''Пользователь видит список процессоров +++
Пользователь может посмотреть список товаров в корзине +++
Пользователь может добавить в корзину товар, увеличить его количество в корзине, удалить из корзины +++
При нажатии кнопки оплатить идет проверка на количество денег, если денег хватает, то идет проверка на наличие на складе +++
если хватает денег и хватает товаров на складе
то товар спиывается со склада, у пользователя списываются деньги за товар, в поле дата заказа появляется NOW()'''

class View:
    def __convert_to_mass(self, typl):
        res = []
        for i in typl:
            res.append(i[0])

        return res

    def response_field(self, mass, fields):
        response = {}
        for i in range(len(mass)):
            response[fields[i]] = mass[i]

        return response

    def print_response(self, table, mass, fields):
        if table[-1] == 's':
            table = table[:-1]
        else:
            table = table
        print(table)
        response = self.response_field(mass, fields)
        for i in response:
            print('{}: {}'.format(i, response[i]))
        print()

    def print_responses(self, table, mass, fields):
        print(table, ': ')
        for i in mass:
            response = self.response_field(i, fields)
            for i in response:
                print('{}: {}'.format(i, response[i]))
            print()

    def print_error(self, text):
        print('Error: {}'.format(text))


if __name__ == '__main__':
    pass
