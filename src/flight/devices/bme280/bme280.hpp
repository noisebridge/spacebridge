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
    ::rpihw::driver::i2c i2c_;
};
}
}
}
