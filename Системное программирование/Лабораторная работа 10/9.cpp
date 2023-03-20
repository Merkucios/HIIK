//  Дан файл вещественных чисел. Найти сумму его элементов с четными номерами.
#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream inputFile("Numbers.txt");
    double sum = 0.0, num;
    int counter = 0;
    while (inputFile >> num) {
        if (counter % 2 == 0) {
            sum += num;
        }
        counter++;
    }
    inputFile.close();

    cout << "Sum of elements with even numbers: " << sum << endl;
    return 0;
}