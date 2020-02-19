def intt():
    dict = str(input('Введите словарь: '))
    word = str(input('Введите слово: '))
    new_dict = ''
    res = ""
    l = []
    for i in range(len(dict)):
        if new_dict.find(dict[i]) == -1 and dict[i] != ' ':
            new_dict += dict[i]
    print('Словарь = ', new_dict)

    for i in range(len(word)):
        for j in range(len(new_dict)):
            if new_dict[j] == word[i]:
                l.append(j)

    n = len(new_dict)
    k = len(word)
    result = 0
    s = len(word)
    l.reverse()
    print('n = ', n)
    print('k =', k)
    for i in range(len(word)):
        result += (n ** (k - s)) * ((l[i]) + 1)
        res += ('(({} ** ({}-{})) * {}) + '.format(n, k, s, l[i] + 1))
        s -= 1

    print(res[:-2] + '= {}'.format(result))


def word():
    dict = input('Введите словарь: ')
    number = int(input('Введите число: '))
    view = ''
    word = ''
    tmp2 = 0
    tmp = ''
    result = ''
    while (len(dict) <= number):
        if (number % len(dict) == 0):
            tmp = view
            view = ') * {} * {} + {} '.format(number // len(dict), len(dict), number % len(dict))
            view += tmp
            word += str(len(dict))
            number = number // len(dict) - 1
            print(word, number)
        else:
            tmp = view
            view = ') * {} * {} + {} '.format(number // len(dict), len(dict), number % len(dict))
            view += tmp
            word += '{}'.format(number % len(dict))
            number = number // len(dict)
            #print(word, number)
        tmp2 += 1
    if number > 0:
        word += '{}'.format(number % len(dict))
    print('{}{}'.format('(' * tmp2, len(dict)) + view)
    for i in reversed(word):
        result += dict[(int(i) - 1)]
    print(result)


if __name__ == '__main__':
    n = int(input('Выберите действие: \n'
                  '1. Из строки в число \n'
                  '2. Из числа в строку \n'))
    if n == 1:
        intt()
    elif n == 2:
        word()
