class Qyest:
    def __init__(self):
        self.plus = None
        self.multiply = None
        self.increase = None

    def inc(self, mass, depth):
        res = [['E']]
        for i in range(depth - 1):
            if len(res) == 1:
                res.append(mass)
            else:
                res += [self.mul(res[-1], mass)]

        '''result = []
        for i in res[1:]:
            result.append(i[0])
        return result'''
        return res

    def mul(self, left, right):
        every_step = [left.copy() for i in range(len(right))]
        for i in range(len(right)):
            for j in range(len(left)):
                every_step[i][j] += right[i]


        for i in range(len(every_step)):
            j = 0
            while j < len(every_step) - 1:
                if 'E' in every_step[i][j]:
                    every_step[i].pop(j)
                else:
                    j += 1

        result = []
        for i in every_step:
            result += i

        return result

    def sum(self, left, right):
        return left + right

    def result_first(self):
        '''a = self.inc(['0'], 3)
        print(a)
        b = ['1']
        c = self.inc(['0'], 3)
        d = ['1']
        e = self.inc(['0'], 3)

        a = self.sum(self.sum(self.sum(self.sum(a, b), c), d), e)

        a = self.mul(a, a)'''
        a = ['a', 'b', 'c']
        a = self.inc(a, 4)
        #print(a)
        b = []
        for i in a[1:]:
            b = self.sum(b, self.mul(i.copy(), '!'))
        a = b
        print(a)
        #a = self.mul(a, a)


        #print(a)

'''class Alph:
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
        sympy.pprint(ish)'''

if __name__ == '__main__':
    a = Qyest()
    left = ['E', '1', '0']
    right = ['1', '0', '1']
    #print(a.inc(['0', '1'], 3))
    a.result_first()