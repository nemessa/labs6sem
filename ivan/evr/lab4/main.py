from random import randint


def create_matrix(n, m, T1, T2):
    mass = [randint(T1, T2) for i in range(m)]
    return mass


def output_matrix(matrix, n):
    string = ''
    for i in matrix:
        string += '{}  '.format(i) * n + '\n'

    return string


def crit(matrix, m):
    mass_tmp = matrix.copy()
    p = [[] for i in range(m)]
    for i in mass_tmp:
        p[union(p)].append(i)
    return p


def union(matrix):
    tmp = [sum(i) for i in matrix]
    return tmp.index(min(tmp))


def HDMT(matrix):
    Pa, Pb = crit(matrix, 2)
    print('Уровень 1:')
    print('Pa =', Pa, ' sum =', sum(Pa))
    print('Pb =', Pb, ' sum =', sum(Pb))
    print()
    print('Уровень 2 левая часть:')
    Pa = crit(Pa, n // 2)
    for i in range(n // 2):
        print('P{} = {}, sum = {}'.format(i + 1, Pa[i], sum(Pa[i])))
    print('Уровень 2 правая часть:')
    Pb = crit(Pb, n // 2)
    for i in range(n // 2):
        print('P{} = {}, sum = {}'.format(i + n // 2 + 1, Pb[i], sum(Pb[i])))
    P = Pa + Pb
    sums = list(map(sum, P))
    print(sums)
    print('Tmax = P{}'.format(sums.index(max(sums))+1),
          '=', P[sums.index(max(sums))], '=', max(sums))
    print()
    print()


if __name__ == '__main__':
    n = int(input('Введите количество процессоров: '))
    m = int(input('Введите количество заданий: '))
    T1 = int(input('Введите нижнию границу: '))
    T2 = int(input('Введите верхнюю границу: '))
    matrix = create_matrix(n, m, T1, T2)
    print('Исходная матрица:')
    print(output_matrix(matrix, n))
    HDMT(matrix)
    print()
    print('Отсортирована по возрастанию: ')
    matrix = sorted(matrix)
    print(output_matrix(matrix, n))
    HDMT(matrix)
    print('Отсортирована по убыванию: ')
    matrix = sorted(matrix)[::-1]
    print(output_matrix(matrix, n))
    HDMT(matrix)
