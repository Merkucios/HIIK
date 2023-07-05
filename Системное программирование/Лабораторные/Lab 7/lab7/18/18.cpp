//18.	Записать программу, выясняющую, можно ли из букв слова X составить слово Y.
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool canForm(string x, string y) {
    sort(x.begin(), x.end()); // sort the letters in x
    sort(y.begin(), y.end()); // sort the letters in y

    return x == y; // check if the sorted strings are equal
}

int main() {
    string x, y;
    cin >> x >> y;

    if (canForm(x, y)) {
        cout << "Yes, the letters of word X can form word Y." << endl;
    }
    else {
        cout << "No, the letters of word X cannot form word Y." << endl;
    }

    return 0;
}
