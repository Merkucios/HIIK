// Дан файл целых чисел. Продублировать в нем все элементы с нечетными номерами.
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    vector<int> numbers;
    int x;

    
    ifstream input("Numbers.txt");
    if (!input.is_open()) {
        cerr << "Error: Unable to open the file." << endl;
        return 1;
    }

    
    while (input >> x) {
        numbers.push_back(x);
    }
    input.close();

    
    ofstream output("Num.txt");
    if (!output.is_open()) {
        cerr << "Error: Unable to open the file." << endl;
        return 1;
    }

    
    for (int i = 0; i < numbers.size(); ++i) {
        output << numbers[i] << endl;
        if (i % 2 != 0) {
            output << numbers[i] << endl;
        }
    }
    output.close();

    return 0;
}