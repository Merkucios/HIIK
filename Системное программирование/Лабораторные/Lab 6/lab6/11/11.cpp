#include <iostream>
#include <cmath>
using namespace std;

const int N = 5;

void add_min_col(double a[][N], double b[][N], double c[][N]) {
    for (int j = 0; j < N; j++) {
        double min_val = b[0][j];
        for (int i = 1; i < N; i++) {
            if (b[i][j] < min_val) {
                min_val = b[i][j];
            }
        }
        for (int i = 0; i < N; i++) {
            c[i][j] = a[i][j] + min_val;
        }
    }
}

int main() {
    double a[N][N] = { {1, 2, 3, 4, 5},
                      {6, 7, 8, 9, 10},
                      {11, 12, 13, 14, 15},
                      {16, 17, 18, 19, 20},
                      {21, 22, 23, 24, 25} };
    double b[N][N] = { {25, 24, 23, 22, 21},
                      {20, 19, 18, 17, 16},
                      {15, 14, 13, 12, 11},
                      {10, 9, 8, 7, 6},
                      {5, 4, 3, 2, 1} };
    double c[N][N];
    add_min_col(a, b, c);
    cout << "Result matrix:" << endl;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << c[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}