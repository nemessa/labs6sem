from psycopg2 import sql
import psycopg2
import config

class Model:
    def __init__(self):
        self.conn = psycopg2.connect(dbname='pr_dima', user=config.user,
                                     password=config.password, host=config.host)

    def _rollback(self):
        with self.conn.cursor() as cursor:
            cursor.execute('rollback;')

    def _beautiful_change(self, mass):
        new_mass = []
        for i in mass:
            new_mass.append(i[0])
        return new_mass

    def _get_tables(self):
        with self.conn.cursor() as cursor:
            stmt = sql.SQL("SELECT table_name FROM information_schema.tables"
                           " WHERE table_schema NOT IN ('information_schema','pg_catalog') AND "
                           "table_name NOT LIKE '%_old';")

            cursor.execute(stmt)
            return self._beautiful_change(cursor.fetchall())


if __name__ == '__main__':
    print('Hello Wrold!!!')
    print(Model()._get_tables())
