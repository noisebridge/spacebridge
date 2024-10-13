cc_library(
    name="rpi_hw",
    visibility = ["//visibility:public"],
    defines = [
        "RPI_HW_VERSION_MAJOR=0",
        "RPI_HW_VERSION_MINOR=7",
        "RPI_HW_VERSION_PATCH=3",
        "RPI_HW_VERSION=0.7.3",
        "USE_MAGICK=0",
        "USE_FREETYPE=0",
    ],
    copts=[
        "-Wall",
        "-ansi",
        "-pedantic",
        "-pedantic-errors",
        "-O2",
        "-std=c++11",
        "-Wno-long-long",
    ],
    strip_include_prefix="include",
    hdrs=glob(["include/**/*.hpp",], ["include/display/*.hpp", "include/iface/*.hpp"]),
    srcs=glob(["src/**/*.cpp",], ["src/iface/*.cpp",]),
    deps=[
        "//:rpi-header",
        "//:rpi-config-header",
    ]
)

cc_library(
    name = "rpi-header",
    hdrs = ["rpi.hpp"],
    include_prefix = "rpi-hw",
)

cc_library(
    name = "rpi-config-header",
    hdrs = ["config.hpp"],
    include_prefix ="rpi-hw",
)

genrule(
    name = "rpi-header-gen",
    outs = ["rpi.hpp"],
    cmd = "touch $@",
)

genrule(
    name = "rpi-config-header-gen",
    outs = ["config.hpp"],
    cmd = "touch $@",
)