//10.	В двумерном массиве целых чисел поменять местами столбцы, симмет-ричные относительно середины массива (вертикальной линии).
#include<iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
    int a[100][100], i, j, t, n, m;
    cout << "n= "; cin >> n;
    cout << "m= "; cin >> m;
    cout << "Matr:" << endl;
    srand(time(NULL));
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            a[i][j] = rand() % 10;
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    for (j = 0; j < m / 2; j++)
        for (i = 0; i < n; i++)
        {
            t = a[i][j]; a[i][j] = a[i][m - 1 - j]; a[i][m - 1 - j] = t;
        }
    cout << endl << "New matr:" << endl;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
            cout << a[i][j] << " ";
        cout << endl;
    }
    return 0;
}