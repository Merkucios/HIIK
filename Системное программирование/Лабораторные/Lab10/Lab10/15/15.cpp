//  Дан файл целых чисел. Удалить из него все элементы с четными номерами.
#include <iostream>
#include <fstream>
#include <vector>

int main() {
    std::ifstream input("Numbers.txt"); 
    std::ofstream output("Num.txt"); 
    std::vector<int> numbers; 

    int x;
    while (input >> x) {
        numbers.push_back(x); 
    }

    for (int i = 0; i < numbers.size(); i++) {
        if (i % 2 != 0) { 
            output << numbers[i] << ' '; 
        }
    }

    input.close(); 
    output.close(); 

    return 0;
}