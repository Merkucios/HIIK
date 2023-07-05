//1.	Дана вещественная матрица размером NxM. Переставляя ее строки и столбцы, добиться того,
//     чтобы наибольший элемент (один из них) оказал-ся в верхнем левом углу.
#include<iostream>
using namespace std;


int main()
{
    int i, j, n, m;
    double mas[3][4], max, cur;

    cout << "Write elemets 3 X 4:" << endl; //дальше ввом 3 строки по 4 элемента через пробел, так удобнее
    for (i = 0; i < 3; i++)
        for (j = 0; j < 4; j++)
            cin >> mas[i][j];

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
            cout << mas[i][j] << "\t";
        cout << endl;
    }

    max = mas[0][0];
    for (i = 0; i < 3; i++)
        for (j = 0; j < 4; j++)
            if (mas[i][j] > max)
            {
                max = mas[i][j];
                n = i, m = j;
            }
    cout << "Max = mas" << "[" << n << "][" << m << "] = " << max << endl;

    //обмен верхнего левого и найденного максимального элементов
    cur = mas[0][0];
    mas[0][0] = max;
    mas[n][m] = cur;

    cout << "Result:\n";
    for (int i = 0; i < 7; i++)
    {
        for (int j = 0; j < 4; j++)
            cout << mas[i][j] << "\t";
        cout << endl;
    }

    system("pause");
    return 0;
}