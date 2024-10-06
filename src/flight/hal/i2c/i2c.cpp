#include "i2c.hpp"

namespace spacebridge {
namespace flight {
namespace hal {
namespace i2c {

std::expected<uint32_t, I2CError> I2C::Read(std::span<uint8_t> buffer,
                                            uint8_t size) {
    if (buffer.size() < size) {
        return std::unexpected(I2CError::UNDERSIZED_BUFFER);
    }
    if (buffer.size() == 0) {
        return std::unexpected(I2CError::INVALID_SIZE);
    }

    return 0;
}

std::expected<uint32_t, I2CError> I2C::Write(std::span<uint8_t> data,
                                             uint8_t size) {
    return 0;
}

}  // namespace i2c
}  // namespace hal
}  // namespace flight
}  // namespace spacebridge