#include <iostream>
#include <cmath>
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

double nonRecursiveSum(double x, int n) {
    double s = 1.0;
    double ln3 = ln(3.0);
    double xPower = 1.0;
    double factorial = 1.0;

    for (int i = 1; i <= n; i++) {
        xPower *= x;
        factorial *= i;
        double term = ln3 / factorial * xPower;
        s += term;
    }

    return s;
}

double recursiveSum(double x, int n, double ln3 = ln(3.0), double xPower = 1.0, double factorial = 1.0, double s = 1.0, int i = 1) {
    if (i > n) {
        return s;
    }

    xPower *= x;
    factorial *= i;
    double term = ln3 / factorial * xPower;
    s += term;

    return recursiveSum(x, n, ln3, xPower, factorial, s, i + 1);
}

int main() {
    setlocale(LC_ALL, "RU");
    double xk = 0.1; // Начальное значение
    double xh = 1.0; // Конечное значение
    double h = (xh - xk) / 10.0;
    int n = 10; // Число элементов суммы

    double y, s;
    for (double x = xk; x <= xh; x += h) {
        // Функция Y = pow(3,x) || 3^x
        y = pow(3.0, x);

        // Метод через for 
        s = nonRecursiveSum(x, n);
        cout << "x = " << x << ", y = " << y << ", s (через цикл) = " << s << endl;

        // Метод через рекурсию |return func|
        s = recursiveSum(x, n);
        cout << "x = " << x << ", y = " << y << ", s (через рекурсию) = " << s << endl;
    }

    return 0;
}
