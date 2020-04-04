from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from config import DATABASE


Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    balance = Column('balance', String, default=0)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Client('{}','{}','{}')>".format(self.id, self.name, self.balance)

def main():
    engine = create_engine(URL(**DATABASE), echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for client in session.query(Client).filter(Client.name.contains('a')).order_by(Client.balance)[::-1]:
        print(client)

if __name__ == '__main__':
    main()