
from random import randint
from time import sleep

class Kron:
    def __init__(self, n, m, left=10, right=25):
        mass = []
        self.n = n
        for i in range(n):
            mass.append(randint(left, right))

        self.p = [[] for i in range(m)]

        for i in mass:
            self.p[randint(0, m-1)].append(i)

        #self.p = [[10,10,21], [14, 16, 10, 14], [15, 13, 19]]

        self.print_matrix(self.p)

        self.step_1()
        self.step_2()
        self.step_2_2()



    def find_T(self, mass):
        sums = []
        for i in mass:
            sums.append(sum(i))

        Tmax = max(sums)
        for i in mass:
            if Tmax == sum(i):
                Tmax = i
                break

        Tmin = min(sums)
        for i in mass:
            if Tmin == sum(i):
                Tmin = i
                break

        return Tmin, Tmax, sum(Tmax)-sum(Tmin)

    def step_1(self):
        prov = True
        while prov:
            Tmin, Tmax, a = self.find_T(self.p)
            prov = False
            for i in Tmax:
                if i < a:
                    Tmin.append(Tmax.pop(Tmax.index(i)))
                    prov = True
                    break

    def step_2(self):
        prov = True
        while prov:
            Tmin, Tmax, a = self.find_T(self.p)
            #print(Tmin, Tmax, a)
            #self.print_matrix(self.p)
            prov = False
            f = False
            for i in Tmax:
                for j in Tmin:
                    if i - j < a and i - j > 0:
                        Tmin.append(Tmax.pop(Tmax.index(i)))
                        Tmax.append(Tmin.pop(Tmin.index(j)))
                        prov = True
                        f = True
                        break
                if f:
                    f = False
                    break
        self.print_matrix(self.p)

        print('Tmax = {}'.format(sum(self.find_T(self.p)[1])))
        #print_b(sum(self.find_T(self.p)[1]))

    def step_2_2(self):
        prov = True
        while prov:
            for i in range(len(self.p)):
                self.p[i] = sorted(self.p[i])[::-1]
            Tmin, Tmax, a = self.find_T(self.p)
            #print(Tmin, Tmax, a)
            #self.print_matrix(self.p)
            prov = False
            f = False
            for i in Tmax:
                for j in Tmin:
                    if i - j < a and i - j > 0:
                        Tmin.append(Tmax.pop(Tmax.index(i)))
                        Tmax.append(Tmin.pop(Tmin.index(j)))
                        prov = True
                        f = True
                        break
                if f:
                    f = False
                    break
        self.print_matrix(self.p)

        print('Tmax = {}'.format(sum(self.find_T(self.p)[1])))
        #print_b(sum(self.find_T(self.p)[1]))







    def print_matrix(self, mass):
        for i in mass:
            print(i, '|', sum(i))
        print()


if __name__ == '__main__':
    n = int(input('enter n: '))
    m = int(input('enter m: '))
    T1 = int(input('enter T1: '))
    T2 = int(input('enter T2: '))
    Kron(n, m, T1, T2)

