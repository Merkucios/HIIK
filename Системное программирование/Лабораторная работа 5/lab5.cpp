#include <iostream>
#include <math.h>
using namespace std;

#pragma region Идентификатор процедур
void f1();
void f2();
void f3();
void f4();
void f5();
void f6();
void f7();
void f8();
void f9();
void f11();
void f12();
#pragma endregion


int main(int argc, char** argv)
{
    setlocale(LC_ALL, "Russian");

    // Ровно половина заданий
    f12();

}   

void f1()
{
    int myArr[10];
    const int length = sizeof(myArr) / sizeof(myArr[0]);
    int sumResult = 0;
    int max = 0, min = 0;

    for (int i = 0; i < length; i++)
    {
        cout << "Введите\t" << i + 1 << " элемент ";
        cin >> myArr[i];
        if (myArr[i] > max)
        {
            max = myArr[i];
        }
        if (myArr[i] < min)
        {
            min = myArr[i];
        }

    }
    cout << "Минимальный элемент:\t" << min << endl;
    cout << "Максимальный элемент:\t" << max << endl;


    for (int i = 0; i < length; i++)
    {
        sumResult += myArr[i];
    }

    cout << "Сумма элементов массива:\t" << sumResult;
}
void f2()
{
    const int n = 10;
    double pointX[n], pointY[n];
    int indexX, indexY;
    double distanceOfPoints;
    double ch = 0;

    const int length = sizeof(pointX) / sizeof(pointX[0]);

    for (int i = 0; i < length; i++)
    {
        cout << "Введите\t" << i + 1 << " элемент " << endl;
        cout << "Точка X:\t";
        cin >> pointX[i];
        cout << "Точка Y:\t";
        cin >> pointY[i];
    }

    for (int i = 0; i < length; i++)
    {
        for (int j = i + 1; j < length - 1; j++)
        {
            distanceOfPoints = sqrt(pow(pointX[i] - pointX[j], 2) + pow(pointY[i] - pointY[j], 2));
            if (distanceOfPoints > ch)
            {
                ch = distanceOfPoints;
                indexX = i;
                indexY = j;
            }
        }

    }

    cout << "Наибольшее расстояние между точками" << endl;
    cout << "X\t" << pointX[indexX] << endl;
    cout << "Y\t" << pointY[indexY];

}
void f3()
{
    int const n = 10;

    double A[n];
    const int length = sizeof(A) / sizeof(A[0]);
    int sumResult = 0;
    int indexMin;

    for (int i = 0; i < length; i++)
    {
        cout << "Введите\t" << i + 1 << " элемент ";
        cin >> A[i];

    }

    double min = A[0];

    for (int i = 0; i < length; i++)
    {
        if (A[i] < min)
        {
            min = A[i];
            indexMin = i;
        }
    }
    cout << "Минимальный элемент:\t" << min << endl;

    for (int i = 0; i < length; i++)
    {
        sumResult += A[i];
    }
    sumResult /= length;

    A[indexMin] = sumResult;

    cout << "Среднее арифметическое минимального элемента:\t" << A[indexMin];
}
void f4()
{
    const int n = 10;

    double A[n], Ak[n];
    const int length = sizeof(A) / sizeof(A[0]);
    int counter = 0;

    for (int i = 0; i < length; i++)
    {
        cout << "Введите\t" << i + 1 << " элемент ";
        cin >> A[i];
        Ak[i] = A[i];
    }

    for (int k = 1; k < length; k++)
    {
        if (Ak[k] < (Ak[k - 1] + A[k + 1]) / 2)
        {
            counter++;
        }
    }

    cout << "Количество чисел подобающих условию (Ak-1 + Ak+1 / 2)\t" << counter << endl;
}
void f5()
{
    const int n = 12;

    double A[n], Ak[n];
    const int length = sizeof(A) / sizeof(A[0]);
    int counter = 0;

    for (int i = 0; i < length; i++)
    {
        cout << "Введите\t" << i + 1 << " элемент ";
        cin >> A[i];
        Ak[i] = A[i];
    }

    for (int k = 1; k < length; k++)
    {
        if (Ak[k] > pow(2, k))
        {
            counter++;
        }
    }

    cout << "Количество чисел подобающих условию Ak > 2^k\t" << counter << endl;
}
void f6()
{
    const int n = 12;

    int A[n];
    const int length = sizeof(A) / sizeof(A[0]);
    int counter = 0;
    double min;

    for (int i = 0; i < length; i++)
    {
        cout << "Введите\t" << i + 1 << " элемент ";
        cin >> A[i];
    }
    min = A[0];

    for (int i = 1; i < length; i++)
    {
        if (A[i] % 2 == 0)
        {
            if (A[i] < min && A[i] != 0)
            {
                min = A[i];
            }
        }
    }

    cout << "Наименьшее чётное число\t" << min << endl;
}
void f7()
{
    const int n = 12;

    int A[n];
    const int length = sizeof(A) / sizeof(A[0]);
    int counter = 0;
    double max;

    for (int i = 0; i < length; i++)
    {
        cout << "Введите\t" << i + 1 << " элемент ";
        cin >> A[i];
    }
    max = A[0];

    for (int i = 1; i < length; i++)
    {
        if (A[i] % 2 != 0)
        {
            if (A[i] > max && A[i] != 0)
            {
                max = A[i];
            }
        }

        else if (A[i] % 2 == 0)
        {
            counter++;
        }
    }

    cout << "Наибольшее нечётное число\t" << max << endl;
    cout << "Количество чётных чисел\t" << counter << endl;
}
void f8()
{
    const int n = 15;

    int A[n];
    const int length = sizeof(A) / sizeof(A[0]);
    int counter = 0;
    double max, min;
    int maxIndex = 0, minIndex = 0;

    for (int i = 0; i < length; i++)
    {
        cout << "Введите\t" << i + 1 << " элемент ";
        cin >> A[i];
    }
    max = A[0];
    min = A[0];

    for (int i = 1; i < length; i++)
    {
        if (A[i] > max)
        {
            max = A[i];
            maxIndex = i;
        }

        if (A[i] < min)
        {
            min = A[i];
            minIndex = i;
        }
    }

    cout << "Массив без изменений\n";
    for (int i = 0; i < length; i++)
    {
        cout << A[i] << "\t";
    }
    cout << endl;

    A[maxIndex] = min;
    A[minIndex] = max;

    cout << "Массив с изменёнными значениями\n";
    for (int i = 0; i < length; i++)
    {
        cout << A[i] << "\t";
    }

}
void f9()
{
    const int n = 15;

    double A[n];
    const int length = sizeof(A) / sizeof(A[0]);
    int counter = 0;
    double max, min;
    int maxIndex = 0, minIndex = 0;

    for (int i = 0; i < length; i++)
    {
        cout << "Введите\t" << i + 1 << " элемент ";
        cin >> A[i];
    }
    max = A[0];
    min = A[0];

    for (int i = 1; i < length; i++)
    {
        if (A[i] > max)
        {
            max = A[i];
            maxIndex = i;
        }

        if (A[i] < min)
        {
            min = A[i];
            minIndex = i;
        }
    }

    cout << "Массив без изменений\n";
    for (int i = 0; i < length; i++)
    {
        cout << A[i] << "\t";
    }
    cout << endl;

    A[maxIndex] = A[length - 1];
    A[minIndex] = A[0];
    A[0] = min;
    A[length - 1] = max;

    cout << "Массив с изменёнными значениями\n";
    for (int i = 0; i < length; i++)
    {
        cout << A[i] << "\t";
    }

}
void f11()
{
    const int n = 10;

    double A[n];
    const int length = sizeof(A) / sizeof(A[0]);
    double max, min;
    int maxIndex = 0, minIndex = 0;

    for (int i = 0; i < length; i++)
    {
        cout << "Введите\t" << i + 1 << " элемент ";
        cin >> A[i];
    }
    max = A[0];
    min = A[0];

    for (int i = 1; i < length; i++)
    {
        if (A[i] > max)
        {
            max = A[i];
            maxIndex = i;
        }

        if (A[i] < min)
        {
            min = A[i];
            minIndex = i;
        }
    }
    cout << "Массив без изменений\n";
    for (int i = 0; i < length; i++)
    {
        cout << A[i] << "\t";
    }
    cout << endl;

    if (A[maxIndex] == 0)
    {
        A[minIndex] = 0;
        A[maxIndex] = min;
    }
    if (A[minIndex] == 0)
    {
        A[maxIndex] = 0;
        A[minIndex] = max;
    }

    cout << "Массив с изменёнными значениями\n";
    for (int i = 0; i < length; i++)
    {
        cout << A[i] << "\t";
    }
}
void f12()
{
    const int n = 10;

    int A[n];
    const int length = sizeof(A) / sizeof(A[0]);
    double max, min;
    int maxIndex = 0, minIndex = 0;

    for (int i = 0; i < length; i++)
    {
        cout << "Введите\t" << i + 1 << " элемент ";
        cin >> A[i];
    }
    max = A[0];
    min = A[0];

    for (int i = 1; i < length; i++)
    {
        if (A[i] > max)
        {
            max = A[i];
            maxIndex = i;
        }

        if (A[i] < min)
        {
            min = A[i];
            minIndex = i;
        }
    }
    cout << "Массив без изменений\n";
    for (int i = 0; i < length; i++)
    {
        cout << A[i] << "\t";
    }
    cout << endl;

    if (A[0] == min && A[length - 1] == max)
    {
        A[maxIndex] = min;
        A[minIndex] = max;
    }

    cout << "Массив с изменёнными значениями\n";
    for (int i = 0; i < length; i++)
    {
        cout << A[i] << "\t";
    }

}