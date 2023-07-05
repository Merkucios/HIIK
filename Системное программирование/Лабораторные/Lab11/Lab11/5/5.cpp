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
    int product = 1;
    int num;
    while (infile.read(reinterpret_cast<char*>(&num), sizeof(num))) {
        product *= num;
    }
    infile.close();

    cout << "Произведение чисел в файле равно: " << product << endl;
    return 0;
}
