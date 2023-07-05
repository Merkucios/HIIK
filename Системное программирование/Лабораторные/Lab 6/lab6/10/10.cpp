#include<iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
    int myArr[100][100], i, j, t, n, m;
    cout << "n= "; cin >> n;
    cout << "m= "; cin >> m;
    cout << "Matr:" << endl;
    srand(time(NULL));
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            myArr[i][j] = rand() % 10;
            cout << myArr[i][j] << " ";
        }
        cout << endl;
    }
    for (j = 0; j < m / 2; j++)
        for (i = 0; i < n; i++)
        {
            t = myArr[i][j]; myArr[i][j] = myArr[i][m - 1 - j]; myArr[i][m - 1 - j] = t;
        }
    cout << endl << "New matr:" << endl;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
            cout << myArr[i][j] << " ";
        cout << endl;
    }
    return 0;
}