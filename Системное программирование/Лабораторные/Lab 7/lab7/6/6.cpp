#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
    string str;
    getline(cin, str);

    stringstream ss(str);
    string word;

    while (ss >> word) {
        int length = word.length();
        char first = word[length - 1];
        for (int i = length - 1; i > 0; i--) {
            word[i] = word[i - 1];
        }
        word[0] = first;
        cout << word << " ";
    }

    return 0;
}
