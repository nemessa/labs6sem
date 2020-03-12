from models import *
from views import *

class Controller:
    def __init__(self, table):
        self.table = table

    def updateView(self):
        self.view.print_response(self.model.get_all())

    def setField(self, field_name, field):
        return self.model.setField(field_name, field)

    def getField(self, field):
        return self.model.getField(field)

    def get_all(self):
        return self.model.get_all()

    def kill(self):
        self.model.kill()

class ClientController(Controller):
    def __init__(self, id_db=None):
        super().__init__('clients')
        self.model = Client(id_db)
        self.view = ClientView()


class ProcessorController(Controller):
    def __init__(self, id_db=None):
        super().__init__('processors')
        self.model = Processor(id_db)
        self.view = ProcessorView()


class BasketController(Controller):
    def __init__(self, id_db=None):
        super().__init__('basket')
        self.model = Basket(id_db)
        self.view = BasketView()


class OrderController(Controller):
    def __init__(self, id_db=None):
        super().__init__('orders')
        self.model = Order(id_db)
        self.view = OrderView()

if __name__ == '__main__':
    a = ClientController(4)
    a.updateView()
    a.setField('name', a.getField('name') + ' zad')

    e = ClientController()
    e.kill()

    b = ProcessorController(4)
    b.updateView()

    c = BasketController(4)
    c.updateView()

    d = OrderController(3)
    d.updateView()


