//  Дан файл целых чисел с элементами A1, A2, …, AN (N — количество элементов в файле).Заменить исходное расположение его элементов на следующее : A1, AN, A2, AN−1, A3, … .
#include <iostream>
#include <fstream>
#include <vector>

int main() {
    std::ifstream in("Number.txt");
    std::ofstream out("Num.txt");
    std::vector<int> arr;

    int n;
    in >> n;

    int x;
    while (in >> x) {
        arr.push_back(x);
    }

    for (int i = 0; i < arr.size() / 2; i++) {
        out << arr[i] << " " << arr[arr.size() - i - 1] << " ";
    }

    if (arr.size() % 2 == 1) {
        out << arr[arr.size() / 2];
    }

    in.close();
    out.close();

    return 0;
}