#include "rpi-hw/driver/i2c.hpp"
#include "bme280.h"

namespace spacebridge {
namespace flight {
namespace devices {
class Bme280 {
   public:
    Bme280(const std::string& dev_path, int addr);

    void Init();

    void IsConnected();

   private:
    BME280_INTF_RET_TYPE BME280_i2c_read(uint8_t reg_addr, uint8_t *reg_data, uint32_t length, void *intf_ptr);
    BME280_INTF_RET_TYPE BME280_i2c_write(uint8_t reg_addr, const uint8_t *reg_data, uint32_t length, void *intf_ptr);

    struct bme280_dev dev_ {
        .intf = BME280_I2C_INTF,
    };

    ::rpihw::driver::i2c i2c_;
};
}
}
}
