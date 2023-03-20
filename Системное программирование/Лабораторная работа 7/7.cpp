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
        for (int i = 0; i < word.length(); i++) {
            if (word[i] == 'a' && i % 2 == 0) {
                word[i] = 'e';
            }
            else if (word[i] == 'b' && i % 2 != 0) {
                word.replace(i, 1, "ak");
                i += 1;
            }
        }
        cout << word << " ";
    }

    return 0;
}
