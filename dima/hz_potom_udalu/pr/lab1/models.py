from psycopg2 import sql
import psycopg2
import config


class Model:
    def __init__(self, table, id_db=None):
        self.conn = psycopg2.connect(dbname='pr_dima', user=config.user,
                                     password=config.password, host=config.host)
        self.conn.autocommit = True
        if id_db:
            with self.conn.cursor() as cursor:
                stmt = sql.SQL("SELECT id FROM {} WHERE id = {};".format(table, id_db))
                cursor.execute(stmt)
                if cursor.fetchone():
                    self.id = id_db
                else:
                    stmt = sql.SQL("INSERT INTO {}(id) VALUES ({});".format(table, id_db))
                    cursor.execute(stmt)
                    self.id = id_db
        else:
            with self.conn.cursor() as cursor:
                stmt = sql.SQL("INSERT INTO {}(id) VALUES (DEFAULT);".format(table))
                cursor.execute(stmt)

                stmt = sql.SQL("SELECT id FROM {} "
                               "ORDER BY id DESC "
                               "LIMIT 1;".format(table, id_db))
                cursor.execute(stmt)
                self.id = cursor.fetchone()[0]

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
            for i in cursor.fetchall()[1:]:
                res.append(i[0])

            return res

    def get_all(self):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT * FROM {} WHERE id = {};".format(self.table, self.id))
            cursor.execute(stmt)
            return cursor.fetchone()

    def getField(self, field):
        if field in self.showFields() + ['id']:
            with self.conn.cursor() as cursor:
                stmt = sql.SQL("SELECT {} FROM {} WHERE id = {};".format(field, self.table, self.id))
                cursor.execute(stmt)
                return cursor.fetchone()[0]
        else:
            return 'Error, you must select a field from the list of fields'

    def setField(self, field_name, field):
        if field_name != 'id' and field_name in self.showFields():
            with self.conn.cursor() as cursor:
                stmt = sql.SQL("UPDATE {} SET {} = '{}' WHERE id = {};".format(self.table, field_name, field, self.id))
                cursor.execute(stmt)
        else:
            return 'Error, you cannot enter id, or you must select a field from the list of fields'

    def kill(self):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("DELETE FROM {} WHERE id = {};".format(self.table, self.id))

            cursor.execute(stmt)

# один контроллер, самый верхний уровень с пользователем, проверяет на валидность
class Client(Model):
    def __init__(self, id_db=None):
        self.table = 'clients'
        super().__init__(self.table, id_db)

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
    def __init__(self, id_db=None):
        self.table = 'orders'
        super().__init__(self.table, id_db)


class Processor(Model):
    def __init__(self, id_db=None):
        self.table = 'processors'
        super().__init__(self.table, id_db)


class Basket(Model):
    def __init__(self, id_db=None):
        self.table = 'basket'
        super().__init__(self.table, id_db)

    def end_order(self, id_order):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("DELETE FROM {} WHERE id = {};".format(self.table, self.id))

            cursor.execute(stmt)



if __name__ == '__main__':
    '''a = Client(2)
    print(a.getField('name'))
    a.setField('name', 'pri')
    print(a.getField('name'))
    #a.kill()

    b = Order(12)
    print(b.getField('id'))
    b.setField('date_order', '1999-01-08')
    print(b.getField('date_order'))
    b.kill()

    c = Processor(12)
    print(c.getField('name'))
    c.setField('name', 'pri')
    print(c.getField('name'))
    c.kill()

    d = Basket(12)
    print(d.getField('id_client'))
    d.setField('quantity', 12)
    print(d.getField('quantity'))
    d.kill()'''

    client = Client(1)
    print(client.enough_balance(10000))
