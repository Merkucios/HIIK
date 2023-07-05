// Third.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <math.h>

using namespace std;

const double math_pi = 3.14159265358979311600;
const double math_e = 2.718281828459045;
const double math_phi = 1.618033988749895;

int main()
{
    setlocale(LC_ALL, "Russian");

    double w, a;
    double resultX, resultY;

    cout << "Введите значение для w:\t";
    cin >> w;
    cout << "\nВведите значение для a:\t";
    cin >> a;
    cout << "\n";

    resultX = (math_pi / 2 - math_phi) / w;
    resultY = a * pow(math_e, -a * resultX) * sin(w * resultX);

    cout << "Результат вычислений для X равен:\t" << resultX << "\n";
    cout << "Результат вычислений для Y равен:\t" << resultY << "\n";
}

