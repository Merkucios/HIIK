using System;
using System.Collections.Generic;


namespace Laboratornaya_Rabota4
{
    internal class JacobiMethod
    {
        public static bool diagonalDominanceStatement(double[,] _sys_of_lin_eq)
        {
            double _diagonal_elem = 0;
            double _sum_elem = 0;
            bool _check; int _counter_check = 0;
            for (int i = 0; i < _sys_of_lin_eq.GetLength(0); i++)
            {
                _diagonal_elem = _sys_of_lin_eq[i, i];

                for (int j = 0; j < _sys_of_lin_eq.GetLength(1) - 1; j++)
                {
                    if (i != j)
                    {
                        _sum_elem += _sys_of_lin_eq[i, j];
                    }

                }
                if (Math.Abs(_diagonal_elem) >= Math.Abs(_sum_elem))
                {
                    _check = true;
                    _counter_check++;
                }
                _sum_elem = 0;

            }

            if (_counter_check == _sys_of_lin_eq.GetLength(0))
            {
                
                return true;
            }
            else
            {
                
                return false;
            }
        }

        public static void calculationOfUnknown(double[,] _sys_of_lin_eq, double eps)
        {
            static void Schitaem_Unknown(double[,] _sysEq, double eps = 0.001)
            {
                double[] _old_values = new double[_sysEq.GetLength(0)];
                string[] _unknowns = { "x1", "x2", "x3", "x4", "x5" };
                byte k = 0;
                for (int i = 0; i < _old_values.Length; i++)
                {
                    _old_values[i] = 0.0;
                }

                while (true)
                {
                    double[] _new_values = new double[_sysEq.GetLength(0)];
                    Console.WriteLine($"Шаг {k+1}"); ;
                    for (int i = 0; i < _sysEq.GetLength(0); i++)
                    {
                        _new_values[i] = _sysEq[i, _sysEq.GetLength(0)];

                        for (int j = 0; j < _sysEq.GetLength(0); j++)
                        {
                            if (i != j)
                            {
                                _new_values[i] -= _sysEq[i, j] * _old_values[j];
                            }
                        }
                        _new_values[i] /= _sysEq[i, i];
                        Console.WriteLine($"{_unknowns[i]} = {_new_values[i]:F3}");
                        
                    }
                    double _diff = 0.0;
                    for (int i = 0; i < _sysEq.GetLength(0); i++)
                        _diff += Math.Abs(_new_values[i] - _old_values[i]);

                    if (_diff < eps) break;

                    _old_values = _new_values;
                    k++;
                    
                }
            }
            if (diagonalDominanceStatement(_sys_of_lin_eq) == false)
            {
                Console.WriteLine("Диагональное преобладание не проходит условие задачи" + 
                    "\nВведите другое СЛАУ ");
            }
            else
            {
                Schitaem_Unknown(_sys_of_lin_eq , eps);
            }
        }
    }
}
