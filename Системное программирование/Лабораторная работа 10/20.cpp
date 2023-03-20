//  Дан файл целых чисел. Заменить в нем каждое положительное число на три нуля.
#include <fstream>
#include <iostream>

int main() {
    std::ifstream inputFile("Numbers.txt");
    std::ofstream outputFile("Num.txt");

    int number;
    while (inputFile >> number) {
        if (number > 0) {
            outputFile << "0 0 0 ";
        }
        else {
            outputFile << number << " ";
        }
    }

    inputFile.close();
    outputFile.close();

    return 0;
}