using System;
using System.Linq;
using System.Collections.Generic;

namespace Laboratornaya_Rabota4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int _number_of_equations; // Количество уравнений в СЛАУ
            Console.WriteLine("Введите точность");

            double eps = double.Parse(Console.ReadLine());
            Console.WriteLine("Введите количество уравнений в системе");
            _number_of_equations = int.Parse(Console.ReadLine());
            int _number_of_unknown = _number_of_equations + 1;

            List<string> _unknown_members = InputEquationsData.InputUnkown(_number_of_unknown); // Список неизвестных уравнения

            double[,] _num_of_eq = InputEquationsData.InputData(_number_of_equations);
            
            JacobiMethod.diagonalDominanceStatement(_num_of_eq);


            JacobiMethod.calculationOfUnknown(_num_of_eq, eps);

            Console.ReadKey();

        }    
    }
}
