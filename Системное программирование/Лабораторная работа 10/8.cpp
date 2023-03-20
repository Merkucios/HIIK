//  Дан файл вещественных чисел. Найти среднее арифметическое его элементов.
#include <fstream>
#include <iostream>

using namespace std;

int main() {
    double sum = 0, number, count = 0;
    ifstream inFile("Numbers.txt"); // открытие файла для чтения
    if (!inFile) { // проверка на успешное открытие файла
        cout << "Could not open the file" << endl;
        return 1;
    }
    while (inFile >> number) { // чтение всех чисел из файла
        sum += number;
        count++;
    }
    inFile.close(); // закрытие файла
    if (count == 0) { // проверка на пустой файл
        cout << "The file is empty" << endl;
        return 1;
    }
    cout << "Arithmetic mean of the elements: " << sum / count << endl;
    return 0;
}