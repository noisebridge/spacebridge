load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# RPI HW drivers
http_archive(
   name = "rpi_hw_cc",
   strip_prefix = "Rpi-hw-0.7.3/",
   sha256 = "2a7a7127bffb2f4e50772315223d6fc9dc8f4778f68701810f7545692f0b51d3",
   build_file="@//third_party/rpi_hw:BUILD",
   url = "https://github.com/Wicker25/Rpi-hw/archive/refs/tags/v0.7.3.zip",
)

# IMU - LSM6DSV16X registers
http_archive(
    name = "lsm6dsv16x_regs_cc",
    sha256 = "1baebca7a19f0915f28234e43b5757a9ca55fab0e4fa4ff2db27a75510a38b6b",
    strip_prefix = "SparkFun_LSM6DSV16X_Arduino_Library-1.0.2/src/st_src",
    build_file="@//third_party/lsm6dsv16x:BUILD",
    url = "https://github.com/sparkfun/SparkFun_LSM6DSV16X_Arduino_Library/archive/refs/tags/v1.0.2.zip"
)

# Humidity - BME280
http_archive(
    name = "bme280_cc",
    sha256 = "be148c48a5d840b59d51a35dfd21257edff1c16966dab1e7100bab0ebc53039b",
    strip_prefix = "BME280_SensorAPI-bme280_v3.5.1",
    build_file="@//third_party/bme280:BUILD",
    url = "https://github.com/boschsensortec/BME280_SensorAPI/archive/refs/tags/bme280_v3.5.1.zip"
)