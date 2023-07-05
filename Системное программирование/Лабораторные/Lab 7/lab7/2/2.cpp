#include <iostream>
#include <string>

using namespace std;

int main() {
    string str;
    getline(cin, str);

    int count = 0;
    int len = str.length();

    
    for (int i = len - 1; i >= 0; i--) {
        if (str[i] == ' ') {
            
            break;
        }
        else if (str[i] == 'a') {
            
            count++;
        }
    }

    cout << "The number of letters 'a' in the last word is: " << count << endl;

    return 0;
}
