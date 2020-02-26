class Alph:
    def __init__(self):
        self. alph = '01'

    def razl(self, sump):
        mass = [None, sump]
        for i in range(13):
            mass.append(sump * (len(mass[-1]) + 1))

        return mass

    def comp(self, left, right):
        if not(left and right):
            return None
        else:
            return left + right

    def chet(self):
        mass = ['S0Z', '1', '0Z', '1', '0ZSZ']
        print(''.join(mass))

if __name__ == '__main__':
    print(Alph().chet())