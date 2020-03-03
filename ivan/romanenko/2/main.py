import re
from random import randint


def create_string(result):
    a, b, c = 'a', 'b', 'c'
    for i in range(15):
        a1, b1, c1 = randint(0, 15), randint(0, 15), randint(0, 15)
        result = result + a * a1 + b * b1 + c * c1 + '!' + ','
    const = re.split("[,]", result)
    print(const)
    if text in const:
        print('True')
    else:
        print('False')
    return const


def create_string2(result, text):
    for i in range(16):
        for j in range(16):
            for y in range(16):
                result = result + 'a' * y + 'b' * j + 'c' * i + '!' + ','
    const = re.split("[,]", result)
    const.sort()
    const.sort(key=len)
    print(const)
    if text in const:
        print('True')
    else:
        print('False')
    return const

if __name__ == '__main__':
    result = ''
    text = input("Введите последовательность: ")
    #create_string(result)
    create_string2(result, text)

