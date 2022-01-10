import sp108e as led
import time
import sys
import os

led.CONTROLLER_IP = sys.argv[1]
led.change_color("#00FF00")
time.sleep(0.3)
led.change_mono_color_animation(0xd3)
time.sleep(0.3)
led.change_brightness(255)
time.sleep(0.3)

f = open(os.path.dirname(__file__) + "/set.txt","wt")
print("green", file=f)
f.close()