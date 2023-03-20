#include <iostream>
#include <fstream>
using namespace std;

int main() {
    setlocale(LC_ALL, "Russian");
    ofstream file("f", ios::out | ios::binary);
    for (int i = 1; i <= 100; i++) {
        file.write(reinterpret_cast<const char*>(&i), sizeof(i));
    }
    file.close();

    
    int k;
    cout << "Введите к:\t";
    cin >> k;
    ifstream infile("f", ios::in | ios::binary);
    infile.seekg((k - 1) * sizeof(int));
    int num;
    infile.read(reinterpret_cast<char*>(&num), sizeof(num));
    infile.close();

    
    cout << "Это " << k << " -ый элемент равен " << num << endl;
    return 0;
}
