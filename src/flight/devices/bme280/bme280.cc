#include <expected>
#include "rpi-hw/driver/i2c.hpp"
#include "bme280.hpp"
namespace spacebridge {
namespace flight {
namespace devices {

Bme280::Bme280(const std::string& dev_path, int addr) : i2c_(dev_path, addr) {};

void Bme280::Init() {};

void Bme280::IsConnected() {};

}
}
}