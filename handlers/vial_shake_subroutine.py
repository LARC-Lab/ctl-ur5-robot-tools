from utils.vial_shake_generator import vial_shake_generator as vsg
import time
from utils.coordinate_utility import coordinate_util as coord_util
from handlers.robot_handler import robot as Robot
from handlers.camera_handler import Camera 

CAMERA_POSE = [2.7035980224609375, -1.1756010812572022, 1.2089040915118616, -1.6375476322569789, -1.5411441961871546, 4.249309539794922]

## this subrouting extends the robot class (it has all the methods and attributes and can make more)
class vial_shake_subroutine():
    def __init__(self, number_cycles : int, robot: Robot):
        self.robot : Robot = robot ## this would be a pointer to the robot object IF I HAD POINTERS
        #self.start_point = self.robot.current_position ## this will get the current joint positions from the robot
        self.start_point = CAMERA_POSE
        self.shake_cycles : int  = number_cycles
        self.vsg = vsg(1.57,number_cycles,self.start_point) ## this uses the helper function to generate the shake positions
    
    def shake_vial(self, sample_number : int, type: str):
        ## the robot subroutine that shakes the vial in space (gets its own start position)
        base_filename = str(sample_number) + type
        camera = Camera(0, base_filename)
        camera.finish=False
        camera.name=type + str(sample_number) 
        camera.capture_video()
        for i in range(self.shake_cycles):
            for j in range(len(self.vsg.shake_coords)):
                #camera.name=base_filename+str(j)+".tiff"
                #camera.capture_img(base_filename+str(j)+".tiff")
                self.robot.move_joints_slow(self.vsg.shake_coords[j])
                time.sleep(0.5)
        camera.finish= True

    