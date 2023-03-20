// Дано целое число K и файл, содержащий неотрицательные целые числа. Вывести K - й элемент файла.Если такой элемент отсутствует, то вывести −1.
#include <iostream>
#include <fstream>

using namespace std;

int main() {
    int k, num, cnt = 0;

    cout << "Enter the value of k: ";
    cin >> k;

    string fileName;
    cout << "Enter the name of the file: ";
    cin >> fileName;

    ifstream inFile(fileName);
    if (!inFile.is_open()) {
        cout << -1 << endl;
        return 0;
    }

    while (inFile >> num) {
        cnt++;
        if (cnt == k) {
            cout << num << endl;
            return 0;
        }
    }

    cout << -1 << endl;
    return 0;
}