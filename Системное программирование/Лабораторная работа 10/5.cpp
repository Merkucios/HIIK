//  Дан файл целых чисел. Создать новый файл, содержащий те же элементы, что и исходный файл, но в обратном порядке.
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    string in_file_name, out_file_name;
    cout << "Enter the name of the input file: ";
    cin >> in_file_name;
    cout << "Enter the name of the output file: ";
    cin >> out_file_name;

    ifstream in_file(in_file_name);
    ofstream out_file(out_file_name);

    if (!in_file.is_open()) {
        cout << "Error opening input file." << endl;
        return 1;
    }

    vector<int> numbers;
    int number;
    while (in_file >> number) {
        numbers.push_back(number);
    }

    if (!out_file.is_open()) {
        cout << "Error opening output file." << endl;
        return 1;
    }

    for (int i = numbers.size() - 1; i >= 0; i--) {
        out_file << numbers[i] << endl;
    }

    in_file.close();
    out_file.close();

    return 0;
}