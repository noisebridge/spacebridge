import serial, time
serial_port_name = '/dev/tty.usbserial-B0033MRP'


def slew_direction(direction :bytes) -> None:
	try:
		with serial.Serial(serial_port_name, 9600, timeout=2) as ser:
			 ser.write(b':M'+direction+b'#')  # Send a command (adjust as necessary)
			 print(f"Slewing")
			 time.sleep(1)
			 ser.write(b':Q#')  # Stop slewing)
	except serial.SerialException as e:
		print(f"Failed {e}")

def slew_north():
	slew_direction(b'n')

def slew_south():
	slew_direction(b's')

def slew_east():
	slew_direction(b'e')

def slew_west():
	slew_direction(b'w')


def slew_test() -> None:
	try:
		with serial.Serial(serial_port_name, 9600, timeout=2) as ser:
			 ser.write(b':Ms#')  # Send a command (adjust as necessary)
			 print(f"Slewing")
			 time.sleep(1)
			 ser.write(b':Q#')  # Stop slewing)
	except serial.SerialException as e:
		print(f"Failed {e}")


slew_test()