#include <expected>
#include "rpi-hw/driver/i2c.hpp"
#include "bme280.hpp"
namespace spacebridge {
namespace flight {
namespace devices {

Bme280::Bme280(const std::string& dev_path, int addr) : i2c_(dev_path, addr) {
};

void Bme280::Init() {};

void Bme280::IsConnected() {};

BME280_INTF_RET_TYPE Bme280::BME280_i2c_read(uint8_t reg_addr, uint8_t *reg_data, uint32_t length, void *intf_ptr) {
    return 0;
};

BME280_INTF_RET_TYPE Bme280::BME280_i2c_write(uint8_t reg_addr, const uint8_t *reg_data, uint32_t length, void *intf_ptr) {
    return 0;
};

}
}
}