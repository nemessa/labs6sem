from models import *
from views import *

class Controller:
    def show_processor(self, id):
        CPU = Processor()
        View().print_response(CPU.table, CPU[id].get_record(), CPU.showFields())

    def show_processors(self):
        CPU = Processor()
        View().print_responses(CPU.table, CPU.get_all(), CPU.showFields())

    def setField(self, field_name, field):
        id = self.id
        self.id = None
        return self.model[id].setField(field_name, field)

    def getField(self, field):
        return self.model.getField(field)

    def get_all(self):
        return self.model.get_all()

    def kill(self, table, id):
        self.model().kill()



if __name__ == '__main__':
    a = Controller()
    a.show_processors()




