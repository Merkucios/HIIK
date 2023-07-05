//  Дан файл вещественных чисел. Заменить в файле каждый элемент, кроме начального и конечного, на его среднее арифметическое с предыдущим и последующим элементом.
#include <fstream>
#include <iostream>

using namespace std;

int main() {
    ifstream inputFile("Number.txt");
    ofstream outputFile("Num.txt");

    if (!inputFile.is_open() || !outputFile.is_open()) {
        cout << "Error opening file" << endl;
        return 1;
    }

    double prev, current, next;
    inputFile >> prev;
    outputFile << prev << endl;

    while (inputFile >> current) {
        inputFile >> next;
        outputFile << (prev + current + next) / 2 << endl;
        prev = current;
    }

    outputFile << current << endl;

    inputFile.close();
    outputFile.close();

    return 0;
}