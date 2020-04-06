from random import randint


class Chmod:
    def __init__(self, entity=4):
        self.rights_name = ['Grant', 'Write', 'Read']
        self.rights = [[0, 0, 0] for i in range(entity)]
        self.entity = [randint(0, 100) for i in range(entity)]

    def write(self, num, new):
        if self.rights[num][1] == 1:
            self.read(num)
            old = self.entity[num]
            self.entity[num] = new
            print('Entity {} = {} has been changed to {}'.format(num, old, self.entity[num]))
        else:
            print('Dont have rights to write')

    def read(self, num):
        if self.rights[num][2] == 1:
            print('Entity {} ='.format(num), self.entity[num])
        else:
            print('Dont have rights to read')

    def change_right(self, num, right, new_right):
        if self.rights[num][0] == 1:
            self.rights[num][right] = new_right
            print('Right successful changed')
        else:
            print('Dont have rights to grant')


class User(Chmod):
    def __init__(self, admin=1, entity=4):
        super().__init__()
        print('Initialization was successful')
        if admin == 0:
            self.rights = [[1, 1, 1] for i in range(entity)]
        else:
            self.rights = [[randint(0, 1), randint(0, 1), randint(0, 1)] for j in range(entity)]
        for j in self.rights:
            if j[-1] == 0 and j[-2] == 1:
                j[-1] = 1

    def __str__(self):
        string = 'Your roots:\n'
        for i in range(len(self.rights)):
            string += 'Entity {}: '.format(i)
            c = 0
            tmp = ''
            for j in range(len(self.rights_name)):
                if self.rights[i][j]:
                    c += 1
                    tmp += self.rights_name[j] + ' '
            if c == 0:
                string += 'No rights'
            elif c == 3:
                string += 'All rights'
            else:
                string += tmp
            string += '\n'
        return string


if __name__ == '__main__':
    while True:
        user = User(admin=int(input('Enter a user: ')))
        print(user)
        while True:
            print('1) Show my roots',
                  '2) Read entity',
                  '3) Write to entity',
                  '4) Change right',
                  '0) Quit',
                  sep='\n')
            choice = input('Enter an action: ')
            if choice == '1':
                print(user)
            elif choice == '2':
                user.read(int(input('Enter index entity: ')))
            elif choice == '3':
                user.write(int(input('Enter index entity: ')), int(input('Enter new value to entity: ')))
            elif choice == '4':
                user.change_right(
                    int(input('Enter index entity: ')),
                    int(input('Enter index right: ')),
                    int(input('Enter new right for entity: '))
                )
            elif choice == '0':
                break
