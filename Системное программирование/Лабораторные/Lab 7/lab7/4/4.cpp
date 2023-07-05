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
        if (word[0] == word[word.length() - 1]) {
            count++;
        }
    }

    cout << "The number of words in which the first and last characters are the same is: " << count << endl;

    return 0;
}
