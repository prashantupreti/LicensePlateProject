import detectLicensePlate as detect
import camera
import os, os.path, shutil
import time
import cv2 as cv
from picamera.array import PiRGBArray as prgb
from picamera import PiCamera as pc
import l298n_dc as motor
#motor.runMotor()

camera.formatTempFile()
camera.getCameraFrame()
DIR= "/home/pi/LicensePlateProject/img/temp"
totalImage= len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
detect.getLicensePlateNumber('lp_'+str(totalImage-1)+'.jpg')
