from random import randint

mass = [16, 21, 8, 14, 26, 94, 30, 1]

mass = [22, 14, 9, 7, 7, 5,5,5]

m = 14

n = 4

mass = []

t ='a'

for i in range(m):
    tmp = randint(0, 100)
    mass.append(tmp)

def prt(m):
    for i in mass:
        print('{} '.format(i) * n)
mmm = mass.copy()
prt(mass)
res = []

def t_find(mass_t):
    if len(mass_t) == 2:
        if mass_t[0] > mass_t[1]:
            res.append(mass_t[1])
            return
        else:
            res.append(mass_t[0])
            return

    new_mass_t = []

    for i in range(len(mass_t) // 2):
        if mass_t[i*2] > mass_t[i*2+1]:
            new_mass_t.append(mass_t[i*2+1])
        else:
            new_mass_t.append(mass_t[i*2])
    if len(mass_t) % 2 == 1:
        new_mass_t.append(mass_t[-1])
    t_find(new_mass_t)

def t_sort(mass_t):
    for i in range(len(mass_t)):
        t_find(mass)
        mass[mass.index(res[-1])] = 9999
    return res

def s(m):
    r = 0
    for i in m:
        r += i
    return r

def e(p):
    su = [s(i) for i in p]

    return su.index(min(su))

def krit(m, n):
    p = [[0] for i in range(n)]

    for i in m:
        print(p)
        p[e(p)].append(i)

    return p

print()
print('T = {}'.format(list(reversed(t_sort(mass)))))
mass = mmm.copy()

res = []
a = krit(list(reversed(t_sort(mass))), 4)
mass = mmm.copy()

print(a)

print()
###
for i in a:
    print(s(i))
###
res = []
mass = mmm.copy()
print()
print('T = {}'.format(mass))

a = krit(mass, 4)
print(a)

mass = mmm.copy()
print()

for i in a:
    print(s(i))
mass = mmm.copy()
####
print()
res = []
print('T = {}'.format(t_sort(mass)))
res = []
mass = mmm.copy()

a = krit(t_sort(mass), 4)
res = []

print(a)

print()

for i in a:
    print(s(i))
mass = mmm.copy()