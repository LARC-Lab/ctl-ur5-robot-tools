
from PIL import ImageTk, Image
import numpy as np
import math
import os
import sys



from handlers.vial_shake_subroutine import vial_shake_subroutine as shake_vial
from handlers.robot_handler import robot as Robot
from handlers.gripper_handler import gripper_handler as Gripper
from handlers.pick_sample_subroutine import pick_sample_subroutine as pick_sample
from utils.coordinate_generator import coord_handler
from handlers.set_sample_subroutine import set_sample_subroutine as place_vial
from handlers.camera_handler import Camera
from utils.coordinate_utility import coordinate_util as cord_utility
import threading
NUMBER_SAMPLES = 2
SET_POSE = [1.757969856262207, -1.1455830794623871, 1.8073609511004847, -2.238370557824606, -1.6023200193988245, 3.2870290279388428]
PICK_POSE = [0.6805216670036316, -0.5859013360789795, 1.186540428792135, -0.6354494851878663, -0.9158652464496058, 0.0343778133392334]
def startup():
     robot = Robot("192.168.0.2",30003)
     
     gripper=Gripper("192.168.0.2", 63352)
     
     return robot, gripper

def collect_training_data():
     
    
     robot, gripper = startup()
     
     print("Done startup")
     #input("Drive robot to first pick position, press enter when done")
     #first_pick  = robot.get_joints()
    # input("Drive robot to first place position and press enter")
     #first_set = robot.get_joints()
     
     ## coordinate handler 
     positions = coord_handler(PICK_POSE, 8,SET_POSE,4)     
     print("got the joint positions, starting")
     
     ## this is the main loop!
     pick = pick_sample(robot, gripper)
     shake = shake_vial(3,robot)
     place = place_vial(robot, gripper)
     cord_util = cord_utility()
     

     for i in range(NUMBER_SAMPLES):
          ## pick the sample up
          #pick.run(positions.pick_positions[i])
          gripper.open()
          pick.run()

          ## this should kick off the camera! 
          shake.shake_vial(i, "visc")
          #place.run(positions.set_positions[math.floor(i/2)])
          place.run()

def degreestorad(list):
     for i in range(6):
          list[i]=list[i]*(math.pi/180)
     return(list)    
    

if __name__=="__main__":
     collect_training_data()