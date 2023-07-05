    //
    #include <iostream>
    #include <string>

    int main() {
        std::string text;
        std::cin >> text;
        int count = 0;
        for (size_t i = 0; i < text.length(); i++) {
            if (text[i] == ' ') {
                continue;
            }
            if (text[i] == 'a' || text[i] == 'e' || text[i] == 'i' || text[i] == 'o' || text[i] == 'u' || text[i] == 'A' || text[i] == 'E' || text[i] == 'I' || text[i] == 'O' || text[i] == 'U') {
                count++;
            }
            while (i < text.length() && text[i] != ' ') {
                i++;
            }
        }
        std::cout << "The number of words starting with a vowel: " << count << std::endl;
        return 0;
    }
