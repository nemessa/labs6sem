#здесь всё что должен увидеть клиент список товаров/ время ожидания и т.п.
from controller import *

class View:
    def __init__(self):
        self.a = Controller('product')

    def output(self):
        print(self.a.output_chek('product'))

if __name__ == '__main__':
    pass