import numpy as np


'''a = np.random.randint(10, 25, 10)
print(a)
print(a.sum())'''

class Sort:
    @staticmethod
    def __find(mass_t, res):
        if len(mass_t) == 2:
            if mass_t[0][0] > mass_t[1][0]:
                res.append(mass_t[1])
                return
            else:
                res.append(mass_t[0])
                return

        new_mass_t = []

        for i in range(len(mass_t) // 2):
            if mass_t[i*2][0] > mass_t[i*2+1][0]:
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
            mass_t[mass_t.index(res[-1])][0] = 9999

        return res

class Proiz:
    def __init__(self, N, M, left=10, right=25):
        self.mass = np.random.randint(left, right, (N, M))
        self.N = N
        self.M = M

    def __sum(self, mass):
        res = 0
        for i in mass:
            res += i
        return res

    def sort(self):
        tmp = []
        for i in self.mass:
            tmp.append([i.sum(), i])
        # Костыль
        a = Sort.t_sort(tmp)
        new_mass = np.array([a[0][1], a[1][1]])
        for i in a[2:]:
            new_mass = np.append(new_mass, [i[1]], axis=0)
        return new_mass
        # конец костыля

    def __index(self, mass, el):
        for i in range(len(mass)):
            if el == mass[i]:
                return i

    def __arbitrary(self, mass):
        res = [[0 for j in range(len(mass[0]))] for i in range(len(mass))]
        m = mass[0].min()
        res[0][self.__index(mass[0], m)] = m
        for i in range(1, len(mass)):
            tmp = res[i-1].copy()
            for j in range(len(mass[i])):
                tmp[j] += mass[i][j]

            res[i] = res[i-1].copy()
            res[i][tmp.index(min(tmp))] = min(tmp)

        self.print_matrix(res)

        print('max({}); Tmax = {}'.format(res[-1], max(res[-1])))
        print('\n*******************************\n')

    def arbitrary_without_sort(self):
        print('Without sort: ')
        self.print_matrix(self.mass)
        self.__arbitrary(self.mass)

    def arbitrary_ascending_sort(self):
        mass = self.sort()
        print('Ascending sort: ')
        self.print_matrix(self.create_mass_with_sum(mass))
        self.__arbitrary(mass)

    def arbitrary_descending_sort(self):
        mass = list(reversed(self.sort()))
        print('Descending sort: ')
        self.print_matrix(self.create_mass_with_sum(mass))
        self.__arbitrary(mass)

    def create_mass_with_sum(self, mass):
        tmp = []
        for i in range(len(mass)):
            tmp.append([])
            for j in mass[i]:
                tmp[i].append(j)
            tmp[i].append('|')
            tmp[i].append(self.__sum(mass[i]))
        return tmp

    def print_matrix(self, mass):
        for i in mass:
            for j in i:
                print(j, end=' ' * (4 -len(str(j))))
            print()
        print('\n-------------------------------\n')


if __name__ == '__main__':
    a = Proiz(15, 4)
    a.print_matrix(a.mass)
    a.arbitrary_ascending_sort()
    a.arbitrary_descending_sort()
    a.arbitrary_without_sort()
    '''aa = np.array([i[1]] for i in a.sort())
    print(aa)'''