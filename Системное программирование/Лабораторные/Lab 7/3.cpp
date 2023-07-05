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
        if (word[0] == 'b' || word[0] == 'B') {
            count++;
        }
    }

    cout << "The number of words starting with the letter 'b' is: " << count << endl;

    return 0;
}
