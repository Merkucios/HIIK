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
    cout << "Vvedite razmer: n,n" << endl;
    cin >> n;
    vector<vector<int>> myArr(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << "Vvedite myArr[" << i << "][" << j << "]:";
            cin >> myArr[i][j];
        }
    }
    if (isSymmetric(myArr, n)) {
        cout << "Matrix is symmetric" << endl;
    }
    else {
        cout << "Matrix is not symmetric" << endl;
    }
    return 0;
}