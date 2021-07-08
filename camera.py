from picamera.array import PiRGBArray as prgb
from picamera import PiCamera as pc
import time
import cv2 as cv
import os, shutil
path = '/home/pi/LicensePlateProject/img/temp'
def formatTempFile():
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def getCameraFrame():
    # output requirements
    resolution = [640, 480]
    frame_rate = 32
    _format = "bgr"
    save_format = ".jpg"
    #----------------------------------------------

    # save spot
    DIR = "/home/pi/LicensePlateProject/img/temp"

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
        
        os.chdir(DIR)
        cv.imwrite("lp_" + str(runner) + save_format, image)
        time.sleep(0.1)
        os.chdir(DIR)
        
        if key == ord("q"):
            break
        runner+=1
        
    cv.destroyAllWindows()
