from absl import app
from absl import flags

from collections.abc import Sequence

from dataclasses import dataclass

import cv2 # import the opencv library 

import numpy as np

FLAGS = flags.FLAGS

# Flag names are globally defined!  So in general, we need to be
# careful to pick names that are unlikely to be used by other libraries.
# If there is a conflict, we'll get an error at import time.
flags.DEFINE_boolean('debug', False, 'Produces debugging output.')


flags.DEFINE_string('path_to_video', None, 'Path to video to load.')

flags.DEFINE_integer('camera_index', None, 'Your age in years.', lower_bound=0)
flags.DEFINE_boolean('camera_autofocus', False, 'Whether to enable camera autofocus.')
flags.DEFINE_float('camera_zoom', None, 'Zoom level.')


@dataclass
class CameraParameters:
    x: float
    y: float
    radius: float
    exposure:float = 0.5

def wait_for_and_handle_key_inputs(cam_parms: CameraParameters) -> (bool, CameraParameters):
	key_pressed = cv2.waitKey(1)
	if key_pressed == -1:
		return (True, cam_parms)
	elif key_pressed == 13: # Enter key
		return (False, cam_parms)
	elif key_pressed == ord('q'):
		quit()
	elif key_pressed == 0: # Up key
		xc = xc - 1
	elif key_pressed == 1: # Down key
		xc = xc + 1
	elif key_pressed == 2: # Left key
		yc = yc - 1
	elif key_pressed == 3: # Right key
		yc = yc + 1
	elif key_pressed == ord('p'):
		exposure_val = exposure_val + 0.05
		print('Setting exposure:', exposure_val)
		cap.set(cv2.CAP_PROP_EXPOSURE, exposure_val)
	elif key_pressed == ord('l'):
		exposure_val = exposure_val - 0.05
		print('Setting exposure:', exposure_val)
		cap.set(cv2.CAP_PROP_EXPOSURE, exposure_val)
	elif key_pressed == ord('=') or key_pressed == ord('+'): # (Unshifted) Plus Key
		radius = radius + 1
	elif key_pressed == ord('-'): # Minus Key
		radius = radius - 1
	else:
		print('key_pressed:', key_pressed)
	
	return (True, cam_parms)


def generate_telescope_mask(cap):
	# Gets a single frame for shape.
	ret, frame = cap.read() 
	if not ret:
		raise ValueError('Unable to read frame from provided image capture stream.')

	hh, ww = frame.shape[:2]

	cam_params = CameraParameters(
		x = ww//2,
		y = hh//2,
		radius = 100,
		exposure=0.5)


	while (True):
		# Reads next frame.
		ret, frame = cap.read() 
		if not ret:
			# Loops video.
			if not cap.set(cv2.CAP_PROP_POS_FRAMES, 0):
				raise ValueError('Unable to read frame from provided image capture stream.')
			continue 


		# Draw a circle to indicate inner perimeter for the tube mask.
		calib_frame = frame.copy()
		cv2.circle(calib_frame, (camera_params.x,camera_params.y), camera_params.radius, (0,255,0), 5)
		cv2.imshow("calib_frame", calib_frame)

		(should_continue, cam_params) = wait_for_and_handle_key_inputs(cam_params)
		if not should_continue:
			break

	# Build Mask
	print('camera_params:', cam_parms)
	mask = np.zeros_like(frame[:,:,0])
	mask = cv2.circle(mask, (camera_params.x,camera_params.y), camera_params.radius, 255, -1)
	cv2.imshow("mask", mask)
	cv2.waitKey(0)
		
		
	pass


def main(argv):
	if FLAGS.debug:
		print('non-flag arguments:', argv)

	cap = None
	if FLAGS.camera_index is not None:
		print("Camera Index provided!")

		# cap = cv2.VideoCapture(FLAGS.camera_index,cv2.CAP_DSHOW)
		cap = cv2.VideoCapture(FLAGS.camera_index)

		cap.set(cv2.z, 1.0)
		cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25) # manual mode

		# Sets camera properties.
		# cap.set(cv2.CAP_PROP_AUTOFOCUS, 1 if FLAGS.camera_autofocus else 0 )
		
		# if FLAGS.camera_zoom is not None:
		# 	cap.set(cv2.CAP_PROP_ZOOM,FLAGS.camera_zoom)
		if FLAGS.debug:
			print('')
	elif FLAGS.path_to_video is not None:
		print("Video provided!")
		cap = cv2.VideoCapture(FLAGS.path_to_video)
		fps = cap.get(cv2.CAP_PROP_FPS)
		print("Frame rate: ", int(fps), "FPS")
	else:
		raise Exception("Must provide `camera_index` or `path_to_video`. ")


	generate_telescope_mask(cap)

	while(True):
		# Capture the video frame 
		# by frame 
		ret, frame = cap.read() 

		if ret:
			# Display the resulting frame 
			cv2.imshow("Image", frame)
		else:
			print('no video')
			cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
			continue
		
		# the 'q' button is set as the 
		# quitting button you may use any 
		# desired button of your choice 
		if cv2.waitKey(1) & 0xFF == ord('q'): 
			break
	  
	# After the loop release the cap object 
	cap.release() 
	# Destroy all the windows 
	cv2.destroyAllWindows() 



if __name__ == '__main__':
	app.run(main)
