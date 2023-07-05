//  Дан файл целых чисел. Заменить в нем каждый элемент с четным номером на два нуля.
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream inputFile("Number.txt");
    ofstream outputFile("Num.txt");

    int number;
    int count = 0;

    while (inputFile >> number) {
        count++;
        if (count % 2 == 0) {
            outputFile << "0 0" << endl;
        }
        else {
            outputFile << number << endl;
        }
    }

    inputFile.close();
    outputFile.close();

    return 0;
}