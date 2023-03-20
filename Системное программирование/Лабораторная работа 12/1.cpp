#include <iostream>
using namespace std;

float distance(float x1, float y1, float x2, float y2)
{
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

bool multiple(int x, int y)
{
    if (x % y == 0)
        return true;
    else
        return false;
}

void print(int x)
{
    cout << "x=" << x << endl;
}

void f1();
void f2();
void f3();


int main() {
    setlocale(LC_ALL, "Russian");  
    f1();
    cout << endl;
    f2();
    cout << endl;
    f3();
    cout << endl;

    return EXIT_SUCCESS;

    
}
void f1()
{
    float a, b, c, d, rez;
    cout << "Введите координаты точек: " << endl;
    cin >> a >> b >> c >> d;
    rez = distance(a, b, c, d);
    cout << "Результат: " << rez << endl;
}

void f2()
{
    int a, b; bool rez;
    cout << "Введите числа: " << endl;
    cin >> a >> b;
    rez = multiple(a, b);
    if (rez) 
        cout << "Первое число кратно второму" << endl;
    
    else
        cout << "Первое число некратно второму" << endl;
}

void f3() 
{
    print(7);
}
