from random import randint


def create_matrix(N, M, down, up):
    return [[randint(down, up) for j in range(N)] for i in range(M)]


def output(matrix):
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
            print(matrix[i][j], end=' ')
        print('sum = ', sum)


def rasp(matrix):
    tmp = [0] * N
    i = 0
    while i < M:
        for j in range(len(result)):
            tmp[j] = result[j] + matrix[i][j]
        result[tmp.index(min(tmp))] = tmp[tmp.index(min(tmp))]
        i += 1
    print('T = ', result, 'Max = ', max(result))


def minimal(matrix):
    result = [0] * N
    i = 0
    while i < M:
        result[matrix[i].index(min(matrix[i]))] += matrix[i][matrix[i].index(min(matrix[i]))]
        i += 1
    print('T = ', result, 'Max = ', max(result))


def Sort(matrix):
    matrix = sorted(matrix, key=lambda matrix: sum((int(matrix[i]) for i in range(0, int(len(matrix))))))
    output(matrix)
    return matrix

def Sort2(matrix):
    matrix = sorted(matrix, key=lambda matrix: sum((int(matrix[i]) for i in range(0, int(len(matrix))))))
    matrix.reverse()
    output(matrix)
    return matrix


if __name__ == '__main__':
    N, M, down, up = int(input('Введите число процессоров ')), int(input('Введите число заданий ')), int(input(
        'Введите нижнюю границу ')), int(input('Введите верхнюю границу '))
    matrix = create_matrix(N, M, down, up)
    result = [0] * N
    matrix2 = matrix.copy()
    print('Исходный матрица: ')
    output(matrix)
    rasp(matrix)
    print('Матрица повозрастанию: ')
    Sort(matrix)
    rasp(matrix)
    print('Матрица поубыванию: ')
    Sort2(matrix)
    rasp(matrix)
    print('Исходная матрица и алгоритм минимального элемента:')
    output(matrix2)
    minimal(matrix2)
