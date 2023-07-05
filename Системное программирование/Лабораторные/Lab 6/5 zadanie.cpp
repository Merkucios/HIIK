//5.	Определить, является ли заданная целочисленная квадратная матрица по-рядка N симметричной относительно главной диагонали.
#include <iostream>
#include <vector>

using namespace std;

bool isSymmetric(vector<vector<int>> matrix, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] != matrix[j][i]) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    int n;
    cin >> n;
    vector<vector<int>> matrix(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }
    if (isSymmetric(matrix, n)) {
        cout << "Matrix is symmetric" << endl;
    }
    else {
        cout << "Matrix is not symmetric" << endl;
    }
    return 0;
}