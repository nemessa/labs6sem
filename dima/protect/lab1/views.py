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
                '''if i != len(word) - 1:
                    print('{}^({}-{})*{}'.format(len(self.alph), len(word), i + 1, self.alph.index(word[i]) + 1),
                          end=' + ')
                else:
                    print('{}^({}-{})*{}'.format(len(self.alph), len(word), i + 1, self.alph.index(word[i]) + 1))'''

            return res

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

if __name__ == '__main__':
    unittest.main()

    a = Alphabet('abc')

    print(a.to_num('caba'))