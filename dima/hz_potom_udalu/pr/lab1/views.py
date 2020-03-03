from psycopg2 import sql
import psycopg2
import config

from models import *

class View:
    def __init__(self, table):
        self.conn = psycopg2.connect(dbname='pr_dima', user=config.user,
                                     password=config.password, host=config.host)
        self.table = table

    def __convert_to_mass(self, typl):
        res = []
        for i in typl:
            res.append(i[0])

        return res

    def take_titles(self):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT column_name FROM information_schema.columns "
                           "WHERE table_name = '{}';".format(self.table))

            cursor.execute(stmt)

            return self.__convert_to_mass(cursor.fetchall())

    def response_fields(self, mass):
        if self.table[-1] == 's':
            table = self.table[:-1]
        else:
            table = self.table
        response = {table: ''}
        titles = self.take_titles()
        for i in range(len(mass)):
            response[titles[i]] = mass[i]

        return response

    def print_response(self, mass):
        response = self.response_fields(mass)
        for i in response:
            print('{}: {}'.format(i, response[i]))
        print()


class ClientView(View):
    def __init__(self):
        super().__init__('clients')


class ProcessorView(View):
    def __init__(self):
        super().__init__('processors')


class BasketView(View):
    def __init__(self):
        super().__init__('basket')


class OrderView(View):
    def __init__(self):
        super().__init__('orders')

if __name__ == '__main__':
    a = Client(4)
    ClientView().print_response(a.get_all())

    b = Processor(4)
    ProcessorView().print_response(b.get_all())

    c = Basket(4)
    BasketView().print_response(c.get_all())

    d = Order(3)
    OrderView().print_response(d.get_all())