//11.	Составить программу для вычеркивания из слов текста всех букв, стоящих на нечетных местах после буквы "а".
#include <iostream>
#include <string>
#include <sstream>

using namespace std;
void crossOutLetters(string& word);

void crossOutLetters(string& word) {
    bool foundA = false;
    for (int i = 0; i < word.length(); i++) {
        if (foundA && i % 2 == 1) {
            word[i] = '-';
        }
        if (word[i] == 'a' || word[i] == 'A') {
            foundA = true;
        }
    }
}

int main() {
    string str;
    getline(cin, str);

    stringstream ss(str);
    string word;

    while (ss >> word) {
        crossOutLetters(word);
        cout << word << " ";
    }

    return 0;
}
