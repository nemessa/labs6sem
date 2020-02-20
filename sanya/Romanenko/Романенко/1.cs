using System;
using System.Collections.Generic;

namespace Романенко
{
    class Program
    {

        static void WordToInt()
        {
            Console.WriteLine("Введите словарь: ");
            //словарь
            string l = Console.ReadLine().ToString();

            Console.WriteLine("Введите слово: ");
            string word = Console.ReadLine().ToString();

            List<int> index = new List<int>();

            for (int i = 0; i < word.Length; i++)
            {
                for (int j = 0; j < l.Length; j++)
                {
                    if (l[j] == word[i]) index.Add(j);
                }
            }

            int n = l.Length;
            int k = word.Length;
            int sum = 0;

            for (int i = 0, j = 0; i < word.Length; i++, j++)
            {
                sum += Convert.ToInt32(Math.Pow(n, --k)) * (index[j] + 1);
                if (i != 0) Console.Write(" + ");
                Console.Write(n + "^" + k + " * " + (index[j] + 1));
            }
            Console.WriteLine(" = " + sum);
        }

        static void IntToWord()
        {
            Console.WriteLine("Введите словарь: ");
            //словарь
            string l = Console.ReadLine().ToString();

            Console.WriteLine("Введите N: ");
            int N = Convert.ToInt32(Console.ReadLine());

            string view = "";
            int tmp2 = 0;
            string word = "";
            while (l.Length <= N / l.Length)
            {
                if (N % l.Length == 0)
                {
                    Console.WriteLine(N / l.Length - 1 + " * " + l.Length + " + " + l.Length);
                    string tmp = view;
                    view += ") * " + l.Length + " + " + l.Length + tmp;
                    word += l.Length;
                    N = N / l.Length - 1;
                }
                else
                {
                    Console.WriteLine(N / l.Length + " * " + l.Length + " + " + N % l.Length);
                    string tmp = view;
                    view = ") * " + l.Length + " + " + N % l.Length + tmp;
                    word += N % l.Length;
                    N = N / l.Length;
                }

                tmp2++;
            }
            word += l.Length;

            for (int i = 0; i < tmp2; i++) Console.Write('(');
            Console.WriteLine(l.Length + view);

            for (int i = word.Length - 1; i >= 0; i--) Console.Write(l[(word[i] - 49)]);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("1. Из слова в число");
            Console.WriteLine("2. Из числа в слово");
            char n = Convert.ToChar(Console.ReadLine());
            if ('1' == n) WordToInt();
            if ('2' == n) IntToWord();
                        
            Console.ReadKey();
        }
    }
}
