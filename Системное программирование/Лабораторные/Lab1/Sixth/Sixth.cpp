// Sixth.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <math.h>

using namespace std;
const double math_pi = 3.14159265358979311600;

int main()
{
    setlocale(LC_ALL, "Russian");

    double r = 20;
    double R;
    double Scol;
    while (true)
    {
        cout << "Введите радиус внешнего круга:\t" << "\n";
        cin >> R;

        if (R < 20) 
        {
            cout << "Вы ввели недопустимое значение для внешного радиуса круга!!\n";
            cout << "Введите радиус значение которого больше 20\n";
        }
        else if (R > 20) 
        {
            break;
        }
    }
    Scol = math_pi * (R - r);
    cout << "Площадь кольца равна:\t" << Scol << "\n";
    
    return 0;
}