import serial
import time

from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
from queue import PriorityQueue
from threading import Thread
from typing import Any


class MeadeCommand(Enum):
	SLEW_STOP = 0
	SLEW_UP = 1
	SLEW_DOWN = 2
	SLEW_LEFT = 3
	SLEW_RIGHT = 4


def send_meade_command(
		serial_device:serial.Serial,
		command:MeadeCommand) -> None:
	match command:
		case MeadeCommand.SLEW_STOP:
			serial_device.write(b':Q#')
		case MeadeCommand.SLEW_UP:
			serial_device.write(b':Mn#')
		case MeadeCommand.SLEW_DOWN:
			serial_device.write(b':Ms#')
		case MeadeCommand.SLEW_LEFT:
			serial_device.write(b':Mw#')
		case MeadeCommand.SLEW_RIGHT:
			serial_device.write(b':Me#')
		# If an exact match is not confirmed, this last case will be used if provided
		case _:
			raise TypeError("Invalid command received") 

	pass

@dataclass(order=True)
class MeadeTelescopeCommand:
	sort_index:float = field(compare=False, init=False)
	priority:int = field(compare=False, default=0)
	issued_time:datetime = field(compare=False, default=datetime.now())
	command:MeadeCommand = field(compare=False,default=MeadeCommand.SLEW_STOP)

	def __post_init__(self) -> None:
		# Sort order precedence:
		#  * highest priority
		#  * most recent 
		self.sort_index = - self.priority * 10e10 - self.issued_time.timestamp()

	

class MeadeTelescope():
	serial_port_path: str
	serial_device: serial.Serial
	slew_duration:float = 5 #0.25
	debug:bool = False
	dry_run:bool = False

	command_queue:PriorityQueue = PriorityQueue()
	command_processing_thread:Thread

	def __init__(self,
			  serial_port_path:str,
			  slew_duration:float = None,
			  debug:bool=None,
			  dry_run:bool =None) -> None:
		self.serial_port_path = serial_port_path
		if slew_duration:
			self.slew_duration = slew_duration
		if debug:
			self.debug = debug
		if dry_run:
			self.dry_run = dry_run

		# Open serial device controlling meade telescope
		if not self.dry_run:
			self.serial_device = serial.Serial(serial_port_path, 9600, timeout=2)

		self.command_processing_thread = Thread(target=self.process_loop, args=[])
		self.command_processing_thread.start()

	def __del__(self):
		print("MeadeTelescope destructor called - stopping worker thread...")
		if self.command_processing_thread:
			self.command_processing_thread.stop()

	def queue_command(self,
				  priority:float,
				  command:MeadeCommand) -> None:
		if self.debug:
			print(f'Adding {command} at {priority} piority.')
		self.command_queue.put(MeadeTelescopeCommand(priority=priority,command=command))

	def process_loop(self) -> None:
		while True:
			print('process_loop()')
			if self.command_queue.empty():
				if self.debug:
					print('No commands to process.')
			else:
				command_info = self.command_queue.get()
				command = command_info.command
				if self.debug:
					print("processing command: ", command_info)
				if not self.dry_run:
					send_meade_command(self.serial_device, command)

			time.sleep(self.slew_duration)
			


# def main():
# 	pq = PriorityQueue()
# 	pq.put(MeadeTelescopeCommand(issued_time=datetime.now(),command=MeadeCommand.SLEW_DOWN))
# 	pq.put(MeadeTelescopeCommand(priority=1, issued_time=datetime.now(),command=MeadeCommand.SLEW_UP))
# 	pq.put(MeadeTelescopeCommand(issued_time=datetime.now(),command=MeadeCommand.SLEW_LEFT))
# 	# for item in pq.queue:
# 	# 	print(item)

# 	# sorted_list = [] 
# 	while pq.empty()  == False:
# 		item = pq.get()
# 		print(item)
# 		# sorted_list.append(pq.get())

# 	telescope = MeadeTelescope(
# 		serial_port_path='/dev/...',
# 		debug=True,
# 		dry_run=True)
	
# 	telescope.queue_command(0, MeadeCommand.SLEW_RIGHT)
# 	telescope.queue_command(0, MeadeCommand.SLEW_LEFT)
# 	telescope.queue_command(1, MeadeCommand.SLEW_STOP)
# 	telescope.queue_command(0, MeadeCommand.SLEW_UP)
# 	telescope.queue_command(0, MeadeCommand.SLEW_UP)
# 	telescope.queue_command(0, MeadeCommand.SLEW_UP)
# 	telescope.queue_command(0, MeadeCommand.SLEW_UP)
# 	telescope.queue_command(0, MeadeCommand.SLEW_UP)
# 	telescope.queue_command(0, MeadeCommand.SLEW_UP)
# 	telescope.queue_command(0, MeadeCommand.SLEW_UP)
# 	telescope.queue_command(0, MeadeCommand.SLEW_DOWN)



# 	input("Press Enter to continue...")
# 	del telescope
	

# if __name__ == '__main__':
# 	main()