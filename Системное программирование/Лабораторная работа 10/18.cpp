//  Дан файл целых чисел. Продублировать в нем все числа, принадлежащие диапазону 5 – 10.
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    ifstream input_file("Numbers.txt");
    ofstream output_file("Num.txt");
    vector<int> numbers;

    int number;
    while (input_file >> number) {
        numbers.push_back(number);
    }

    for (int i = 0; i < numbers.size(); ++i) {
        if (numbers[i] >= 5 && numbers[i] <= 10) {
            output_file << numbers[i] << endl;
            output_file << numbers[i] << endl;
        }
        else {
            output_file << numbers[i] << endl;
        }
    }

    input_file.close();
    output_file.close();

    return 0;
}