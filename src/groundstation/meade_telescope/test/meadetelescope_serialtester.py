import serial, time

serial_port_name = '/dev/cu.usbserial-B0033MRP'
try:
    with serial.Serial(serial_port_name, 9600, timeout=2) as ser:
        ser.write(b':Ms#')  # Send a command (adjust as necessary)
        print(f"Slewing south")
        time.sleep(2)
        ser.write(b':Q#')  # Stop slewing)
        time.sleep(1)

        ser.write(b':Mn#')  # Send a command (adjust as necessary)
        print(f"Slewing North")
        time.sleep(2)
        ser.write(b':Q#')  # Stop slewing)
        time.sleep(1)

        ser.write(b':Me#')  # Send a command (adjust as necessary)
        print(f"Slewing east")
        time.sleep(2)
        ser.write(b':Q#')  # Stop slewing)
        time.sleep(1)

        ser.write(b':Mw#')  # Send a command (adjust as necessary)
        print(f"Slewing west")
        time.sleep(2)
        ser.write(b':Q#')  # Stop slewing)
        time.sleep(1)


except serial.SerialException as e:
    print(f"Failed {e}")
