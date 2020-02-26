from random import randint
matrix = []

def create_matrix(M, down, up):
    for i in range(M):
        matrix.append(randint(down, up))

def print_matrix(matrix):
    string = ''
    for i in matrix:
        string += '{}  '.format(i) * N + '\n'
    return string

def proc(matrix):
    tmp_mas = matrix.copy()
    for i in range(M):
        min = tmp_mas[0]
        min_index = 0
        if i >= N:
            for j in range(N):
                if tmp_mas[j] < min:
                    min_index = j
                    min = tmp_mas[j]
            tmp_mas[min_index] += matrix[i]

    for i in range(N):
        print('p{} ='.format(i+1), tmp_mas[i])

    max = tmp_mas[0]
    for i in range(M):
        if tmp_mas[i] > max:
            max = tmp_mas[i]
    print('Max =', max)

def heap_sort (sequence):

    def swap_items (index1, index2):
        if sequence[index1] < sequence[index2]:                                 # !
            sequence[index1], sequence[index2] = sequence[index2], sequence[index1]

    def sift_down (parent, limit):
        while True:
            child = (parent + 1) << 1 # То же, что и parent * 2 + 2
            if child < limit:
                if (sequence[child] < sequence[child - 1]):
                    swap_items(parent, child-1)
                    parent = child-1
                else:
                    swap_items(parent, child)
                    parent = child
            else:
                if (child-1<limit):
                    swap_items(parent,child-1)
                break
    # Тело функции heap_sort
    length = len(sequence)
    # Формирование первичной пирамиды
    for index in range((length >> 1) - 1, -1, -1):
        sift_down(index, length)
    # Окончательное упорядочение
    for index in range(length - 1, 0, -1):
        swap_items(index, 0)
        sift_down(0, index)

def heap_sort_down (sequence):

    def swap_items (index1, index2):
        if sequence[index1] > sequence[index2]:                                 # !
            sequence[index1], sequence[index2] = sequence[index2], sequence[index1]

    def sift_down (parent, limit):
        while True:
            child = (parent + 1) << 1 # То же, что и parent * 2 + 2
            if child < limit:
                if (sequence[child] < sequence[child - 1]):
                    swap_items(parent, child-1)
                    parent = child-1
                else:
                    swap_items(parent, child)
                    parent = child
            else:
                if (child-1<limit):
                    swap_items(parent,child-1)
                break
    # Тело функции heap_sort
    length = len(sequence)
    # Формирование первичной пирамиды
    for index in range((length >> 1) - 1, -1, -1):
        sift_down(index, length)
    # Окончательное упорядочение
    for index in range(length - 1, 0, -1):
        swap_items(index, 0)
        sift_down(0, index)

if __name__ == '__main__':
    N, M, down, up = int(input('Введите число процессов ')), int(input('Введите число заданий ')), int(input(
        'Введите нижнюю границу ')), int(input('Введите верхнюю границу '))
    create_matrix(M, down, up)
    print('Исходная матрица: ')
    print(print_matrix(matrix))
    print('T =', matrix)
    proc(matrix)
    print('Отсортированная матрица по возрастанию:')
    heap_sort(matrix)
    print(print_matrix(matrix))
    print('T =', matrix)
    proc(matrix)
    print('Отсортированная матрица по убыванию:')
    heap_sort_down(matrix)
    print(print_matrix(matrix))
    print('T =', matrix)
    proc(matrix)
