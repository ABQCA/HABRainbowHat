# Rainbow Hat HAB v1.0
# Broilo

import rainbowhat as rh
import time
import subprocess
import picamera

def display_message(message):
    rh.display.clear()
    rh.display.print_str(message)
    rh.display.show()

def control_camera(command):
    if command=='start':
        timestr = time.strftime("%Y%m%d-%H%M%S")
        camera.resolution = (1080, 720)
        camera.start_recording('/media/pi/DATA/%s.h264' % timestr)
    else:
        camera.stop_recording()
        
@rh.touch.A.press()
def press_a(channel):
    rh.rainbow.clear()
    display_message("Run")
    rh.rainbow.set_pixel(6, 0, 255, 0, brightness=0.1)
    rh.rainbow.show()
    rh.lights.rgb(0,1,0)
    #rh.buzzer.midi_note(90, 1)
    subprocess.call("/home/bin/GPSLogger.sh")
    rh.rainbow.set_pixel(4, 0, 255, 0, brightness=0.1)
    rh.rainbow.show()
    control_camera('start')
    rh.rainbow.set_pixel(3, 0, 255, 0, brightness=0.1)
    rh.rainbow.show()
    
@rh.touch.B.press()
def press_b(channel):
    rh.rainbow.clear()
    display_message("End")
    rh.rainbow.set_pixel(5, 255, 0, 0, brightness=0.1)
    rh.rainbow.show()
    rh.lights.rgb(1,0,0)
    #rh.buzzer.midi_note(80, 1)
    subprocess.call("/home/bin/StopGPS.sh")
    control_camera('stop')
    rh.rainbow.set_pixel(4, 0, 0, 0)

try:
    global camera
    camera = picamera.PiCamera()
    while True:
        time.sleep(0.05)
        
except KeyboardInterrupt:
    pass
