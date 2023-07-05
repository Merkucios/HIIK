//4.	Дана вещественная матрица размером NхM. Упорядочить ее строки по возрастанию наибольших элементов.
#include <iostream>
#include <algorithm>

using namespace std;

bool compareRows(int* a, int* b, int m) {
    int maxA = a[0], maxB = b[0];
    for (int i = 1; i < m; i++) {
        maxA = max(maxA, a[i]);
        maxB = max(maxB, b[i]);
    }
    return maxA < maxB;
}

int main() {
    setlocale(LC_ALL, "Russian");
    int n, m;
    cout << "Введите размеры матрицы\n";
    cin >> n >> m;

    int** matrix = new int* [n];
    for (int i = 0; i < n; i++) {
        matrix[i] = new int[m];
        for (int j = 0; j < m; j++) {
	    cout << "Введите a[" << i << "][" << j << "]:";
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
    cin;
    return 0;
}