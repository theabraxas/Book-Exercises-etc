using System;
using System.Diagnostics;

namespace ex2
{
    class Program
    {
        static void Main(string[] args)
        {

            int result = Fibonacci(5);
            Console.WriteLine(result);
            Console.ReadKey(true);
        }
        static int Fibonacci(int n)
        {
            Debug.WriteLine($"Entering {nameof(Fibonacci)} method");
            Debug.WriteLine($"We are looking for the {n}th number");            
            int n1 = 0;
            int n2 = 1;
            int sum = 0;

            for (int i = 2; i < n; i++)
            {
                sum = n1 + n2;
                n1 = n2;
                n2 = sum;
                Debug.WriteLineIf(sum == 1, $"sum is 1, n1 is {n1}, n2 is {n2}"); 
            }
            return n == 0 ? n1 : n2;
        }
    }
}