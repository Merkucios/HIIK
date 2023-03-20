#include <iostream>
#include <fstream>
using namespace std;

int main() {
    setlocale(LC_ALL, "Russian");
    ifstream infile("f", ios::in | ios::binary);
    if (!infile) {
        cerr << "Не могу найти файл f" << endl;
        return 1;
    }

    ofstream outfile("g", ios::out | ios::binary);
    if (!outfile) {
        cerr << "Не могу открыть файл g" << endl;
        return 1;
    }

    char buffer[1024];
    while (infile.read(buffer, sizeof(buffer))) {
        outfile.write(buffer, infile.gcount());
    }
    outfile.write(buffer, infile.gcount());

    infile.close();
    outfile.close();

    cout << "Копирование данных успешно завершено" << endl;
    return 0;
}
