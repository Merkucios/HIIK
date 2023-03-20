//  Дан файл вещественных чисел. Поменять в нем местами минимальный и максимальный элементы.
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main() {
    ifstream input_file("Numbers.txt");
    ofstream output_file("Num.txt");

    double num, min_val, max_val;
    int min_pos, max_pos;

    // read the first number in the file
    input_file >> num;

    // initialize the minimum and maximum values
    min_val = max_val = num;
    min_pos = max_pos = 0;

    // counter for the current position in the file
    int pos = 0;

    // loop through the rest of the numbers in the file
    while (input_file >> num) {
        ++pos;

        // update the minimum value and its position if necessary
        if (num < min_val) {
            min_val = num;
            min_pos = pos;
        }

        // update the maximum value and its position if necessary
        if (num > max_val) {
            max_val = num;
            max_pos = pos;
        }
    }

    // close the input file
    input_file.close();

    // open the input file again
    input_file.open("Numbers.txt");

    // counter for the current position in the file
    pos = 0;

    // loop through the numbers in the file
    while (input_file >> num) {
        // write the number to the output file
        if (pos == min_pos) {
            output_file << max_val << endl;
        }
        else if (pos == max_pos) {
            output_file << min_val << endl;
        }
        else {
            output_file << num << endl;
        }

        ++pos;
    }

    // close the input and output files
    input_file.close();
    output_file.close();

    return 0;
}