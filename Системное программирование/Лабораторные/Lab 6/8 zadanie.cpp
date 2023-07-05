//8.	Даны целые числа А1,...,А10, целочисленная квадратная матрица порядка N.
//	Заменить нулями в матрице те элементы, для которых имеются равные числа среди А1,...,А10.
#include <iostream>
using namespace std;

int main()
{
    const int N = 20;
    int A[N][N] = { { 0 } };

    for (int row = 0; row < N; row++)
    {
        for (int col = 0; col < N; col++)
        {
            A[row][col] = std::rand() % 9 + 1;
            std::cout << A[row][col] << " ";
        }

        std::cout << endl;
    }

    std::cout << endl;

    for (int row = 0; row < N; row++)
        for (int col = 0; col < N; col++)
            if (((row + col) % 2) == 0)
            {
                int r_fwd = 0, c_fwd = 0;
                while (r_fwd < N)
                {
                    if (c_fwd >= N) { c_fwd = 0; r_fwd++; }
                    if (A[r_fwd][c_fwd] == A[row][col] && r_fwd != row && c_fwd != col)
                        A[r_fwd][c_fwd] = 0;

                    c_fwd++;
                }
            }

    for (int row = 0; row < N; row++)
    {
        for (int col = 0; col < N; col++)
            std::cout << A[row][col] << " ";

        std::cout << endl;
    }

    std::cout << endl << endl;

    std::cin.get();
}