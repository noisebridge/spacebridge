load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# RPI HW drivers
http_archive(
   name = "rpi_hw_cc",
   strip_prefix = "Rpi-hw-0.7.3/",
   sha256 = "2a7a7127bffb2f4e50772315223d6fc9dc8f4778f68701810f7545692f0b51d3",
   build_file="@//third_party/rpi_hw:BUILD",
   url = "https://github.com/Wicker25/Rpi-hw/archive/refs/tags/v0.7.3.zip",
)

# LSM6DSV16X registers
http_archive(
    name = "lsm6dsv16x_regs_cc",
    sha256 = "1baebca7a19f0915f28234e43b5757a9ca55fab0e4fa4ff2db27a75510a38b6b",
    strip_prefix = "SparkFun_LSM6DSV16X_Arduino_Library-1.0.2/src/st_src",
    build_file="@//third_party/lsm6dsv16x:BUILD",
    url = "https://github.com/sparkfun/SparkFun_LSM6DSV16X_Arduino_Library/archive/refs/tags/v1.0.2.zip"
)