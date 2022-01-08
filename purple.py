import sp108e as led
import time
import sys

led.CONTROLLER_IP = sys.argv[1]
led.change_color("#820080")
time.sleep(0.3)
led.change_mono_color_animation(0xd3)
time.sleep(0.3)
led.change_brightness(255)
time.sleep(0.3)
