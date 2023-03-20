// Forth.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    setlocale(LC_ALL, "Russian");
    
    double a1, a2, b1, b2, c1, c2;
    double resultX, resultY;

    cout << "Введите коээфициенты первого уравнения:\n";
    cin >> a1 >> b1 >> c1;

    cout << "Введите коээфициенты второго уравнения:\n";
    cin >> a2 >> b2 >> c2;

    resultX = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1);
    resultY = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1);

    cout << "РЕЗУЛЬТАТ ДЛЯ X:\t" << resultX << "\n";
    cout << "РЕЗУЛЬТАТ ДЛЯ Y:\t" << resultY;

    return 0;

}
