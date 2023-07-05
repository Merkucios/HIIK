//  Дан файл вещественных чисел. Найти его первый локальный минимум (локальным минимумом называется элемент, который меньше своих соседей).
#include <fstream>
#include <iostream>

int main() {
    std::ifstream input_file("Numbers.txt");
    double prev, curr, next;
    if (input_file >> prev) {
        while (input_file >> curr) {
            if (input_file >> next) {
                if (prev > curr&& curr < next) {
                    std::cout << "The first local minimum is " << curr << std::endl;
                    return 0;
                }
                prev = curr;
            }
            else {
                break;
            }
        }
        std::cout << "No local minimum found." << std::endl;
    }
    else {
        std::cout << "Input file is empty." << std::endl;
    }
    return 0;
}