#include <iostream>
#include <algorithm>

using namespace std;

const int N = 10;

void swap(int a[], int b[], int size) {
    for (int i = 0; i < size; ++i) {
        swap(a[i], b[i]);
    }
}

int main() {
    int arr[N][N];
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> arr[i][j];
        }
    }
    for (int i = 0; i < n / 2; ++i) {
        swap(arr[i], arr[n - i - 1], m);
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}