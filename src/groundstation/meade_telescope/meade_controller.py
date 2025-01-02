import time

from absl import app
from absl import flags
from flask import Flask
from markdown_it import MarkdownIt

# Sets up flags used by this probram
FLAGS = flags.FLAGS
flags.DEFINE_boolean('debug', False, 'If true will produces debugging output.')
flags.DEFINE_boolean('dry_run', False, 'If True will not actually send swivel commands and will only simulate them in debug msgs.')
flags.DEFINE_boolean('threaded', False, 'Whether to run Flask app in threaded mode.')

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

# Instatiate flask app.
flask_app = Flask(__name__)

@flask_app.route("/")
def print_usage_instructions():
    return usage_markdown_html

@flask_app.route("/slew_up")
def slew_up():
    return "Slewing up!"

@flask_app.route("/slew_down")
def slew_down():
    return "Slewing down!"

@flask_app.route("/slew_left")
def slew_left():
    return "Slewing left!"

@flask_app.route("/slew_right")
def slew_right():
    return "Slewing right!"



def main(argv):
	if FLAGS.debug:
		print('non-flag arguments:', argv)

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