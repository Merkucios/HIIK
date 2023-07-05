//  Дан файл целых чисел, содержащий более 5 элементов. Уменьшить его размер до 5 элементов, удалив из файла необходимое количество конечных элементов.
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int num, count = 0;
    int arr[100];
    ifstream fin;
    fin.open("Number.txt");
    while (fin >> num) {
        arr[count] = num;
        count++;
    }
    fin.close();
    ofstream fout;
    fout.open("Num.txt");
    int n = count > 5 ? 5 : count;
    for (int i = 0; i < n; i++) {
        fout << arr[i] << endl;
    }
    fout.close();
    return 0;
}