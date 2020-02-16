from random import randint

def hoar(mass):
    if not mass:
        return []
    else:
        if len(mass) > 2:
            ind = []
            while len(ind) != 3:
                tmp = randint(0, len(mass) - 1)
                if not tmp in ind:
                    ind.append(tmp)

            print(mass, ind, end=' ')
            if mass[ind[0]] > mass[ind[1]] > mass[ind[2]]:
                middle = mass[ind[1]]
                ind = ind[1]
            elif mass[ind[0]] > mass[ind[2]] > mass[ind[1]]:
                middle = mass[ind[2]]
                ind = ind[2]
            else:
                middle = mass[ind[0]]
                ind = ind[0]
        else:
            middle = mass[0]
            ind = 0
        print(middle, ind)
        left = [i for i in mass[0:ind] + mass[ind:len(mass)] if i < middle]
        '''left = []
        for i in mass[0:ind] + mass[ind:len(mass)]:
            if i < middle:
                left.append(i)'''
        right = [i for i in mass[0:ind] + mass[ind:len(mass)] if i > middle]
        return hoar(left) + [middle] + hoar(right)

mass = [5, 2, 4, 1, 3]

print(hoar(mass))


