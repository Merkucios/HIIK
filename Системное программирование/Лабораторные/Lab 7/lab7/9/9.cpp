#include <iostream>
#include <string>
#include <sstream>
#include <unordered_set>

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

        unordered_set<char> seen;
        string result = "";

        for (int i = 0; i < word.length(); i++) {
            if (seen.count(word[i]) == 0) {
                result += word[i];
                seen.insert(word[i]);
            }
        }

        if (result.length() % 2 == 1) {
            result.erase(result.length() / 2, 1);
        }

        cout << result << " ";
    }

    return 0;
}
