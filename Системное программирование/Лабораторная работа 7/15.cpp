//
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> combinations = { "USCH", "YUSCH", "..." };
    std::string text;
    std::cin >> text;
    int count = 0;
    for (const auto& combination : combinations) {
        size_t pos = text.find(combination);
        while (pos != std::string::npos) {
            count++;
            pos = text.find(combination, pos + 1);
        }
    }
    std::cout << "The number of specific combinations of letters: " << count << std::endl;
    return 0;
}
