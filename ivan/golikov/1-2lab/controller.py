from model import *

class Controller():

    def __init__(self, table):
        self.a = Model(table)

    def output_chek(self):
        result = self.a.check()
        return result
        

if __name__ == '__main__':
    pass