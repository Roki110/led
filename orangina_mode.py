import sp108e as led
import time
import sys
import os

led.CONTROLLER_IP = sys.argv[1]

# Set Orangina color animation, blue and yellow
led.change_mixed_colors_animation(0x88)
time.sleep(0.3)
led.change_speed(0)
time.sleep(0.3)
led.change_brightness(200)
time.sleep(0.3)
f = open(os.path.dirname(__file__) + "/set.txt","wt")
print("orangina", file=f)
f.close()