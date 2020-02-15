from random import randint

class Sort:
    @staticmethod
    def __find(mass_t, res):
        if len(mass_t) == 2:
            if mass_t[0] > mass_t[1]:
                res.append(mass_t[1])
                return
            else:
                res.append(mass_t[0])
                return

        new_mass_t = []

        for i in range(len(mass_t) // 2):
            if mass_t[i*2] > mass_t[i*2+1]:
                new_mass_t.append(mass_t[i*2+1])
            else:
                new_mass_t.append(mass_t[i*2])
        if len(mass_t) % 2 == 1:
            new_mass_t.append(mass_t[-1])
        Sort.__find(new_mass_t, res)

    @staticmethod
    def t_sort(mass_t):
        res = []

        for i in range(len(mass_t)):
            Sort.__find(mass_t, res)
            mass_t[mass_t.index(res[-1])] = 9999

        return res


class Krit:
    def __init__(self, n, m):
        self.mass = []
        for i in range(m):
            self.mass.append(randint(10, 100))
        self.n = n

    def __sum(self, mass):
        res = 0
        for i in mass:
            res += i
        return res

    def __union(self, mass):
        tmp = [self.__sum(i) for i in mass]

        return tmp.index(min(tmp))

    def __krit(self, mass):
        p = [[0] for i in range(self.n)]

        for i in self.mass:
            p[self.__union(p)].append(i)
            # print(p)

        for i in range(len(p)):
            print('p{} = {};  {}'.format(i + 1, self.__sum(p[i]), p[i]))

        print('\n', '-' * 20, '\n', sep='')

    def krit_withot_sort(self):
        print('T = {}'.format(self.mass))

        self.__krit(self.mass)


    def krit_ascending(self):
        mass = Sort.t_sort(self.mass.copy())
        print(self.__print_matrix(mass))
        print('T = {}'.format(mass))

        self.__krit(mass)

    def krit_descending(self):
        mass = list(reversed(Sort.t_sort(self.mass.copy())))
        print(self.__print_matrix(mass))
        print('T = {}'.format(mass))

        self.__krit(mass)

    def __print_matrix(self, mass):
        string = ''
        for i in mass:
            string += '{}  '.format(i) * self.n + '\n'

        return string

    def __str__(self):
        string = ''
        for i in self.mass:
            string += '{}  '.format(i) * self.n + '\n'

        return string

a = Krit(8, 14)
print(a)

a.krit_withot_sort()
a.krit_ascending()
a.krit_descending()
