from psycopg2 import sql
import psycopg2
import config

from models import *

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
        print(table)
        for i in mass:
            response = self.response_field(i, fields)
            for i in response:
                print('{}: {}'.format(i, response[i]))
            print()


if __name__ == '__main__':
    pass
