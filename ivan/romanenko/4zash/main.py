from random import randint

def create_user_rights(N, M):
    user = [randint(0, 2) for i in range(N)]
    rights = [randint(0, 2) for i in range(M)]
    return user, rights

def output_right(user, rights):
    tmp = 0
    right = ['Совершенно секретно', 'Секретно', 'Открытые данные']
    print('Множество атрибутов безопасности')
    print('L = {}'.format(right))
    print('Уровни конфиденциальности объектов')
    print('O = [', end='')
    for i in rights:
        print('Объект_{}'.format(tmp), right[i], end=',')
        tmp+= 1
    print(' ]')
    tmp = 0
    print('Уровни допуска пользователей')
    print('S = [', end='')
    for i in user:
        print('№{}'.format(tmp), right[i], end=',')
        tmp +=1
    print(' ]')

def request(user, user_id, rights, M):
    if user[user_id] <= rights[M]:
        print('Успешно')
    else:
        print('Доступ запрещен')

def acsses(rights, user, user_id):
    string = 'Перечень доступных объектов:'
    for i in range(len(rights)):
        if user[user_id] <= rights[i]:
            string += ' Объект_{}'.format(i)
    return string

def main():
    N, M = int(input('Введите число субъектов ')), int(input('Введите число объектов '))
    user, rights = create_user_rights(N, M)
    output_right(user, rights)
    while True:
        user_log = int(input('Введите пользователя: ' + '\n'))
        while user_log:
            print('1 Показать мои объекты ',
                  '2 Запрос ',
                  '3 Выход ',
                  sep='\n')
            tmp = input('Выберите действие ')
            if tmp == '1':
                print(acsses(rights, user, user_log ))
            elif tmp == '2':
                obj = int(input('Какой объект? '))
                request(user, user_log, rights, obj)
            elif tmp == '0':
                break
if __name__ == '__main__':
    main()