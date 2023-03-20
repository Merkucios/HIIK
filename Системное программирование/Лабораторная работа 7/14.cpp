//
#include <iostream>
#include <string>

int main() {
    std::string X, Y;
    std::cin >> X >> Y;
    int count = 0;
    for (int i = 0; i < X.length(); i++) {
        if (X[i] == Y[i]) {
            count++;
        }
    }
    std::cout << "The number of identical letters: " << count << std::endl;
    return 0;
}
