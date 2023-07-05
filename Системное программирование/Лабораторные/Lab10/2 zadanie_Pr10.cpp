//  Дано имя файла и вещественные числа A и D. Создать файл вещественных чисел с данным именем и записать в него 10 первых членов арифметической прогрессии
//  с начальным членом A и разностью D : A, A + D, A + 2·D, A + 3·D, …
#include <iostream>
#include <fstream>

using namespace std;

int main() {
    string filename;
    float A, D;

    cout << "Enter the name of the file: ";
    cin >> filename;
    cout << "Enter A: ";
    cin >> A;
    cout << "Enter D: ";
    cin >> D;

    ofstream file(filename, ios::out);
    if (!file) {
        cout << "Cannot open file" << endl;
        return 1;
    }

    for (int i = 0; i < 10; i++) {
        file << A + i * D << endl;
    }

    file.close();
    cout << "Data written to file " << filename << endl;
    return 0;
}