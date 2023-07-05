//  Дано имя файла и целое число N (> 1). Создать файл целых чисел с данным именем и записать в него N первых положительных четных чисел(2, 4, …).
#include <iostream>
#include <fstream>

using namespace std;

int main() {
    int n;
    string filename;
    cout << "Enter the name of the file: ";
    cin >> filename;
    cout << "Enter a positive integer N: ";
    cin >> n;

    ofstream file;
    file.open(filename);

    for (int i = 2; i <= 2 * n; i += 2) {
        file << i << endl;
    }

    file.close();

    cout << "The first " << n << " positive even numbers have been written to the file '" << filename << "'." << endl;
    return 0;
}