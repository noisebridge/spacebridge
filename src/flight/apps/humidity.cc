#include "src/flight/devices/bme280/bme280.hpp"
#include <iostream>

int main() {
    ::spacebridge::flight::devices::Bme280("/dev/i2c-1", 77);
    std::cout << "hello world" << '\n';
    return 0;
}