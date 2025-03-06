#!/usr/bin/env bash

set -e # exit if any command [1] has a non-zero exit status
set -u # references to undefined variables cause an error
set -o pipefail # prevent errors in a pipeline from being masked
set -x # print every command as it is executed

if ! command -v ubxtool &> /dev/null; then
  echo "Error: ubxtool not found. Please install GPSD (which provides ubxtool) from https://gpsd.io/index.html"
  exit 1
fi

# You need to know the protocol version of your u-blox receiver.
# Change this number based on the output of `ubxtool -p MON-VER | grep -F PROT`
export UBXOPTS="-P 18"

# Define the GPS device. You may need to change this depending on your system.
DEVICE=/dev/ttyACM0

# "7" means Airborne with <2g acceleration.
# Value comes from this doc: https://content.u-blox.com/sites/default/files/u-blox-M9-SPG-4.04_InterfaceDescription_UBX-21022436.pdf
UBX_CFG_NAV5_MODEL=7

# Configure the Dynamic Platform Model (UBX-CFG-NAV5) to UBX_CFG_NAV5_MODEL
ubxtool -f "$DEVICE" -p "MODEL,$UBX_CFG_NAV5_MODEL"

# By default, changes made via ubxtool are applied to the device's volatile memory and may be lost upon power cycling.
# Save the configuration to non-volatile memory: 
ubxtool -f "$DEVICE" -p SAVE

# Confirm your changes worked by printing the CFG-NAV5 config
ubxtool -f "$DEVICE" -p CFG-NAV5
