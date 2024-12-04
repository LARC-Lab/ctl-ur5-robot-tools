import cv2
import numpy as np


class Camera:
    def __init__(self, port: int, sample_name : str):
        #self.videoController = cv2.VideoCapture(port)
        self.finish : bool = False
        self.name = sample_name 
       
    def capture_video(self):
        cap = cv2.VideoCapture(0)  
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(self.name + '.avi', fourcc, 20.0, (640, 480))

        while(self.finish==True):  
            ret, frame = cap.read() 
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            out.write(hsv) 
            cv2.imshow('Original', frame)
            cv2.imshow('frame', hsv)
            if cv2.waitKey(1) & 0xFF == ord('a') or self.finish:
                break
        cap.release()
        out.release()  
        cv2.destroyAllWindows()

    def capture_image(self, filename):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow(filename)
        ret, frame = cam.read()
        img_counter = 0
        cv2.imwrite(filename, frame)
        cam.release
        

               
    
   