// Дан файл целых чисел. Продублировать в нем все элементы с нечетными номерами.
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    vector<int> numbers;
    int x;

    // Открытие файла для чтения
    ifstream input("Number.txt");
    if (!input.is_open()) {
        cerr << "Error: Unable to open the file." << endl;
        return 1;
    }

    // Чтение чисел из файла в вектор
    while (input >> x) {
        numbers.push_back(x);
    }
    input.close();

    // Открытие файла для записи
    ofstream output("Num.txt");
    if (!output.is_open()) {
        cerr << "Error: Unable to open the file." << endl;
        return 1;
    }

    // Запись продублированных элементов с нечетными номерами
    for (int i = 0; i < numbers.size(); ++i) {
        output << numbers[i] << endl;
        if (i % 2 != 0) {
            output << numbers[i] << endl;
        }
    }
    output.close();

    return 0;
}