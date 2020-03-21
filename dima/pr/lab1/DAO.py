import psycopg2
from psycopg2 import sql
import config
from models import argsError


class DAO:
    def __init__(self, table):
        self.conn = psycopg2.connect(dbname='pr_dima', user=config.user,
                                     password=config.password, host=config.host)
        self.conn.autocommit = True
        self.table = table
        self.key = None

    def check_exist_id(self, id):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT * FROM {} WHERE id = {};".format(self.table, id))
            cursor.execute(stmt)
            if not cursor.fetchone():
                raise IndexError("list index out of range")

    def get_all(self):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT * FROM {};".format(self.table))
            cursor.execute(stmt)
            return cursor.fetchall()

    def showFields(self):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT column_name FROM information_schema.columns "
                           "WHERE table_name = '{}';".format(self.table))
            cursor.execute(stmt)

            res = []
            for i in cursor.fetchall():
                res.append(i[0])

            return res

    def check_valid(self, dict):
        args = self.showFields()
        for i in dict:
            if not i in args:
                return False
        return True

    def create_request(self, dict):
        mass = ['', '']
        for i in dict:
            if mass[0] == '' and mass[1] == '':
                mass[0] = i
                if isinstance(dict[i], str):
                    mass[1] = "'{}'".format(dict[i])
                else:
                    mass[1] = "{}".format(dict[i])
            else:
                mass[0] = "{}, {}".format(mass[0], i)
                if isinstance(dict[i], str):
                    mass[1] = "{}, '{}'".format(mass[1], dict[i])
                else:
                    mass[1] = "{}, {}".format(mass[1], dict[i])

        return mass

    def __getitem__(self, key):
        self.check_exist_id(key)
        self.id = key
        return self

    def get_record(self):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT * FROM {} WHERE id = {};".format(self.table, self.id))
            cursor.execute(stmt)
            self.id = None
            return cursor.fetchone()

    def __setitem__(self, key, dict):
        if (not self.check_valid(dict)) and ('id' in dict):
            raise argsError('args not in table {} or id in dict'.format(self.table))
        if not key:
            raise IndexError('not indicate id')
        self.check_exist_id(key)
        if not self.check_valid(dict):
            raise argsError('args not in args table {}'.format(self.table))
        with self.conn.cursor() as cursor:
            for i in dict:
                if isinstance(dict[i], str):
                    field = "'{}'".format(dict[i])
                else:
                    field = dict[i]
                stmt = sql.SQL("UPDATE {} SET {} = {} WHERE id = {};".format(self.table, i, field, key))
                cursor.execute(stmt)

        self.key = None

    def __delitem__(self, key):
        self.check_exist_id(key)
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("DELETE FROM {} WHERE id = {};".format(self.table, key))
            cursor.execute(stmt)

    # if already exists raise psycopg2.errors.UniqueViolation
    def append(self, dict):
        if not self.check_valid(dict):
            raise argsError('args not in args table {}'.format(self.table))
        with self.conn.cursor() as cursor:
            request = self.create_request(dict)
            stmt = sql.SQL("INSERT INTO {}({}) VALUES({});".format(self.table, request[0], request[1]))
            cursor.execute(stmt)


class ClientDAO(DAO):
    def __init__(self):
        pass
    # дописать


if __name__ == '__main__':
    pass

