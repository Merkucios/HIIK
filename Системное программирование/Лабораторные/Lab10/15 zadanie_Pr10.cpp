//  Дан файл целых чисел. Удалить из него все элементы с четными номерами.
/#include <iostream>
#include <fstream>
#include <vector>

int main() {
    std::ifstream input("Number.txt"); // Открытие файла для чтения
    std::ofstream output("Num.txt"); // Открытие файла для записи
    std::vector<int> numbers; // Вектор для хранения чисел из файла

    int x;
    while (input >> x) {
        numbers.push_back(x); // Чтение чисел из файла и добавление их в вектор
    }

    for (int i = 0; i < numbers.size(); i++) {
        if (i % 2 != 0) { // Если номер элемента нечетный
            output << numbers[i] << ' '; // Записываем его в выходной файл
        }
    }

    input.close(); // Закрытие файла для чтения
    output.close(); // Закрытие файла для записи

    return 0;
}