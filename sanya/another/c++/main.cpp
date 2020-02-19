#include <iostream>

int main() {
    int f1 = 0;
    int f2 = 1;
    int i = 1;
    int n = 6;
    while (i < n) {
        std::cout << f1 << f2 << std::endl;
        f2 = f2 + f1;
        f1 = f2 - f1;
        i++;
    }
    std::cout << f2 << std::endl;
    return 0;
}
