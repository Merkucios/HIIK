#include <iostream>
using namespace std;

void printDecimal(int n) {
    if (n < 10) {
        cout << n;
    }
    else {
        printDecimal(n / 10);
        cout << n % 10;
    }
}

int main() {
    int n;
    cout << "Enter a positive integer: ";
    cin >> n;
    cout << "Decimal representation of " << n << ": ";
    printDecimal(n);
    return 0;
}
