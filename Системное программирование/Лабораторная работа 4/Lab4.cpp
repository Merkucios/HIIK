// Lab4.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <math.h>
#include <string>

using namespace std;

#pragma region Все задания 

void f1();
void f2();
void f3();
void f4();
void f5();
void f6();
void f7();
void f8();
void f9();
void f10();
void f11();
void f12();
void f13();
void f14();
void f15();
void f16();
void f17();
void f18();
void f19();
void f20();
void f21();
void f22();
#pragma endregion


int main()
{
    setlocale(LC_ALL, "Russian");
    
    f20();
    
}
void f1()
{
    cout << "Цикл с предусловием:\n";

    int res, i, res2, i2, res3, i3;
    res = 1;
    i = 1;

    while (i <= 10)
    {
        res = res * i;
        i++;
    }
    cout << res << "\nЦикл с постусловием:\n";

    res2 = 1;
    i2 = 1;
    do
    {
        res2 = res2 * i2;
        i2++;
    } while (i2 <= 10);
    cout << res2 << "\nЦикл с параметром:\n";

    res3 = 1;

    for (i3 = 1; i3 <= 10; i3++)
    {
        res3 *= i3;
    }
    cout << res3;
}
void f2()
{
    int a, k = 0;

    cout << "Напишите число: ";
    cin >> a;

    while (a > 0)
    {
        a = a / 10;
        k++;
    }

    cout << "Число цифр: " << k << endl;
}
// TODO: f3()
void f3()
{
    int taler = 1770;
    int horse = 31, bull = 21;
    // 31x + 21y = 1770
    // x = 1770 - 21y / 31
    // y = 1770 - 31x / 21

    for(int i = 1; i * bull <= taler; i++)
    {
        if((taler - i * bull) % horse == 0)
        {
            cout << "Кол-во быков\t" << i << endl;
            cout << "Кол-во лошадей\t" << (taler - i * bull) / horse << "\n";
        }
    }

    
    
}
void f4()
{
    double x, resultY;
    resultY = 0;
    cout << "Введите число x:\t" << endl;
    cin >> x;
    for(int i = 1; i <= 30; i++)
    {
        resultY += pow(cos(x), i);
    }
    cout << "Результат Y = cos(x) ^ i:\t" << resultY << endl;
}
void f5()
{
    double y = 0; 
    cout << "y = ";
    for (double i = 1.0; i < 2.1; i += 0.1) { 
        
        y += sin(i); 
    }

    cout << y << endl; 
}
void f6()
{
    bool p;
    int n;
    cout << "Введите n:\t";
    cin >> n;
    int counter = 0;
    string isProstoe;

    for(int i = 1; i <= n; i++)
    {
        if(n % i == 0)
        {
            counter++;
        }
        if(counter > 2)
        {
            p = false;
            isProstoe = "не простое число";
        }
        else 
        {
            p = true;
            isProstoe = "простое число";
        }
    }
    cout << n << " Простое число?\t" << isProstoe << endl;
}
void f7()
{
    double sum = 1;
    double dx = 0.5;
    double x = 1;

    for (int i = 1; i < 21; i++)
    {
        sum *= x * x;
        x += dx;
        cout << i << endl;
    }

    cout << sum;
}
void f8()
{
    int x;
    int k = 0;
    for (x = 100; x <= 999; x++)
    {
        int a, b, c;
        a = x % 10;
        b = x / 10 % 10;
        c = x / 100;
        int n = a + b + c;
        if ((n > 1) && (n < 27)) k++;
    }

    cout << "Количество чисел от 100 до 999 = " << k << endl;
}
void f9()
{
    cout << "Все числа без повторений цифр в десятичной записи: ";
    {
        int j, a, b, c;
        for (j = 100; j < 1000; j++) {
            a = j % 10;
            b = j / 10 % 10;
            c = j / 100;
            if (a != b && a != c && b != c)
            {
                cout << j << " ";
            }
        }
    }
}
void f10()
{
    // 10.Определить количество натуральных чисел, не превышающих n , которые не делятся на 11.
    int num; int counter = 0;
    cout << "Введите число:\t";
    cin >> num;
    cout << endl;

    for(int i = 0; i < num; i++)
    {
        if(i % 11 != 0)
        {
            counter++;
        }
    }
    cout << "Количество чисел равно:\t" << counter;
    cout << endl;

}
void f11()
{
    int x, y, z;
    cout << "Введите число :\t";
    cin >> x;
    cout << endl;
    while (true)
    {
        y = x % 10;
        x = x / 10;
        if (y == 3)
        {
            cout << "Есть число 3" << endl;
            break;
        }
        if (x == 0)
        {
            cout << "Нет числа 3" << endl;
            break;
        }


    }
    cin >> x;
    y = x % 10;
    x = x / 10;
    z = y;
    while (true)
    {
        y = x % 10;
        x = x / 10;
        z = z * 10 + y;
        if (x == 0)
            break;
    }
    cout << z;
}
void f12()
{
    int n, m, k = 0;

    cout << "Введите натуральное число: "; cin >> n;

    m = n;

    while (m > 10)
    {
        m /= 10;
        k++;
    }
    int t = n % 10;

    n = n + (t - m) * pow(10, k) - (t - m);
    cout << n << endl;
    n = n * 10 + 1 + pow(10, k + 2);
    cout << n << endl;
}
void f13() 
{
    double x = 2;
    double xPrevious;
    double dx = 0.2;
    double result = 0;

    cout << "10 итераций для формулы\n";
    cout << "(x^3 + 8)^0.5\n";

    xPrevious = x;

    for (int i = 0; i <= 10; i++)
    {
        x = xPrevious + pow(dx,2);
        xPrevious = x;

        result += pow((pow(x, 3) + 8), 0.5);
    }
    cout << "Результат равен\t" << result;
    cout << endl;
}
void f14()
{
    double x = 2;
    double xPrevious;
    double dx = 1;
    double result = 0;

    cout << "8 итераций для формулы\n";
    cout << "x^2 + 1.5 / |x| + 10\n";

    xPrevious = x;

    for (int j = 0; j <= 8; j++)
    {
        x = xPrevious + dx;
        xPrevious = x;

        result += (pow(x, 2) + 1.5) / (abs(x) + 10);
    }
    cout << "Результат равен\t" << result;
    cout << endl;
}
void f15()
{
    double x = 1;
    double xPrevious;
    double dx = 0.1;
    double result = 0;

    cout << "15 итераций для формулы\n";
    cout << "sin x^2\n";

    xPrevious = x;

    for (int i = 0; i <= 15; i++)
    {
        x = xPrevious + dx;
        xPrevious = x;

        result += (sin(pow(x, 1)));
    }
    cout << "Результат равен\t" << result;
    cout << endl;
}
// TODO f16() Работает через костыль, числа 21,25,27 не являются простыми
void f16()
{
    // 6 =
}
void f17()
{
    double x = 1, y = 0.5;
    double xPrevious, yPrevious;
    double dx = 0.5, dy = 0.2;

    double result = 0;

    cout << "10 итераций для формулы\n";
    cout << "(x+y)/(|x|+|y|)\n";

    xPrevious = x;
    yPrevious = y;

    for (int i = 0; i <= 10; i++)
    {
        x = xPrevious + dx;
        y = yPrevious + dy;
        xPrevious = x;
        yPrevious = y;

        result += (x + y) / (abs(x) + abs(y));
    }
    cout << "Результат равен\t" << result;
    cout << endl;
}
void f18()
{
    double x = 3, y = 2;
    double xPrevious, yPrevious;
    double dx = 0.1, dy = 0.2;

    double result = 0;

    cout << "10 итераций для произведения формулы\n";
    cout << "x^2 / y^2 + x\n";

    xPrevious = x;
    yPrevious = y;

    for (int i = 0; i <= 10; i++)
    {
        x = xPrevious + dx;
        y = yPrevious + dy;
        xPrevious = x;
        yPrevious = y;

        result *= pow(x, 2) / pow(y, 2) + abs(x);
    }
    cout << "Результат равен\t" << result;
    cout << endl;
}
void f19()
{
    double x = 2;
    double xPrevious;
    double dx = 0.1;
    double result = 0;

    cout << "10 итераций для формулы\n";
    cout << "x^2 + x + 7\n";

    xPrevious = x;

    for (int i = 0; i <= 10; i++)
    {
        x = xPrevious + dx;
        xPrevious = x;

        result += pow(x, 2) + x + 7;
    }
    cout << "Результат равен\t" << result;
    cout << endl;
}
void f20()
{
    double x = 3;
    double xPrevious;
    double dx = 0.2;
    double result = 0;

    cout << "10 итераций для формулы\n";
    cout << "sqrt(x) + 5.3\n";

    xPrevious = x;

    for (int i = 0; i <= 10; i++)
    {
        x = xPrevious + dx;
        xPrevious = x;

        result += sqrt(x) + 5.3;
    }
    cout << "Результат равен\t" << result;
    cout << endl;
}
void f21()
{
    double x = 2;
    double xPrevious;
    double dx = 0.3;
    double result = 0;

    cout << "20 итераций для формулы\n";
    cout << "cos(x^2)\n";

    xPrevious = x;

    for (int i = 0; i <= 20; i++)
    {
        x = xPrevious + dx;
        xPrevious = x;

        result += cos(pow(x, 2));
    }
    cout << "Результат равен\t" << result;
    cout << endl;
}
void f22()
{
    double x = 1;
    double xPrevious;
    double dx = 0.1;
    double result = 0;

    cout << "12 итераций для формулы\n";
    cout << "ctg(x^3)\n";

    xPrevious = x;

    for (int i = 0; i <= 12; i++)
    {
        x = xPrevious + dx;
        xPrevious = x;

        result += 1 / tan(pow(x, 3));
    }
    cout << "Результат равен\t" << result;
    cout << endl;
}





