import sp108e as led
import time
import sys

led.CONTROLLER_IP = sys.argv[1]

# Set rainbow color animation
led.change_mixed_colors_animation(0x1)
time.sleep(0.3)
led.change_speed(0)
time.sleep(0.3)
led.change_brightness(200)
time.sleep(0.3)
