from random import randint


def create_matrix(N, M):
    return [[[1, 1, 1] for i in range(M)]] + \
           [[[randint(0, 1), randint(0, 1), randint(0, 1)] for j in range(M)] for i in range(N - 1)]

def output_right(matrix , user):
    right = ['Дать права', 'Запись', 'Чтение']
    tmp_mass = matrix[user]
    string = ''
    for i in range(len(tmp_mass)):
        string += 'Объект{}:'.format(i)
        tmp = 0
        for j in range(len(right)):
            if tmp_mass[i][j]:
                tmp += 1
                string += right[j] + ' '
        if tmp == 0:
            string += 'Нет прав'
        string += '\n'
    return string

def menu():
    N, M = int(input('Введите число субъектов ')), int(input('Введите число объектов '))
    matrix = create_matrix(N, M)
    tmp_str = ''
    while tmp_str != 'выход':
        tmp_str = ''
        user = int(input('Введите пользователя: '+ '\n'))
        while tmp_str != 'Назад':
            print(output_right(matrix, user))
            tmp_str = input('Жду ваших указаний: '+ '\n')
            if tmp_str == 'Запись':
                tmp_str = int(input('Какой объект?' + '\n'))
                if matrix[user][tmp_str][1] == 1:
                    print('Запись разрешена'+ '\n')
                else:
                    print('Недостаточно прав'+ '\n')
            elif tmp_str == 'Чтение':
                tmp_str = int(input('Какой объект?'+ '\n'))
                if matrix[user][tmp_str][2] == 1:
                    print('Чтение разрешено')
                else:
                    print('Недостаточно прав')
            elif tmp_str == 'Дать права':
                tmp_str = int(input('На какой объект передается право?'))
                tmp_str_right = input('Какое право?' + '\n')
                tmp_str_user = int(input('Какому пользователю?' + '\n'))
                if matrix[user][tmp_str][0] == 1:
                    print('Доступ прав подтверждён')
                    if tmp_str_right == 'Дать права':
                        print(matrix[tmp_str_user][tmp_str][0])
                        if matrix[tmp_str_user][tmp_str][0] == 1:
                            print('У этого пользователя имеются эти права'+ '\n')
                        else:
                            matrix[tmp_str_user][tmp_str][0] = 1
                    elif tmp_str_right == 'Чтение':
                        print(matrix[tmp_str_user][tmp_str][2])
                        if matrix[tmp_str_user][tmp_str][2] == 1:
                            print('У этого пользователя имеются эти права'+ '\n')
                        else:
                            matrix[tmp_str_user][tmp_str][2] = 1
                    elif tmp_str_right == 'Запись':
                        print(matrix[tmp_str_user][tmp_str][1])
                        if matrix[tmp_str_user][tmp_str][1] == 1:
                            print('У этого пользователя имеются эти права' + '\n')
                        else:
                            matrix[tmp_str_user][tmp_str][1] = 1
                else:
                    print('Недостаточно прав')




if __name__ == '__main__':
    menu()