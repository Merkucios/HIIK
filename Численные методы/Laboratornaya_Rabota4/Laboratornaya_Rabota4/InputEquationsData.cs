using System;
using System.Collections.Generic;

namespace Laboratornaya_Rabota4
{
    internal class InputEquationsData
    {
        public static double[,] InputData(int _number_of_equations)
        {
            int x; int k = 1;
            int _number_of_unknown = _number_of_equations + 1;
            double[,] result = new double[_number_of_equations, _number_of_equations + 1];

            List<string> unknown = new List<string>();
            unknown = InputUnkown(_number_of_unknown);
            

            for (int i = 0; i < result.GetLength(0); i++, k++)
            {
                Console.WriteLine($"Введите коэффициенты для {k} уравнения");

                for (int j = 0; j < result.GetLength(1); j++)
                {
                    Console.Write($"{unknown[j]} = ");
                    x = int.Parse(Console.ReadLine());
                    result[i, j] = x;
                }
            }
            return result;
        }

        public static List<string> InputUnkown(int _number_of_equations)
        {
            List<string> result = new List<string>();
            int k = 1;

            for (int i = 0; i < _number_of_equations; i++, k++)
            {
                if (i == _number_of_equations - 1) { result.Add($"b"); }
                else { result.Add($"x{k}"); }
                
            }
            return result;
        }
    }
}
