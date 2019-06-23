import cv2
import numpy as np



def zoom(frame, gaze):
    h, w, c = frame.shape
    #cv2.namedWindow('Zoom', cv2.WINDOW_NORMAL)
    if gaze==1:
        yMin = h//4
        yMax = h
        xMin = w//4
        xMax = w
        frame = frame[yMin:yMax, xMin:xMax]

    elif gaze==2:
        yMin = 0
        yMax = (h//4)*3
        xMin = w//4
        xMax = w
        frame = frame[yMin:yMax, xMin:xMax]

    elif gaze==3:
        yMin = h//4
        yMax = h
        xMin = 0
        xMax = (w//4)*3
        frame = frame[yMin:yMax, xMin:xMax]
        
    elif gaze==4:
        yMin = 0
        yMax = (h//4)*3
        xMin = 0
        xMax = (w//4)*3
        frame = frame[yMin:yMax, xMin:xMax]

    return frame