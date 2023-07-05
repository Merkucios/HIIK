//2.	Дана вещественная матрица размером NxM. Упорядочить ее строки по возрастанию их первых элементов.
#include "iostream"
#include <iomanip>
using namespace std;


int main()
{
    double** a, b;
    int i, j, n, m, k;
    cout << "Vvedite razmer: n,m" << endl;
    cin >> n >> m;
    a = new double* [n];
    for (i = 0; i < n; i++)
        a[i] = new double[m];
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
        {
            cout << "Vvedite a[" << i << "][" << j << "]:";
            cin >> a[i][j];
        }
    cout << "MASSIVE:" << endl;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
            cout << setw(10) << a[i][j] << " ";
        cout << endl;
    }
    for (i = 0; i < n - 1; i++) {
        for (k = 0; k < n - 1; k++) {
            if (a[k][0] > a[k + 1][0]) {
                for (j = 0; j < m; j++) {
                    b = a[k][j];
                    a[k][j] = a[k + 1][j];
                    a[k + 1][j] = b;
                }
            }
        }
    }
    cout << "Result:" << endl;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
            cout << setw(10) << a[i][j] << " ";
        cout << endl;
    }
    for (i = 0; i < n; i++)
        delete[] a[i];
    delete[]a;
    a = NULL;
    return 0;
}