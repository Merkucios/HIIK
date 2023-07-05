//  Дан файл целых чисел. Удвоить его размер, записав в конец файла все его исходные элементы(в том же порядке).
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
    vector<int> numbers;
    int x;

    ifstream inputFile("Numbers.txt");
    if (!inputFile)
    {
        cout << "File not found" << endl;
        return 1;
    }


    while (inputFile >> x)
    {
        numbers.push_back(x);
    }

    inputFile.close();


    ofstream outputFile("Num.txt", ios::app);
    for (int i = 0; i < numbers.size(); i++)
    {
        outputFile << numbers[i] << endl;
    }

    outputFile.close();

    return 0;
}