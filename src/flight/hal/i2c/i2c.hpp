#include <array>
#include <cinttypes>
#include <string>
#include <string_view>

namespace spacebridge {
namespace flight {
namespace hal {
namespace i2c {
class I2C {
   public:
    [[nodiscard]] explicit I2C(const std::string &dev_path, uint8_t)
        : dev_path_(dev_path) {}

   private:
    static constexpr size_t kI2cDataBufferSize = 3;
    const std::string dev_path_;
    std::array<uint8_t, kI2cDataBufferSize> buffer_;
    int fd_;
};

}  // namespace i2c
}  // namespace hal
}  // namespace flight
}  // namespace spacebridge