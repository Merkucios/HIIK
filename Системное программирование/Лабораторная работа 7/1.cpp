#include <iostream>
#include <sstream>

int main() {
    std::string text = "My own text Medvedev";
    std::istringstream iss(text);
    std::string word;
    int word_count = 0;

    while (iss >> word) {
        ++word_count;
    }

    std::cout << "The number of words in the text is: " << word_count << std::endl;

    return 0;
}


