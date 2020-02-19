from views import Alphabet

n = input('If you wanna know word enter 1 or 2 if you wanna know number: ')

if n == '1':
    a = Alphabet(input('Enter an alphabet, only unique chars solid: '))
    if not a:
        print('Incorrect alphabet')
    else:
        num = input('Enter a number: ')
        tmp = a.to_word(num)
        if tmp:
            print(tmp)
        else:
            print('Incorrect number')
elif n == '2':
    a = Alphabet(input('Enter an alphabet, only unique chars: '))
    if not a:
        print('Incorrect alphabet')
    else:
        word = input('Enter a word: ')
        tmp = a.to_num(word)
        if tmp:
            print(tmp)
        else:
            print('Incorrect word')
else:
    print('Incorrect input')