from random import randint


class HDA:
    # left & right границы рандома, можно изменить при вызове конструктора
    def __init__(self, n, m, left=10, right=25):
        self.n = n
        self.mass = [randint(left, right) for i in range(m)]

    def krit(self, mass, n):
        p = [[] for i in range(n)]

        for i in mass:
            sums = list(map(sum, p))
            p[sums.index(min(sums))].append(i)

        return p

    def HDA(self, mass):
        self.print_mass(mass)
        Pa, Pb = self.krit(mass, 2)
        print('Level 1:')
        print('Pa =', Pa, ' sum =', sum(Pa))
        print('Pb =', Pb, ' sum =', sum(Pb))
        print('\nLevel 2 left:')
        Pa = self.krit(Pa, self.n // 2)
        for i in range(self.n // 2):
            print('P{} = {}, sum = {}'.format(i + 1, Pa[i], sum(Pa[i])))
        print('Level 2 right:')
        Pb = self.krit(Pb, self.n // 2)
        for i in range(self.n // 2):
            print('P{} = {}, sum = {}'.format(i + self.n // 2 + 1, Pb[i], sum(Pb[i])))

        P = Pa + Pb
        sums = list(map(sum, P))
        print('Tmax = P{}'.format(sums.index(max(sums))),
              '=', P[sums.index(max(sums))], '=', max(sums), end='\n\n')

    def main(self):
        print('Without sort:')
        self.HDA(self.mass)

        print('Ascending sort:')
        self.HDA(sorted(self.mass))

        print('Descending sort:')
        self.HDA(list(reversed(sorted(self.mass))))

    def print_mass(self, mass):
        string = ''
        for i in mass:
            string += '{}  '.format(i) * self.n + '\n'

        print(string)

    def __str__(self):
        string = ''
        for i in self.mass:
            string += '{}  '.format(i) * self.n + '\n'

        return string

class OFMT:
    # left & right границы рандома, можно изменить при вызове конструктора
    def __init__(self, n, m, left=10, right=25):
        self.n = n
        self.mass = [randint(left, right) for i in range(m)]
        self.deep = [[]]

    def krit(self, mass, n):
        p = [[] for i in range(n)]

        for i in mass:
            sums = list(map(sum, p))
            p[sums.index(min(sums))].append(i)

        return p

    def OFMT_deep(self, mass, l):
        if l >= len(self.deep):
            self.deep.append([])
        Pleft, Pright = self.krit(mass, 2)
        self.deep[l].append(Pleft)
        self.deep[l].append(Pright)
        if (l+1) ** 2 < self.n:
            self.OFMT_deep(Pleft, l+1)
            self.OFMT_deep(Pright, l+1)


    def OFMT(self, mass):
        self.print_mass(mass)
        n = self.n
        self.OFMT_deep(mass, 0)
        for i in self.deep:
            print(i)

    def main(self):
        print('Without sort:')
        self.OFMT(self.mass)

        '''print('Ascending sort:')
        self.OFMT(sorted(self.mass))

        print('Descending sort:')
        self.OFMT(list(reversed(sorted(self.mass))))'''

    def print_mass(self, mass):
        string = ''
        for i in mass:
            string += '{}  '.format(i) * self.n + '\n'

        print(string)

    def __str__(self):
        string = ''
        for i in self.mass:
            string += '{}  '.format(i) * self.n + '\n'

        return string

if __name__ == '__main__':
    m = randint(20, 25)
    print('Вариант 13:\nm =', m, 'n = 4')
    a = HDA(4, m, left=20, right=35)
    a.main()
