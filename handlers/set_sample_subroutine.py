from utils.vial_shake_generator import vial_shake_generator as vsg
import time

from handlers.robot_handler import robot as Robot
from handlers.gripper_handler import gripper_handler as Gripper

APPROACH_POSE = [1.7559785842895508, -1.2860432130149384, 1.5787866751300257, -1.8402077160277308, -1.598492447529928, 3.322289228439331]
SET_POSE = [1.75752592086792, -1.190208987598755, 1.7757566610919397, -2.1761652431883753, -1.605079476033346, 3.3491060733795166]

## this subrouting extends the robot class (it has all the methods and attributes and can make more)
class set_sample_subroutine():
    def __init__(self, robot: Robot, gripper :Gripper):
        self.robot = robot
        self.gripper = gripper
    
    
    #def run(self, position: list):
    def run(self):
        self.robot.move_joints_fast(APPROACH_POSE)
        self.robot.move_joints_slow(SET_POSE)
        self.gripper.open()
        self.robot.move_joints_slow(APPROACH_POSE)