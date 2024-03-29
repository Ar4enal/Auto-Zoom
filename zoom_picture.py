import cv2
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from features import extract_image_features
from gaze_tf import test_imgs
from render_s import detect_gaze,draw_gaze
from zoom_in_out import zoom

#stadium = cv2.imread('C:/Users/DELL/Desktop/gaze/stadium.jpg')
stadium = cv2.imread('C:/Users/DELL/Desktop/gaze/shakespeare.jpg')
#cv2.namedWindow('stadium', cv2.WINDOW_NORMAL)
#cv2.resizeWindow('stadium',1280,720)
cv2.namedWindow('zoom', cv2.WINDOW_NORMAL)
cv2.resizeWindow('zoom',1920,1080)

#cv2.imshow('stadium',stadium)

def show_gaze(img):
    img, faces, face_features = extract_image_features(img)
    return test_imgs(img, faces, face_features)


class GazeDetectStreamPicture:
    
    def __init__(self):
        cap = cv2.VideoCapture(0)
        cap.set(3,1280)
        cap.set(4,720)
        cap.set(11, 0.1)
        cap.set(15, 0.01)
        
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.frameID = int(cap.set(cv2.CAP_PROP_FRAME_COUNT, 1))
        cap.set(6, 1)
        self.is_first_frame = True
        self.cap = cap
        self.fps = cap.get(cv2.CAP_PROP_FPS)
        self.multiplier = self.fps * 2
        self.g = 0
        #self.frameID = int(round(self.cap.get(1)))
        self.timer = 0

    def __iter__(self):
        return self
        
    def __next__(self):
        
        self.frameID += 1
        #print(self.frameID)
        outputs=[]
        ret, frame = self.cap.read()
        
        if self.frameID % self.multiplier == 0:
            outputs = show_gaze(frame)
            print(self.frameID)
            gaze = detect_gaze(frame,outputs,1280,720,12,720)
            if self.g != gaze:
                self.timer = 0
                print('last for: %i seconds'%self.timer)
            else:
                self.timer += 1
                print('last for: %i seconds'%self.timer)
            self.g = gaze
        return self.g
        
for g in GazeDetectStreamPicture():   
    result = zoom(stadium,g)
    cv2.imshow('zoom',result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()