from models import *
from views import *

class Controller:
    def show_processor(self, id):
        CPU = Processor()
        View().print_response(CPU.table, CPU[id].get_record(), CPU.showFields())

    def show_processors(self):
        CPU = Processor()
        View().print_responses(CPU.table, CPU.get_all(), CPU.showFields())

    def show_basket(self, id_client):
        basket = Basket().get_porc_from_basket(id_client)
        titles = ['id', 'name', 'price', 'quantity']
        View().print_responses(Basket().table, basket, titles)

    def add_to_basket(self, id_cpu, id_client):
        Basket().check_in_the_clients(id_client)
        Basket().check_in_the_processors(id_cpu)
        Basket().add_to_basket(id_cpu, id_client)

    # end
    def remove_from_basket(self, id_cpu, id_client):
        Basket().check_in_the_clients(id_client)
        Basket().check_in_the_processors(id_cpu)
        Basket().remove_from_basket(id_cpu, id_client)

    def buy(self, id_client):
        basket = Basket()
        client = Client()
        view = View()

        if client[id_client].enough_balance(basket.get_price(id_client)):
            if basket.check_enough_on_stocks(id_client):
                Order().end_order(id_client)
                client[id_client].pay(basket.get_price(id_client))
                basket.write_off_processors(id_client)
            else:
                view.print_error('insufficient processors in the stocks')
        else:
            view.print_error('insufficient funds in the account')

    def setField(self, field_name, field):
        id = self.id
        self.id = None
        return self.model[id].setField(field_name, field)

    def getField(self, field):
        return self.model.getField(field)

    def get_all(self):
        return self.model.get_all()




if __name__ == '__main__':
    a = Controller()
    a.buy(3)





