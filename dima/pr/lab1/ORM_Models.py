from sqlalchemy import Column, Integer, String, create_engine, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.engine.url import URL
from config import DATABASE


Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    balance = Column('balance', Integer, default=0)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return r"""Client: {
    id: %s,
    name: %s,
    balance: %s
}""" % (self.id, self.name, self.balance)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    date_order = Column('date_order', Date)

    def __init__(self):
        self.date_order = None

    def __repr__(self):
        return """Order{
    id: %s,
    date_order: %s
}""" % (self.id, self.date_order)


class Processor(Base):
    __tablename__ = 'processors'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    price = Column(Integer)
    clock = Column(Integer)
    cores = Column(Integer)
    threads = Column(Integer)
    l1_cache = Column(Integer)
    l2_cache = Column(Integer)
    l3_cache = Column(Integer)
    process_t = Column(Integer)
    balance = Column(Integer, default=0)

    def __init__(self, **kwargs):
        for i in kwargs:
            eval('self.{} = {}'.format(i, kwargs[i]))

    def __repr__(self):
        return """Processor{
    id: %s,
    name: '%s',
    price: %s,
    clock: %s,
    cores: %s,
    threads: %s,
    l1_cache: %s,
    l2_cache: %s,
    l3_cache: %s,
    process_t: %s,
    balance: %s
}""" % (self.id, self.name, self.price, self.clock, self.cores, self.threads,
        self.l1_cache, self.l2_cache, self.l3_cache, self.process_t, self.balance)


class Basket(Base):
    __tablename__ = 'basket'

    id = Column(Integer, primary_key=True)
    id_processor = Column(Integer, ForeignKey('processors.id'))
    quantity = Column(Integer)
    id_client = Column(Integer, ForeignKey('clients.id'))
    id_order = Column(Integer, ForeignKey('orders.id'))

    def __init__(self, id_processor, quantity, id_client, id_order):
        id_processor = id_processor
        quantity = quantity
        id_client = id_client
        id_order = id_order

    def __repr__(self):
        return """Order{
    id: %s,
    id_processor = %s,
    quantity = %s,
    id_client = %s,
    id_order = %s
}""" % (self.id, self.id_processor, self.quantity, self.id_client, self.id_order)


def main():
    engine = create_engine(URL(**DATABASE), echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for client in session.query(Client):
        print(client)

    for order in session.query(Order):
        print(order)

    for processor in session.query(Processor):
        print(processor)



    for basket in session.query(Basket, Processor).join(Basket.id_processor == Processor.id):
        print(basket)

if __name__ == '__main__':
    main()