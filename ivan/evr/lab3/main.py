from random import randint

mass = []


def kron(n, m, T1, T2):
    for i in range(n):
        mass.append(randint(T1, T2))

    p = [[] for i in range(m)]

    for i in mass:
        p[randint(0, m - 1)].append(i)
    print(p)
    return p


def find(mass):
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
    return Tmin, Tmax, sum(Tmax) - sum(Tmin)


def step(matrix):
    proverka = True
    while proverka:
        Tmin, Tmax, a = find(matrix)
        proverka = False
        for i in Tmax:
            if i < a:
                Tmin.append(Tmax.pop(Tmax.index(i)))
                proverka = True
                break
    output_matrix(matrix)
    print('Tmax = {}'.format(sum(find(matrix)[1])))


def step2(matrix):
    proverka = True
    while proverka:
        Tmin, Tmax, a = find(matrix)
        proverka = False
        flag = False
        for i in Tmax:
            for j in Tmin:
                if i - j < a and i - j > 0:
                    #output_matrix(matrix)
                    #print('Tmin = {} Tmax = {} Delta = {}'.format(sum(Tmin), sum(Tmax), sum(Tmax) - sum(Tmin)))
                    #print()
                    Tmin.append(Tmax.pop(Tmax.index(i)))
                    Tmax.append(Tmin.pop(Tmin.index(j)))
                    proverka = True
                    flag = True
                    break
            if flag:
                flag = False
                break
    output_matrix(matrix)
    print('Tmax = {}'.format(sum(find(matrix)[1])))


def step22(matrix):
    proverka = True
    while proverka:
        for i in range(len(matrix)):
            matrix[i] = sorted(matrix[i])[::-1]
        Tmin, Tmax, a = find(matrix)
        proverka = False
        flag = False
        for i in Tmax:
            for j in Tmin:
                if i - j < a and i - j > 0:
                    Tmin.append(Tmax.pop(Tmax.index(i)))
                    Tmax.append(Tmin.pop(Tmin.index(j)))
                    proverka = True
                    flag = True
                    break
            if flag:
                flag = False
                break
    output_matrix(matrix)
    print('Tmax = {}'.format(sum(find(matrix)[1])))


def output_matrix(mass):
    for i in mass:
        print(i, '|', sum(i))
    print()


def crit(m):
    mass_tmp = mass.copy()
    p = [[] for i in range(m)]
    for i in mass_tmp:
        p[union(p)].append(i)

    for i in range(len(p)):
        p[i] = sorted(p[i])
    print(p)
    return p


def crit2(m):
    mass_tmp = mass.copy()
    p = [[] for i in range(m)]
    for i in mass_tmp:
        p[union(p)].append(i)

    for i in range(len(p)):
        p[i] = sorted(p[i])[::-1]
    print(p)
    return p


def union(mass):
    tmp = [sum(i) for i in mass]
    return tmp.index(min(tmp))


if __name__ == '__main__':
    n = int(input('Введите количество процессоров: '))
    m = int(input('Введите количество заданий: '))
    T1 = int(input('Введите нижнию границу: '))
    T2 = int(input('Введите верхнюю границу: '))
    matrix = kron(m, n, T1, T2)
    print('Исходная матрица:')
    output_matrix(matrix)
    print('1 Этап')
    step(matrix)
    print('2 Этап')
    step2(matrix)
    print('2_2 Модификация(отсортировано по убыванию)')
    step22(matrix)
    print('Матрица крит пути (по возрастанию):')
    matrix2 = crit(n)
    output_matrix(matrix2)
    print('1 Этап')
    step(matrix2)
    print('2 Этап')
    step2(matrix2)
    print('2_2 Модификация(отсортировано по убыванию)')
    step22(matrix2)
    print('Матрица крит пути (по убыванию):')
    matrix3 = crit2(n)
    output_matrix(matrix3)
    print('1 Этап')
    step(matrix3)
    print('2 Этап')
    step2(matrix3)
    print('2_2 Модификация(отсортировано по убыванию)')
    step22(matrix3)
