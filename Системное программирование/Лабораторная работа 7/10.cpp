#include <iostream>
#include <string>
#include <sstream>
#include <map>

using namespace std;

int main() {
    string str;
    getline(cin, str);

    stringstream ss(str);
    string word;
    map<string, int> table;

    while (ss >> word) {
        if (word[0] == 'A' || word[0] == 'a') {
            table[word]++;
        }
    }

    for (auto entry : table) {
        cout << entry.first << " " << entry.second << endl;
    }

    return 0;
}
