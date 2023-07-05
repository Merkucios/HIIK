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
    cout << "Vvedite razmer: n,m" << endl;
    cin >> n >> m;

    int** myArr = new int* [n];
    for (int i = 0; i < n; i++) {
        myArr[i] = new int[m];
        for (int j = 0; j < m; j++) {
            cout << "Vvedite a[" << i << "][" << j << "]:";
            cin >> myArr[i][j];
        }
    }

    sort(myArr, myArr + n, [m](int* a, int* b) { return compareRows(a, b, m); });

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << myArr[i][j] << " ";
        }
        cout << endl;
    }

    for (int i = 0; i < n; i++) {
        delete[] myArr[i];
    }
    delete[] myArr;

    return 0;
}