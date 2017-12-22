import picamera
from time import sleep

camera = picamera.PiCamera()
camera.resolution = (1024, 768)

camera.vflip = True
camera.hflip = True
frame_number = 0
while frame_number < 60:
    camera.capture('IMAGE_%06d.JPG' % frame_number)
    frame_number = frame_number + 1
