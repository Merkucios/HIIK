//  Дан файл вещественных чисел. Создать два новых файла, первый из которых содержит элементы исходного файла с нечетными номерами(1, 3, …), а второй — с четными(2, 4, …).
#include <iostream>
#include <fstream>

using namespace std;

int main() {
    string inputFileName, oddFileName, evenFileName;
    cout << "Enter the name of the input file: ";
    cin >> inputFileName;
    cout << "Enter the name of the first output file (for odd numbers): ";
    cin >> oddFileName;
    cout << "Enter the name of the second output file (for even numbers): ";
    cin >> evenFileName;

    ifstream inputFile(inputFileName);
    if (!inputFile) {
        cout << "Error opening input file" << endl;
        return 1;
    }
    ofstream oddFile(oddFileName);
    ofstream evenFile(evenFileName);

    int count = 0;
    double number;
    while (inputFile >> number) {
        if (count % 2 == 0) {
            evenFile << number << endl;
        }
        else {
            oddFile << number << endl;
        }
        count++;
    }

    inputFile.close();
    oddFile.close();
    evenFile.close();

    cout << "Finished splitting the input file into two files" << endl;
    return 0;
}