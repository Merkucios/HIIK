#include<iostream>
using namespace std;


int main()
{
    int i, j, n, m;
    double myArr[3][4], max, cur;

    cout << "Write elemets 3 X 4:" << endl; 
    for (i = 0; i < 3; i++)
        for (j = 0; j < 4; j++)
            cin >> myArr[i][j];

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
            cout << myArr[i][j] << "\t";
        cout << endl;
    }

    max = myArr[0][0];
    for (i = 0; i < 3; i++)
        for (j = 0; j < 4; j++)
            if (myArr[i][j] > max)
            {
                max = myArr[i][j];
                n = i, m = j;
            }
    cout << "Max = mas" << "[" << n << "][" << m << "] = " << max << endl;

    //обмен верхнего левого и найденного максимального элементов
    cur = myArr[0][0];
    myArr[0][0] = max;
    myArr[n][m] = cur;

    cout << "Result:\n";
    for (int i = 0; i < 7; i++)
    {
        for (int j = 0; j < 4; j++)
            cout << myArr[i][j] << "\t";
        cout << endl;
    }

    system("pause");
    return 0;
}