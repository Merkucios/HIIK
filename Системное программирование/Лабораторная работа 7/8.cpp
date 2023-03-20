#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
    string str;
    getline(cin, str);

    stringstream ss(str);
    string word;
    int count = 0;

    while (ss >> word) {
        count++;
        if (count == 1) {
            continue;
        }
        char first = word[0];
        char last = word[word.length() - 1];
        word.erase(0, 1);
        word.erase(word.length() - 1, 1);
        word = last + word + first;
        cout << word << " ";
    }

    return 0;
}
