using System;
using Ex1;
using System.Collections.Generic;

namespace Ex1
{
    class Program
    {
        static void Main123123(string[] args)
        {
            // From class which was in the same file before moving to separate file
            // Car c1 = new Car();
            // c1.Brand = "honda";
            // c1.Color = "Blue";
            // c1.ThisIsYourCar();

            //This builds the car based on the car.cs file in the same directory
            Car c1 = new Car("qwer", "qqq",4);
            c1.ThisIsYourCar();

            Car c2 = new Car("zxcv", "zzz",4);
            c2.ThisIsYourCar();
            
            Car c3 = new Car("asdf", "xxx",4);
            c3.ThisIsYourCar();
            int wheel = Convert.ToInt32(Console.ReadLine());
            c3.MethodOne(wheel);
            c3.ThisIsYourCar();
            System.Console.WriteLine(c3.Wheels);
            string test = c3.MethodTwo("myname");
            System.Console.WriteLine(test);

            // List?
            List<int> numbers = new List<int>();
            // numbers.Add(4);
            // numbers.Add(9);
            // Console.WriteLine(numbers[1]);
            // numbers.ForEach(Console.WriteLine);

            List<Car> cars = new List<Car>();
            cars.Add(c1);
            cars.Add(c2);
            cars.Add(c3);
            // List<Car>(){c1,c2,c3};

            foreach (var item in cars)
            {
                System.Console.WriteLine($"My car is {item.Color} and its brand is {item.Brand}");
            }

            // hashtable

            // for (int i = 0; i < 10; i++)
            // {
            //     Console.WriteLine(i);
            // }
        }
        static void Main(string[] args)
        {
            int result = Fibonacci(5);
            Console.WriteLine(result);
            Console.ReadKey(true);
        }
        static int Fibonacci(int n)
        {
            int n1 = 0;
            int n2 = 1;
            int sum = 0;

            for (int i = 2; i < n; i++)
            {
                sum = n1 + n2;
                n1 = n2;
                n2 = sum;
            }
            return n == 0 ? n1 : n2;
        }
    }
}