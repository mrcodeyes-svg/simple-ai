#include <iostream>
#include <any>
#include <ostream>

auto get_type(std::any input) {
    auto in = input;
    std::cout << in << std::endl;
}

auto test(std::any in){

    std::cin >> in;
    return in;
}

int main() {
    int vea = 2;
    get_type(vea);
}