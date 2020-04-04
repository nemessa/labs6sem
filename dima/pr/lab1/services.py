from ORM_Models import Client, Processor, Basket, Order
from config import DATABASE
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, update

from models import lacksError

'''
Пользователь видит список процессоров +++
Пользователь может посмотреть список товаров в корзине +++
Пользователь может добавить в корзину товар, увеличить его количество в корзине, удалить из корзины +++
При нажатии кнопки оплатить идет проверка на количество денег, если денег хватает, то идет проверка на наличие на складе +++
если хватает денег и хватает товаров на складе
то товар спиывается со склада, у пользователя списываются деньги за товар, в поле дата заказа появляется NOW()
'''
'''
Менеджер может менять хар-ки товаров и добавлять | удалять товары
Кладовщик может изменять кол-во товаров на складе
'''


class ClientService:
    @staticmethod
    def show_processors():
        return [processor for processor in session.query(Processor)]

    def get_proc_from_basket(self, id_client):
        return [[processor.id, processor.name, processor.price, basket.quantity] for processor,
                                                                                     basket in
                session.query(Processor, Basket). \
                    filter(Basket.id_processor == Processor.id, Basket.id_client == id_client)]

    # Возвращает json всех объектов к орзине
    def show_basket(self, id_client):
        response = []
        for i in self.get_proc_from_basket(id_client):
            response.append('''Processor: {
    id: %s,
    name: %s,
    price: %s,
    quantity: %s
}''' % (i[0], i[1], i[2], i[3]))
        return response

    # Исключение
    @staticmethod
    def check_in_the_clients(id_client):
        if not session.query(Client).filter(Client.id == id_client).first():
            raise lacksError("Client does not exists")

    # Исключение
    @staticmethod
    def check_in_the_processors(id_processor):
        if not session.query(Processor).filter(Processor.id == id_processor).first():
            raise lacksError("Processor does not exists")

    def add_to_basket(self, id_processor, id_client):
        self.check_in_the_processors(id_processor)
        self.check_in_the_clients(id_client)
        proc_from_basket = session.query(Basket, Order).filter(Basket.id_order == Order.id,
                                                               Basket.id_client == id_client,
                                                               Basket.id_processor == id_processor,
                                                               Order.date_order == None).all()
        if proc_from_basket:
            proc_from_basket[0][0].quantity += 1
            session.commit()
        else:
            response = session.query(Basket, Order).filter(Basket.id_order == Order.id,
                                                           Basket.id_client == id_client,
                                                           Order.date_order == None).all()
            if response:
                field = Basket(id_processor, 1, id_client, response[0][1].id)
                session.add(field)
                session.commit()
            else:
                order = Order()
                session.add(order)
                session.commit()
                field = Basket(id_processor, 1, id_client, session.query(Order).all()[-1].id)
                session.add(field)
                session.commit()

    def remove_from_basket(self):
        pass


if __name__ == '__main__':
    engine = create_engine(URL(**DATABASE), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    ClientService().add_to_basket(3, 1)
