//
#include <iostream>
#include <string>
#include <map>

using namespace std;

string intToRoman(int num) {
    map<int, string> values = {
        {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
        {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"},
        {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}
    };
    string result;
    for (auto i = values.rbegin(); i != values.rend(); i++) {
        while (num >= i->first) {
            result += i->second;
            num -= i->first;
        }
    }
    return result;
}

int main() {
    int num;
    cin >> num;

    cout << intToRoman(num) << endl;

    return 0;
}
