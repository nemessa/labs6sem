from random import randint


class Scheduling:
    def __init__(self, n=4, left=1, right=25):
        m = randint(8, 15)
        print('N = 4; M =', m)
        self.p = [randint(left, right) for i in range(m)]
        self.mass = [[] for i in range(m)]

        for i in range(len(self.p)):
            inf = 4
            for j in range(n):
                if randint(0, 2):
                    self.mass[i].append(self.p[i])
                    inf -= 1
                else:
                    self.mass[i].append(0)

            if inf == 4:
                self.mass[i][randint(0, 3)] = self.p[i]

    def sort(self, mass=None):
        if not mass:
            mass = self.mass
        mass = mass.copy()
        sorted_mass = list(sorted(self.p))
        new_mass = []
        for i in sorted_mass:
            for j in mass:
                if i in j:
                    new_mass.append(j)
                    mass.pop(mass.index(j))
        '''
        self.output_mass(new_mass)

        dict_num = {}
        dict_sums = {}
        for i in range(len(new_mass)):
            k = 0
            digit = 0
            for j in new_mass[i]:
                if j != 0:
                    k = j
                    digit += j
            dict_num[k] = dict_num.get(k, []) + [i]
            dict_sums[k] = dict_sums.get(k, []) + [digit]

        for i in list(dict_num):
            if len(dict_num[i]) == 1:
                del dict_num[i]
                del dict_sums[i]

        print('a', dict_num)
        print('b', dict_sums)

        new_dict = {}
        for i in list(dict_sums):
            tmp = dict_sums[i]
            tmp_2 = {}
            for j in range(len(dict_sums[i])):
                tmp_2[dict_sums[i][j]] =\
                    dict_num[i][j]
            new_dict[i] = tmp_2
        print(new_dict)
        for i in list(new_dict):
            if len(new_dict[i]) == 1:
                del new_dict[i]
            else:
                tmp = {}
                for j in sorted(new_dict[i]):
                    tmp[j] = new_dict[i][j]
                new_dict[i] = tmp


        print(new_dict)'''

        return list(reversed(new_mass))

    def take_result(self, mass):
        print('Tmax = max(f(P1), f(P2), f(P3)',
              ' f(P4)) = max({}) = {}'.format(
            mass[[sum(i) for i in mass].
                index(max([sum(i) for i in mass]))],
            max([sum(i) for i in mass])))
        print('Tmax = P{} = {}'.format([sum(i) for i in mass].
                index(max([sum(i) for i in mass])),
              max([sum(i) for i in mass])))

    def modif_step_1_to_3(self, mass):
        tmp = []
        for i in mass:
            k = 0
            for j in i:
                if j == 0:
                    k += 1
            tmp.append([k, i])

        new_mass = []
        for i in reversed(range(len(mass[0]))):
            for j in tmp:
                if i == j[0]:
                    new_mass.append(j[1])

        return new_mass

    def modif_step_1_to_2(self, mass):
        tmp = []
        for i in mass:
            k = 0
            for j in i:
                if j == 0:
                    k += 1
            tmp.append([k, i])

        new_mass = []
        for j in tmp:
            if j[0] > 0:
                new_mass.append(j[1])

        for j in tmp:
            if j[0] == 0:
                new_mass.append(j[1])

        return new_mass

    def infinity(self):
        self.output_mass(self.sort())
        mass = self.modif_step_1_to_3(self.sort())
        self.output_mass(mass)
        self.main(mass)

    def low_infinity(self):
        self.output_mass(self.sort())
        mass = self.modif_step_1_to_2(self.sort())
        self.output_mass(mass)
        self.main(mass)

    def critical(self):
        print('Descending sorted:')
        mass = self.sort(self.mass)
        self.output_mass(mass)
        self.main(mass)

    def main(self, mass):

        p = [[] for i in range(len(self.mass[0]))]

        for i in mass:
            tmp = [sum(i) for i in p]
            for j in range(len(i)):
                if i[j] != 0:
                    tmp[j] += i[j]
                else:
                    tmp[j] = None
            m = 99999
            for k in tmp:
                if k:
                    if k < m:
                        m = k
            m = tmp.index(m)
            p[m].append(tmp[m] - sum(p[m]))

        for i in range(len(p)):
            print('P{} ='.format(i), p[i], '| sum =', sum(p[i]))
        self.take_result(p)

    def output_mass(self, mass):
        string = ''
        for i in mass:
            for j in i:
                if len(str(j)) == 1:
                    if j == 0:
                        string = '{} oo '.format(string)
                    else:
                        string = '{} {}  '.format(string, j)
                else:
                    string = '{} {} '.format(string, j)

            string = '{}\n'.format(string)

        print(string)

    def __str__(self):
        string = ''
        for i in self.mass:
            for j in i:
                if len(str(j)) == 1:
                    string = '{} {}  '.format(string, j)
                else:
                    string = '{} {} '.format(string, j)

            string = '{}\n'.format(string)

        return string


if __name__ == '__main__':
    a = Scheduling()
    print(a)
    a.critical()
    a.low_infinity()
    a.infinity()
