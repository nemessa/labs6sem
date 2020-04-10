from random import randint


class Chmod:
    def __init__(self, users=7, entity=4):
        self.rights_name = ['Top_secret', 'Secret', 'All_access']
        self.rights = [randint(0, 2) for i in range(entity)]
        self.users = [randint(0, 2) for i in range(users)]
        self.user_id = -1

    def request(self, entity):
        if self.users[self.user_id] <= self.rights[entity]:
            print('Successful')
        else:
            print('Access denied')


class User(Chmod):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        print('L = {}'.format(self.rights_name))
        print('O = [', end='')
        for i in self.rights:
            print('', self.rights_name[i], end='')
        print(' ]')
        print('S = [', end='')
        for i in self.users:
            print('', self.rights_name[i], end='')
        print(' ]')

    def __new__(cls, user_id):
        if 0 <= user_id <= 6:
            return object.__new__(cls)
        else:
            print('Access denied')

    def __str__(self):
        string = 'Entity for you:'
        for i in range(len(self.rights)):
            if self.users[self.user_id] <= self.rights[i]:
                string += ' Entity_{}'.format(i)
        return string


if __name__ == '__main__':
    while True:
        user = User(user_id=int(input('Enter a user: ')))
        while user:
            print('1) Show my entity',
                  '2) Request',
                  '0) Quit',
                  sep='\n')
            choice = input('Enter an action: ')
            if choice == '1':
                print(user)
            elif choice == '2':
                user.request(int(input('Enter index entity: ')))
            elif choice == '0':
                break
