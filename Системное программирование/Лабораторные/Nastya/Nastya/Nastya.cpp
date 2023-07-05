// 1 - ый вариант
#include <iostream>
#include <cmath>
#include <math.h>
using namespace std;

double factorial(int n) {
    double result = 1.0;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

double ln(double x) {
    return log(x);
}

void nonRecursive()
{
    double xk = 0.1; // Начальное значение
    double xh = 1.0; // Конечное значение
    double h = (xh - xk) / 10.0;
    int n = 10; // Количество членов суммы

    double y, s;
    for (double x = xk; x <= xh; x += h) {
        // Формула Y = 3^x
        y = pow(3, x);

        // Формула суммы s = 1 ; s += ln^n(3) / n! * x^n
        s = 1.0;
        for (int i = 1; i <= n; i++) {
            double term = pow(ln(3.0), i) / factorial(i) * pow(x, i);
            s += term;
        }


        cout << "x = " << x << ", y = " << y << ", s = " << s << endl;
    }
}

int main() {
    nonRecursive();

    return 0;
}
