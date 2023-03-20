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
    int count = 0;
    int k;
    cout << "Введите k:\t";
    cin >> k;
    cout << endl;
    int num;
    while (infile.read(reinterpret_cast<char*>(&num), sizeof(num))) {
        if (num < k) {
            count++;
        }
    }
    infile.close();

    cout << "Количество элементов меньше числа K " << k << ": " << count << endl;
    return 0;
}
