import sp108e as led
import time

# Set Orangina color animation, blue and yellow
led.change_mixed_colors_animation(0x88)
time.sleep(0.3)
led.change_speed(0)
time.sleep(0.3)
led.change_brightness(200)
time.sleep(0.3)
