# ros2 wrapper for CenterTrack

This repo is forked from the official implementation of CenterTrack and add ROS2 wrapper to receive images over ros topics. I am using Ubuntu 20.04 + ros2 foxy.

### ros2 + conda

It seems ros2 is not officially supporting conda currently. The error message is something like no module named ```rclpy._rclpy```. I have a dirty work-around of this problem. Under a particular conda env, I clone the source code of several ros2 packages (rclpy, rcl_interfaces, common_interfaces) into a workspace and build it. Then I can run or launch without problem.

### run demo

I use Intel Realsense D435i in this project. You can simply change the topic name in ```src/ros2_demo.py``` to work with your own camera.  

In one terminal, launch your camera node. You can also use ros2 bag...  

In another terminal, run the demo 

```
python ros2_demo.py tracking,dd --load_model ../models/coco_tracking.pth --demo webcam
```
