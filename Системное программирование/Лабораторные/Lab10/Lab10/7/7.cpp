//  Дан файл целых чисел. Создать два новых файла, первый из которых содержит положительные числа из исходного файла(в обратном порядке), а второй — отрицательные(также в обратном порядке)
//  Если положительные или отрицательные числа в исходном файле отсутствуют, то соответствующий результирующий файл оставить пустым.
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    string fileName;
    cout << "Enter the name of the file: ";
    cin >> fileName;

    ifstream in(fileName);
    if (!in.is_open()) {
        cout << "-1" << endl;
        return 0;
    }

    vector<int> positiveNumbers, negativeNumbers;
    int number;
    while (in >> number) {
        if (number > 0) {
            positiveNumbers.push_back(number);
        }
        else if (number < 0) {
            negativeNumbers.push_back(number);
        }
    }
    in.close();

    ofstream outPositive(fileName + "_positive.txt");
    if (!positiveNumbers.empty()) {
        for (int i = positiveNumbers.size() - 1; i >= 0; i--) {
            outPositive << positiveNumbers[i] << endl;
        }
    }
    outPositive.close();

    ofstream outNegative(fileName + "_negative.txt");
    if (!negativeNumbers.empty()) {
        for (int i = negativeNumbers.size() - 1; i >= 0; i--) {
            outNegative << negativeNumbers[i] << endl;
        }
    }
    outNegative.close();

    return 0;
}