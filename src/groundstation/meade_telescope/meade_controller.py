from meade_telescope_lib import MeadeTelescope, MeadeCommand
import serial
import time

from absl import app
from absl import flags
from flask import Flask
from markdown_it import MarkdownIt
from queue import Queue
from enum import Enum



# Sets up flags used by this probram
FLAGS = flags.FLAGS
flags.DEFINE_boolean('debug', False, 'If true will produces debugging output.')
flags.DEFINE_boolean('dry_run', False, 'If True will not actually send swivel commands and will only simulate them in debug msgs.')
flags.DEFINE_boolean('threaded', False, 'Whether to run Flask app in threaded mode.')

flags.DEFINE_string('serial_port_path',
					'/dev/tty.usbserial-B0033MRP',
					'Path to serial port for MEADE telescope'
					' (i.e. /dev/<usb serial device connected to telescope>).')

flags.DEFINE_string('host',
					'127.0.0.1',
					'The hostname to listen on.')

flags.DEFINE_integer('port',
					50001,
					'Port to listen on.',
					lower_bound=0,
					upper_bound=65535)

flags.DEFINE_float('slew_duration',
					1.0,
					'Duration in seconds to slew for after recieving an instruction.',
					lower_bound=0.0)

# Setup how we want to parse Markdown
md = (
	MarkdownIt('commonmark', {'breaks':True,'html':True})
	.enable('table')
)

# Loads usage instruction.
usage_markdown_html = None
with open("README.md", "r") as file:
	usage_markdown_html = md.render(file.read())

meade_rotator = None

# Instatiate flask app.
flask_app = Flask(__name__)

@flask_app.route("/")
def print_usage_instructions():
	return usage_markdown_html

@flask_app.route("/slew_up")
def slew_up():
	global meade_rotator
	meade_rotator.queue_command(0, MeadeCommand.SLEW_UP)
	return "Added SLEW_UP command to queue!"

@flask_app.route("/slew_down")
def slew_down():
	global meade_rotator
	meade_rotator.queue_command(0, MeadeCommand.SLEW_DOWN)
	return "Slewing down!"

@flask_app.route("/slew_left")
def slew_left():
	global meade_rotator
	meade_rotator.queue_command(0, MeadeCommand.SLEW_LEFT)
	return "Slewing left!"

@flask_app.route("/slew_right")
def slew_right():
	global meade_rotator
	meade_rotator.queue_command(0, MeadeCommand.SLEW_RIGHT)
	return "Slewing right!"

def main(argv):
	global meade_rotator
	if FLAGS.debug:
		print('non-flag arguments:', argv)

	# Setup Meade Controller
	meade_rotator = MeadeTelescope(
			serial_port_path = FLAGS.serial_port_path,
			slew_duration = FLAGS.slew_duration,
			debug = FLAGS.debug,
			dry_run = FLAGS.dry_run)

	flask_app.run(
		host=FLAGS.host,
		port=FLAGS.port,
		debug=FLAGS.debug,
		threaded=FLAGS.threaded,
		load_dotenv=True,
		# ... **options
		)

if __name__ == '__main__':
	app.run(main)