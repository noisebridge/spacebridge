import random
import requests
import time

from absl import app
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_boolean('debug', False, 'Produces debugging output.')
flags.DEFINE_boolean('dry_run', False, 'If True will not send POST requests with our data.')

flags.DEFINE_string('reciever_name',
					None,
					'Name used to identify radio reciever setup.')
flags.mark_flag_as_required('reciever_name')


flags.DEFINE_string('gps_data_endpoint',
					'http://localhost:3000/post_gps_reading',
					'Endpoint used to record GPS(+altitude) readings.')

flags.DEFINE_string('environmental_data_endpoint',
					'http://localhost:3000/post_environmental_reading',
					'Endpoint used to record Environmental Sensor readings.')

flags.DEFINE_integer('recieve_interval',
					 10,
					 'Time between transmissions (in seconds).',
					 lower_bound=0)

flags.DEFINE_float('decode_chance',
					 1.0,
					 'Chance for a given transmission to be successfully'
					 'decoded. Expressed as a ratio between [0,1].',
					 lower_bound=0.0,
					 upper_bound=1.0)

# TODO: Add simulated flight path by taking starting/end locations and interpolating between them.s

# flags.DEFINE_integer('ascent_time',
# 					 150,
# 					 'Ascent time (in minutes).',
# 					 lower_bound=0)

# flags.DEFINE_integer('descent_time',
# 					 60,
# 					 'Descent time (in minutes).',
# 					 lower_bound=0)

# Ascent Variance 
# Burst GPS/Alt

# Descent Variance
# Landing GPS/Alt

def get_gps_altitude() -> dict:
	results = {
		'latitude': 37.773998, 
		'longitude': -122.126069,
		'altitude': 12000
	}
	return results



def main(argv):
	if FLAGS.debug:
		print('non-flag arguments:', argv)
	
	reciever_name = FLAGS.reciever_name

	while (True):
		if random.random() < FLAGS.decode_chance:
			gps_results = get_gps_altitude()
			gps_results['reciever_name'] = reciever_name
			
			if FLAGS.debug:
				print(f'[{reciever_name}] Sending:', gps_results)

			if not FLAGS.dry_run:
				r = requests.post(FLAGS.gps_data_endpoint, json=gps_results)
				if FLAGS.debug:
					print(r.status)

		elif FLAGS.debug:
			print(f'[{reciever_name}] Simulating missing a possible GPS decode.')
		
		if FLAGS.debug:
			print(f'[{reciever_name}] Sleeping for {FLAGS.recieve_interval} seconds')
		time.sleep(FLAGS.recieve_interval)

if __name__ == '__main__':
	app.run(main)