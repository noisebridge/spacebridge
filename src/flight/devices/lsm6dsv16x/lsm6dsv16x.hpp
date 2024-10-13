#include <expected>

#include "lsm6dsv16x_reg.h"
#include "rpi-hw/driver/i2c.hpp"

namespace spacebridge {
namespace flight {
namespace devices {
class Lsm6dsv16x {
   public:
    Lsm6dsv16x(const std::string& dev_path, int addr);

    void Init();

    void IsConnected();

   private:
    ::rpihw::driver::i2c i2c_;
};
}  // namespace devices
}  // namespace flight
}  // namespace spacebridge
