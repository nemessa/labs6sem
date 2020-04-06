#удаление обновление проверки сделать

from sqlalchemy import Column, Integer, String, create_engine, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import insert, update, delete

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employee'

    employee_id = Column(Integer, primary_key=True)
    login = Column('login', String)
    employee_addresses_gps = Column('employee_addresses_gps', Integer)

    # def __init__(self, login):
    # self.login = login

    def __repr__(self):
        return r"""Employee: {
        employee_id: %s
        login: %s
        employee_addresses_gps: %s
}""" % (self.employee_id, self.login, self.employee_addresses_gps)

    def add_employee(self, employee_id, login, employee_addresses_gps):
        inc = Employee(employee_id=employee_id, login=login, employee_addresses_gps=employee_addresses_gps)
        session.add(inc)
        session.commit()

    def del_employee(self, emloyee_id):
        dell = Employee.delete()

class Person(Base):
    __tablename__ = 'person'

    person_id = Column(Integer, primary_key=True)
    login = Column('login', String)
    amount_money = Column('amount_money', Integer, default=0)
    addresses_gps = Column('addresses_gps', Integer)

    # def __init__(self, login):
    # self.login = login

    def __repr__(self):
        return r"""Person: {
        person_id: %s
        login: %s
        amount_money: %s
        addresses_gps: %s
}""" % (self.person_id, self.login, self.amount_money, self.addresses_gps)

    def add_person(self, person_id, login, amount_money, addresses_gps):
        inc = Person(person_id=person_id, login=login, amount_money=amount_money, addresses_gps=addresses_gps)
        session.add(inc)
        session.commit()


class Product(Base):
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key=True)
    product_name = Column('product_name', String)

    # def __init__(self, product_name):
    # self.product_name = product_name

    def __repr__(self):
        return r"""Product: {
        product_id: %s
        product_name: %s
}""" % (self.product_id, self.product_name)

    def add_product(self, product_id, product_name):
        inc = Product(product_id=product_id, product_name=product_name)
        session.add(inc)
        session.commit()

class Store(Base):
    __tablename__ = 'store'

    store_id = Column(Integer, primary_key=True)
    name_store = Column('name_store', String)
    store_addresses_gps = Column('store_addresses_gps', Integer)

    # def __init__(self, login):
    # self.login = login

    def __repr__(self):
        return r"""Store: {
        store_id: %s
        name_store: %s
        store_addresses_gps: %s
}""" % (self.store_id, self.name_store, self.store_addresses_gps)

    def add_store(self, store_id, name_store, store_addresses_gps):
        inc = Store(store_id=store_id, name_store=name_store, store_addresses_gps=store_addresses_gps)
        session.add(inc)
        session.commit()


if __name__ == '__main__':
    engine = create_engine('postgresql://user_1:password@62.109.15.226/databses_kur', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    a = Employee()
    a.add_employee2(4, 'DURAK', 7)

    for employee in session.query(Employee):
        print(employee)

    for person in session.query(Person):
        print(person)

    for product in session.query(Product):
        print(product)

    for store in session.query(Store):
        print(store)
