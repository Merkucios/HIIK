#include <iostream>
#include <string>

using namespace std;

int main() {
    string text;
    getline(cin, text); // Reads the entire line of text from the keyboard

    int maxLength = 0;
    int currentLength = 0;

    for (int i = 0; i < text.length(); i++) {
        char c = text[i];

        if (!isalpha(c)) {
            currentLength++;

            if (currentLength > maxLength) {
                maxLength = currentLength;
            }
        }
        else {
            currentLength = 0;
        }
    }

    cout << "The length of the maximum series of characters other than Latin letters is: " << maxLength << endl;

    return 0;
}
