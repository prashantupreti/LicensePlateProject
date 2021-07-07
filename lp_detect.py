from picamera.array import PiRGBArray as prgb
from picamera import PiCamera as pc
import time
import cv2 as cv
import os

# output requirements
resolution = [640, 480]
frame_rate = 32
_format = "bgr"
save_format = ".jpg"
#----------------------------------------------

# save spot
path = "/home/pi/project/img"

camera = pc()
raw_image = prgb(camera)
camera.resolution = resolution
camera.framerate = frame_rate
raw_feed = prgb(camera, size=resolution)

time.sleep(0.1)

runner = 0

for frame in camera.capture_continuous(raw_feed, _format, use_video_port=True):
    image = frame.array
    
    cv.imshow("Frame", image)
    key = cv.waitKey(1) & 0xFF
    
    raw_feed.truncate(0)
    
    os.chdir(path)
    cv.imwrite("vid_cap_" + str(runner) + save_format, image)
    time.sleep(0.1)
    os.chdir("/home/pi/project")
    
    if key == ord("q"):
        break
    runner+=1