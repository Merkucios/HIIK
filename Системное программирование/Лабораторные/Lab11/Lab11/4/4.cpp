#include <iostream>
#include <fstream>
using namespace std;

const int ARRAY_SIZE = 10;

int main() {
    setlocale(LC_ALL, "Russian");
    int numbers[ARRAY_SIZE] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

    ofstream outfile("numbers", ios::out | ios::binary);
    outfile.write(reinterpret_cast<const char*>(&numbers), sizeof(numbers));
    outfile.close();

    ifstream infile("numbers", ios::in | ios::binary);
    int sum = 0;
    int num;
    while (infile.read(reinterpret_cast<char*>(&num), sizeof(num))) {
        sum += num;
    }
    infile.close();

    cout << "Сумма элементов файла равна: " << sum << endl;
    return 0;
}
