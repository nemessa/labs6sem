import sympy

class Alph:
    def __init__(self):
        self. alph = '01'

    def razl(self, sump):
        res = sympy.Symbol('E')
        step = sump
        for i in range(1):
            res += step
            step *= sump
        #print(res)
        return res

    def comp(self, left, right):
        if not(left and right):
            return None
        else:
            return left + right

    def chet(self):
        x = sympy.Symbol('0')
        y = sympy.Symbol('1')
        a = self.razl(x) + y + self.razl(x) + y + self.razl(x)
        sympy.pprint(a)
        ish = self.razl(a).expand()
        sympy.pprint(ish)

if __name__ == '__main__':
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    a = 1 + x + y
    Alph().chet()