#include "lsm6dsv16x.hpp"

namespace spacebridge {
namespace flight {
namespace devices {

Lsm6dsv16x::Lsm6dsv16x(const std::string& dev_path, int addr) : i2c_(dev_path, addr) {};

void Lsm6dsv16x::Init() {};

void Lsm6dsv16x::IsConnected() {};

}
}
}