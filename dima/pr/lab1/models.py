from psycopg2 import sql
import psycopg2
import config

class argsError(Exception):
    pass
# поменять всё на индексы, доделать изменение и удаления по словарю
# доделать проверку на баланс

class Model:
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

    def __getitem__(self, key):
        self.check_exist_id(key)
        self.id = key
        return self

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
                stmt = sql.SQL("UPDATE {} SET {} = {} WHERE id = {};".format(self.table, i, dict[i], key))
                cursor.execute(stmt)

        self.key = None

    def __delitem__(self, key):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("DELETE FROM {} WHERE id = {};".format(self.table, key))
            cursor.execute(stmt)

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
                    mass[1] = '"{}"'.format(dict[i])
                else:
                    mass[1] = "{}".format(dict[i])
            else:
                mass[0] = "{}, {}".format(mass[0], i)
                if isinstance(dict[i], str):
                    mass[1] = '{}, "{}"'.format(mass[1], dict[i])
                else:
                    mass[1] = "{}, {}".format(mass[1], dict[i])

        return mass

    # if already exists raise psycopg2.errors.UniqueViolation
    def append(self, dict):
        if not self.check_valid(dict):
            raise argsError('args not in args table {}'.format(self.table))
        with self.conn.cursor() as cursor:
            request = self.create_request(dict)
            stmt = sql.SQL("INSERT INTO {}({}) VALUES({});".format(self.table, request[0], request[1]))
            cursor.execute(stmt)

    def _rollback(self):
        with self.conn.cursor() as cursor:
            cursor.execute('rollback;')

    def _get_tables(self):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT table_name FROM information_schema.tables"
                           " WHERE table_schema NOT IN ('information_schema','pg_catalog');")

            cursor.execute(stmt)
            return list(cursor.fetchall())

    def showFields(self):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT column_name FROM information_schema.columns "
                           "WHERE table_name = '{}';".format(self.table))
            cursor.execute(stmt)

            res = []
            for i in cursor.fetchall():
                res.append(i[0])

            return res

    def get_record(self):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT * FROM {} WHERE id = {};".format(self.table, self.id))
            cursor.execute(stmt)
            self.id = None
            return cursor.fetchone()

    def get_all(self):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT * FROM {};".format(self.table))
            cursor.execute(stmt)
            return cursor.fetchall()

    def getField(self, field):
        if not self.id:
            raise IndexError('not indicate id')
        if field in self.showFields():
            with self.conn.cursor() as cursor:
                stmt = sql.SQL("SELECT {} FROM {} WHERE id = {};".format(field, self.table, self.id))
                cursor.execute(stmt)
                self.key = None
                return cursor.fetchone()[0]
        else:
            self.key = None
            return 'Error, you must select a field from the list of fields'

    def setField(self, field_name, field):
        if not self.id:
            raise IndexError('not indicate id')
        if field_name in self.showFields():
            with self.conn.cursor() as cursor:
                stmt = sql.SQL("UPDATE {} SET {} = '{}' WHERE id = {};".format(self.table, field_name, field, self.id))
                cursor.execute(stmt)
        else:
            return 'Error, you cannot enter id, or you must select a field from the list of fields'
        self.key = None


# один контроллер, самый верхний уровень с пользователем, проверяет на валидность
class Client(Model):
    def __init__(self):
        self.table = 'clients'
        super().__init__(self.table)

    def enough_balance(self, price):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT balance FROM clients WHERE id={}".format(self.id))

            cursor.execute(stmt)

            return price <= cursor.fetchone()[0]

    def pay(self, price):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("UPDATE clients SET balance = clients.balance - {} WHERE id = {}".format(price, self.id))

            cursor.execute(stmt)


class Order(Model):
    def __init__(self):
        self.table = 'orders'
        super().__init__(self.table)

    def end_order(self, id_client):
        basket = Basket().get_basket(id_client)
        if basket:
            with self.conn.cursor() as cursor:
                stmt = sql.SQL("UPDATE orders SET date_order = clock_timestamp() WHERE id = {};".format(basket[-1][3]))

                cursor.execute(stmt)


class Processor(Model):
    def __init__(self):
        self.table = 'processors'
        super().__init__(self.table)


class Basket(Model):
    def __init__(self):
        self.table = 'basket'
        super().__init__(self.table)

    # реализация в 3 и 4 лабах
    def add_to_basket(self, id_cpu, id_client):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT * FROM basket INNER JOIN orders ON orders.id = id_order"
                           " WHERE id_processor = {} AND id_client = {} AND orders.date_order IS null;".format(id_cpu,
                                                                                                               id_client))
            cursor.execute(stmt)
            responce = cursor.fetchone()
            if responce:
                self[responce[0]] = {'quantity': responce[2] + 1}
            else:
                stmt = sql.SQL("SELECT * FROM basket INNER JOIN orders ON orders.id = id_order"
                               " WHERE id_client = {} AND orders.date_order IS null;".format(id_client))
                cursor.execute(stmt)
                self.append({'id_processor': id_cpu, 'quantity': 1,
                             'id_client': id_client, 'id_order': cursor.fetchone()[-3]})

    def get_basket(self, id_client):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT * FROM basket INNER JOIN orders ON orders.id = id_order"
                           " WHERE id_client = {} AND orders.date_order IS null;".format(id_client))
            cursor.execute(stmt)
            return cursor.fetchall()

    def pri

if __name__ == '__main__':

    a = Basket()
    print(a.get_basket(2))