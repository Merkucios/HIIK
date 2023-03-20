#include <iostream>
#include <cmath>
#include <iomanip>;
using namespace std;


double factorial(int n) {
    double result = 1.0;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

double nonRecursiveSum(double x, int n) {
    double s = 1.0;
    for (int i = 1; i <= n; i++) {
        double term = (pow(i, 2) + 1) / factorial(i) * pow(x / 2.0, i);
        s += term;
    }
    return s;
}

double recursiveSum(double x, int n, double s = 1.0, int i = 1) {
    if (i > n) {
        return s;
    }
    double term = (pow(i, 2) + 1) / factorial(i) * pow(x / 2.0, i);
    s += term;
    return recursiveSum(x, n, s, i + 1);
}

int main() {
    setlocale(LC_ALL, "RU");
    double xk = 0.1;        // Начальное значение
    double xh = 1.0;        // Конечное значение
    double h = (xh - xk) / 10.0;    // Шаг
    int n = 30;             // Число элементов для суммы
    const double MATH_E = 2.71828182846; // Константа E = 2,71

    cout << setw(5) << "x" << setw(15) << "y" << setw(20) << "s" << endl;
    cout << "------------------------------------------------------------" << endl;
    double y, s;
    for (double x = xk; x <= xh; x += h) {
        // Формула Y = (x^2 / 4 + x / 2 + 1) * e^(x/2)
        y = (pow(x, 2) / 4.0 + x / 2.0 + 1.0) * pow(MATH_E,x / 2);

        // Вычисление суммы через цикл for 
        s = nonRecursiveSum(x, n);
        cout << "| x = " << x << "| , | y = " << y << "| , | s (через цикл) = " << s << "|" << endl;

        // Вычисление суммы через рекурсию 
        s = recursiveSum(x, n);
        cout << "| x = " << x << "| , | y = " << y << "| , | s (через рекурсию) = " << s << "|" << endl;
    }

    return 0;
}
