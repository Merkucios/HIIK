#include <iostream>
#include <fstream>
using namespace std;

void reversePrint(ifstream& infile) {
    int num;
    infile >> num;
    if (num != 0) {
        reversePrint(infile);
        cout << num << " ";
    }
}

int main() {
    ifstream infile("input.txt");
    reversePrint(infile);
    return 0;
}
