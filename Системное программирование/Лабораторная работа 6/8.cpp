#include <iostream>
using namespace std;

int main()
{
    const int N = 20;
    int myArr[N][N] = { { 0 } };

    for (int row = 0; row < N; row++)
    {
        for (int col = 0; col < N; col++)
        {
            myArr[row][col] = rand() % 9 + 1;
            cout << myArr[row][col] << " ";
        }

        cout << endl;
    }

    cout << endl;

    for (int row = 0; row < N; row++)
        for (int col = 0; col < N; col++)
            if (((row + col) % 2) == 0)
            {
                int r_fwd = 0, c_fwd = 0;
                while (r_fwd < N)
                {
                    if (c_fwd >= N) { c_fwd = 0; r_fwd++; }
                    if (myArr[r_fwd][c_fwd] == myArr[row][col] && r_fwd != row && c_fwd != col)
                        myArr[r_fwd][c_fwd] = 0;

                    c_fwd++;
                }
            }

    for (int row = 0; row < N; row++)
    {
        for (int col = 0; col < N; col++)
            cout << myArr[row][col] << " ";

        cout << endl;
    }

    cout << endl << endl;

    cin.get();
}