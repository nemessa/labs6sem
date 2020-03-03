class Qyest:
    def __init__(self):
        self.plus = None
        self.multiply = None
        self.increase = None

    def inc(self, mass, depth):
        res = [['E']]
        for i in range(depth):
            if len(res) == 1:
                res.append(mass)
            else:
                res += [self.mul(res[-1], mass)]

        result = []
        for i in res[1:]:
            for j in i:
                result.append(j)
        return result

    def mul(self, left, right):
        every_step = [left.copy() for i in range(len(right))]
        for i in range(len(right)):
            for j in range(len(left)):
                every_step[i][j] += right[i]

        #print(left, right, every_step)
        for i in range(len(every_step)):
            j = 0
            while j < len(every_step) - 1 and every_step[i]:
                #print(i, j, every_step[i])
                if 'E' in every_step[i][j] and len(every_step[i][j]) > 1:
                    every_step[i].pop(j)
                else:
                    j += 1

        result = []
        for i in every_step:
            result += i

        return result

    def sum(self, left, right):
        return left + right

    def res_van(self):
        a = ['a', 'b', 'c']
        a = self.inc(a, 4)
        print(a)

        a = self.mul(a, ['!'])
        print(a)

    def result_first(self):
        a = self.inc(['0'], 3)
        print(a)
        b = ['1']
        c = self.inc(['0'], 3)
        d = ['1']
        e = self.inc(['0'], 3)

        a = self.sum(self.sum(self.sum(self.sum(a, b), c), d), e)
        print(a)
        a = self.mul(a, a)
        print(a)

    # (0*10*10* + 0*110* + 10*10* + 0*10*1 + 10*1 + 11)*
    def res_second(self):
        a = self.inc(['0'], 5)
        a = ['0']
        b = ['1']
        c = self.inc(['0'], 2)
        c = ['0']
        d = ['1']
        e = self.inc(['0'], 2)
        e = ['0']
        #a = self.mul(self.mul(self.mul(self.mul(a, b), c), d), e)
        ab = self.sum(self.sum(self.sum(self.sum(self.mul(self.mul(self.mul(self.mul(a, b), c), d), e),
                     self.mul(self.mul(self.mul(a, b), d), e)),
                              self.mul(self.mul(self.mul(b, c), d), e)),
                                    self.mul(self.mul(self.mul(a, b), c), d)),
                                        ['11'])
        #print(ab, end=' ')
        a = self.inc(['0'], 2)
        c = self.inc(['0'], 2)
        e = self.inc(['0'], 2)
        # (0*10*10* + 0*110* + 10*10* + 0*10*1 + 10*1 + 11)*
        a = self.sum(self.sum(self.sum(self.sum(self.sum(self.mul(self.mul(self.mul(self.mul(a, b), c), d), e),
                                                 self.mul(self.mul(self.mul(a, b), d), e)),
                                        self.mul(self.mul(self.mul(b, c), d), e)),
                               self.mul(self.mul(self.mul(a, b), c), d)),
                      self.mul(self.mul(b, c), d)),
                      ['11'])
        a = self.sum(a, self.inc(a, 2))
        print(a)
        #aa = self.mul(self.mul(self.mul(a, b), d), e)
        #aaa = self.mul(self.mul(self.mul(b, c), d), e)
        #print(aaa)
        #aaaa = self.mul(self.mul(self.mul(a, b), c), d)
        #print(aaaa)
        #aaaaa = self.mul(self.mul(b, c), d)
        #aaaaa = ['11']

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

def t():
    for i in range(1, 100):
        tmp = str(bin(i))[2:]
        n = 0
        for j in tmp:
            if j == '1':
                n += 1
        if n % 2 == 0:
            print(tmp, end=', ')



if __name__ == '__main__':
    a = Qyest()
    left = ['0', '1', '0']
    right = ['1', '00', '1']
    #print(a.inc(['0', '1'], 3))
    #print(a.mul(left, right))
    a.res_second()
    #t()