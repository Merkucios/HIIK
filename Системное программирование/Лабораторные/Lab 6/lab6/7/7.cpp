#include <iostream>
#include <climits>

using namespace std;

const int N = 100;
int myArr[N][N];

int main() {
    int m, n;
    cout << "Vvedite razmer: n,m" << endl;
    cin >> m >> n;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            cout << "Vvedite myArr[" << i << "][" << j << "]:";
            cin >> myArr[i][j];
        }
    int min_col = INT_MAX;
    int min_product = INT_MAX;
    for (int j = 0; j < n; j++) {
        int product = 1;
        bool flag = true;
        for (int i = 0; i < m; i++) {
            if (abs(myArr[i][j]) > 10) {
                flag = false;
                break;
            }
            product *= myArr[i][j];
        }
        if (flag) {
            if (product < min_product) {
                min_product = product;
                min_col = j;
            }
        }
    }
    if (min_col == INT_MAX) {
        cout << "No such column found" << endl;
    }
    else {
        cout << "The column with minimum product is: " << min_col << endl;
    }
    return 0;
}
