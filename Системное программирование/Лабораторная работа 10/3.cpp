//  Дано имя файла целых чисел. Найти количество элементов, содержащихся в данном файле.Если файла с таким именем не существует, то вывести −1.
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    int kont = 0;
    int x;
    string filename;
    cout << "Enter the name of the file: ";
    cin >> filename;
    ifstream fin(filename);
    if (!fin) {
        cout << -1;
        return 0;
    }
    while (fin >> x) {
        kont++;
    }
    cout << "Number of elements in the file: " << kont << endl;
    fin.close();
    return 0;
}