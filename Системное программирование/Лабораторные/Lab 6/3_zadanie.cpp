//3.	Дана вещественная матрица размером NхM. Упорядочить ее строки по возрастанию суммы их элементов.
#include <iostream>
#include <algorithm>

using namespace std;

bool compareRows(int* a, int* b, int m) {
    int sumA = 0, sumB = 0;
    for (int i = 0; i < m; i++) {
        sumA += a[i];
        sumB += b[i];
    }
    return sumA < sumB;
}

int main() {
    int n, m;
    cin >> n >> m;

    int** matrix = new int* [n];
    for (int i = 0; i < n; i++) {
        matrix[i] = new int[m];
        for (int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }

    sort(matrix, matrix + n, [m](int* a, int* b) { return compareRows(a, b, m); });

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    for (int i = 0; i < n; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;

    return 0;
}