#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cout << "Vvedite razmer: n,m" << endl;
    cin >> n >> m;
    vector<vector<int>> matrix(n, vector<int>(m));
    int max_sum = 0;
    int max_sum_index = 0;
    for (int i = 0; i < n; ++i) {
        int sum = 0;
        bool only_odd = true;
        for (int j = 0; j < m; ++j) {
            cout << "Vvedite myArr[" << i << "][" << j << "]:";
            cin >> matrix[i][j];
            if (matrix[i][j] % 2 == 0) {
                only_odd = false;
                break;
            }
            sum += abs(matrix[i][j]);
        }
        if (only_odd && sum > max_sum) {
            max_sum = sum;
            max_sum_index = i;
        }
    }
    cout << "Index of the row with the maximum sum of odd elements: " << max_sum_index << endl;
    return 0;
}