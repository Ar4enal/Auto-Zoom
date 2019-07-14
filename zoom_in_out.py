import cv2
import numpy as np

def zoom(frame, gaze):
    h, w, c = frame.shape
    #cv2.namedWindow('Zoom', cv2.WINDOW_NORMAL)
    if gaze==1:
        yMin = h//5
        yMax = h
        xMin = w//5
        xMax = w
        frame = frame[yMin:yMax, xMin:xMax]
        
    elif gaze==2:
        yMin = 0
        yMax = (h//5)*4
        xMin = w//5
        xMax = w
        frame = frame[yMin:yMax, xMin:xMax]
        
    elif gaze==3:
        yMin = h//5
        yMax = h
        xMin = 0
        xMax = (w//5)*4
        frame = frame[yMin:yMax, xMin:xMax]
        
    elif gaze==4:
        yMin = 0
        yMax = (h//5)*4
        xMin = 0
        xMax = (w//5)*4
        frame = frame[yMin:yMax, xMin:xMax]
        
    return frame