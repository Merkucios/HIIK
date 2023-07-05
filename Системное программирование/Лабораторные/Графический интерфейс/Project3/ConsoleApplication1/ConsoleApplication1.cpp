#include <iostream>
using namespace std;

int main() {
    float x = -4.0;
    float y;

    while (x <= 4.0) {
        y = -2 * x * x - 5 * x - 8;
        cout << "x = " << x << ", y = " << y << endl;
        x += 0.5;
    }

    return 0;
}
