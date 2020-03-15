class test:
    def __init__(self):
        self.mass = list(range(10))

    def __getitem__(self, key):
        self.key = key
        return self

    def __setitem__(self, key, value):
        self.mass[key] = value

    def __delitem__(self, key):
        del self.mass[key]

    def mul(self, value):
        self.mass[self.key] *= value

if __name__ == '__main__':
    a = test()
    del a[1]
    print(a.mass)