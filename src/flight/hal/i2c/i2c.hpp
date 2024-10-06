#include <array>
#include <cinttypes>
#include <expected>
#include <span>
#include <string>
#include <string_view>

namespace spacebridge {
namespace flight {
namespace hal {
namespace i2c {
enum class I2CError { UNDERSIZED_BUFFER, INVALID_SIZE, IO_ERROR };

class I2C {
   public:
    [[nodiscard]] explicit I2C(const std::string_view &dev_path, uint8_t addr)
        : dev_path_(dev_path), addr_(addr) {};

    // Returns the number of bytes read
    std::expected<uint32_t, I2CError> Read(std::span<uint8_t> buffer,
                                           uint8_t num_bytes);

    // Returns the number of bytes written
    std::expected<uint32_t, I2CError> Write(std::span<uint8_t> data,
                                            uint8_t num_bytes);

   private:
    static constexpr size_t kI2cDataBufferSize = 3;
    const std::string dev_path_;
    const uint8_t addr_;
    std::array<uint8_t, kI2cDataBufferSize> cmd_buffer_;
    int fd_;
};

}  // namespace i2c
}  // namespace hal
}  // namespace flight
}  // namespace spacebridge