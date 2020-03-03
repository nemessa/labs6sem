from views import *
nn = int(input('Enter n: '))
mm = int(input('Enter m: '))
a = Krit(nn, mm)
print(a)

while True:
    n = input('1) Sort Ascending\n2) Sort Descending\n3) Without sort\n')

    if n == '1':
        a.krit_ascending()
    elif n == '2':
        a.krit_descending()
    elif n == '3':
        a.krit_withot_sort()