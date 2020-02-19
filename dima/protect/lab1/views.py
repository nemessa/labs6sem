import unittest


class Alphabet:
    def __init__(self, alph):
        self.alph = alph

    def __new__(cls, alph):
        if len(set(alph)) == len(alph):
            return object.__new__(cls)
        else:
            return None

    def to_num(self, word):
        if set(word) <= set(self.alph):
            res = 0
            for i in range(len(word)):
                res += (len(self.alph) ** (len(word) - i - 1)) * (self.alph.index(word[i]) + 1)
                if i != len(word) - 1:
                    print('{}^({}-{})*{}'.format(len(self.alph), len(word), i + 1, self.alph.index(word[i]) + 1),
                          end=' + ')
                else:
                    print('{}^({}-{})*{}'.format(len(self.alph), len(word), i + 1, self.alph.index(word[i]) + 1))

            return res

    def to_word(self, num):
        try:
            ceil = int(num)
            words = []

            while ceil > 3:
                remainder = ceil % len(self.alph)
                ceil = ceil // len(self.alph)
                if remainder == 0:
                    ceil -= 1
                    remainder = len(self.alph)
                words = [remainder] + words
                print('{}{}*3+{}'.format('(' * (len(words) - 1), ceil, remainder), end='')
                for i in words[1:-1]:
                    print(')3+{}'.format(i), end='')
                if len(words) > 1:
                    print(')3+{}'.format(words[-1]))
                else:
                    print()

            words = [ceil] + words

            for i in range(len(self.alph)):
                for j in range(len(words)):
                    if words[j] == i + 1:
                        words[j] = self.alph[i]

            return ''.join(words)

        except ValueError:
            return None


class TestAlphabet(unittest.TestCase):
    def test_incorrect_alphabet(self):
        self.assertEqual(Alphabet('aa'), None)

    def test_correct_alphabet(self):
        self.assertEqual(Alphabet('abc').alph, 'abc')

    def test_a(self):
        self.assertEqual(Alphabet('abc').to_num('a'), 1)

    def test_caba(self):
        self.assertEqual(Alphabet('abc').to_num('caba'), 97)

    def test_incorrect_word(self):
        self.assertEqual(Alphabet('abc').to_num('cabad'), None)

    def test_321(self):
        self.assertEqual(Alphabet('abc').to_word('321'), 'cbbac')

    def test_34631(self):
        self.assertEqual(Alphabet('abc').to_word('34631'), 'aacbaaaabb')

    def test_incorrect_num(self):
        self.assertEqual(Alphabet('abc').to_word('a321'), None)

    '''def test_incorrect_num(self):
        self.assertEqual(Alphabet('abc').to_word('888'), 'cabbac')'''


if __name__ == '__main__':
    unittest.main()

    a = Alphabet('abc')

    print(a.to_word('4'))
