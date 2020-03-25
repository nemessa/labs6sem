from psycopg2 import sql
import psycopg2
import config


class argsError(Exception):
    pass

class lacksError(Exception):
    pass


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
                if isinstance(dict[i], str):
                    field = "'{}'".format(dict[i])
                else:
                    field = dict[i]
                if not field:
                    field = 'null'
                stmt = sql.SQL("UPDATE {} SET {} = {} WHERE id = {};".format(self.table, i, field, key))
                cursor.execute(stmt)

        self.key = None

    def __delitem__(self, key):
        self.check_exist_id(key)
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

    def toDict(self):
        record = self[self.id].get_record()
        titles = self.showFields()
        request = {}
        for i in range(len(titles)):
            request[titles[i]] = record[i]
        return request

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

    def get_last_order(self):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT * FROM orders ORDER BY id DESC;")
            cursor.execute(stmt)
            return cursor.fetchone()[0]

    def append_new_order(self):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("INSERT INTO orders(id, date_order) VALUES({}, null);".format(self.get_last_order() + 1))
            cursor.execute(stmt)

    def end_order(self, id_client):
        basket = Basket().get_basket(id_client)
        if basket:
            with self.conn.cursor() as cursor:
                stmt = sql.SQL("UPDATE orders SET date_order = NOW() WHERE id = {};".format(basket[-1][3]))

                cursor.execute(stmt)


class Processor(Model):
    def __init__(self):
        self.table = 'processors'
        super().__init__(self.table)

    def check_balance(self, proc, quant):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT balance FROM processors WHERE id = {};".format(proc))
            cursor.execute(stmt)
            return quant <= cursor.fetchone()[0]


    # Проверить эту функцию, сделать списание из ордера, где в ордере проходит по всем товарам
    # если остаток больше, то списывает, инчае ошибка
    def write_off(self, proc, quant):
        if self.check_balance(proc, quant):
            request = self[proc].toDict()
            request['balance'] -= quant
            self[proc] = request
        else:
            raise lacksError("Haven't pro")


class Basket(Model):
    def __init__(self):
        self.table = 'basket'
        super().__init__(self.table)

    def check_in_the_processors(self, id):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT * FROM processors "
                           " WHERE id = {} ;".format(id))
            cursor.execute(stmt)
            if not cursor.fetchall():
                raise lacksError("Lacks processors in the stocks")

    def check_in_the_clients(self, id):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT * FROM clients "
                           " WHERE id = {} ;".format(id))
            cursor.execute(stmt)
            if not cursor.fetchall():
                raise lacksError("Lacks clients in the stocks")

    def check_enough_on_stocks(self, id_client):
        basket = self.get_porc_from_basket(id_client)
        flag = True
        for i in basket:
            if not Processor().check_balance(i[0], i[-1]):
                flag = False
                break
        return flag

    def write_off_processors(self, id_client):
        basket = self.get_porc_from_basket(id_client)
        CPU = Processor()
        for i in basket:
            CPU.write_off(i[0], i[-1])

    def get_price(self, id_client):
        order = self.get_porc_from_basket(id_client)
        price = 0
        for i in order:
            price += i[-1] * i[-2]

        return price

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
                # _ o _
                #  \|/
                #  / \
                stmt = sql.SQL("SELECT * FROM basket INNER JOIN orders ON orders.id = id_order"
                               " WHERE id_client = {} AND orders.date_order IS null;".format(id_client))
                cursor.execute(stmt)
                responce = cursor.fetchone()
                if responce:
                    self.append({'id_processor': id_cpu, 'quantity': 1,
                                 'id_client': id_client, 'id_order': responce[-3]})
                else:
                    Order().append_new_order()
                    self.append({'id_processor': id_cpu, 'quantity': 1,
                                 'id_client': id_client, 'id_order': Order().get_last_order()})

    def remove_from_basket(self, id_cpu, id_client):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT basket.id, quantity, orders.id FROM basket INNER JOIN orders ON orders.id = id_order"
                           " WHERE id_processor = {} AND id_client = {} AND orders.date_order IS null;".format(id_cpu,
                                                                                                               id_client))
            cursor.execute(stmt)
            result = cursor.fetchone()
            if result:
                if result[1] > 1:
                    request = self[result[0]].toDict()
                    request['quantity'] -= 1
                    self[result[0]] = request
                elif result[1] == 1:
                    del self[result[0]]
                    if not self.get_basket(id_client):
                        del Order()[result[2]]

    # возвращает объединение корзины и заказа где id клиента есть в заказах
    def get_basket(self, id_client):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT * FROM basket INNER JOIN orders ON orders.id = id_order"
                           " WHERE id_client = {} AND orders.date_order IS null;".format(id_client))
            cursor.execute(stmt)
            return cursor.fetchall()

    #  yes yes porc, facepalm
    def get_porc_from_basket(self, id_client):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT processors.id, processors.name, processors.price, basket.quantity FROM basket "
                           "INNER JOIN processors ON processors.id = id_processor"
                           " WHERE id_client = {};".format(id_client))
            cursor.execute(stmt)
            return cursor.fetchall()


if __name__ == '__main__':
    a = Order()
    a.append_new_order()
