#include <iostream>
#include <string>
#include <sstream>
#include <climits>

using namespace std;

int main() {
    string str;
    getline(cin, str);

    stringstream ss(str);
    string word;
    int minLength = INT_MAX;

    while (ss >> word) {
        if (word.length() < minLength) {
            minLength = word.length();
        }
    }

    cout << "The length of the shortest word is: " << minLength << endl;

    return 0;
}
