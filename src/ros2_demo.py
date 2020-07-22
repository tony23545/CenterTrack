import sys
CENTERTRACK_PATH = "/home/tony/CenterTrack/src/lib"
sys.path.insert(0, CENTERTRACK_PATH)

from detector import Detector
from opts import opts

import rclpy
from rclpy.node import Node 
from sensor_msgs.msg import Image
import cv2
import numpy as np

MODEL_PATH = "../models/coco_pose.pth"
TASK = 'tracking' # or 'tracking,multi_pose' for pose tracking and 'tracking,ddd' for monocular 3d tracking
opt = opts().init('{} --load_model {}'.format(TASK, MODEL_PATH).split(' '))
opt.debug = max(opt.debug, 1)
detector = Detector(opt)

class MinimalSubscriber(Node):
	def __init__(self):
		super().__init__('minimal_subscriber')
		self.subscription = self.create_subscription(
			Image,
			'/realsense/camera/color/image_raw',
			self.callback,
			30)

	def callback(self, msg):
		img = np.array(msg.data)
		img = img.reshape((480, 640, 3))
		img = np.flip(img, 2)
		
		#print(ret)
		cv2.imshow("img", img)
		ret = detector.run(img)
		if cv2.waitKey(1) == 27:
			return

rclpy.init(args = None)
subs = MinimalSubscriber()
print("start spining node...")
rclpy.spin(subs)

subs.destroy_node()
rclpy.shutdown()

# for img in images:
#   ret = detector.run(img)['results']

