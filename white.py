import sp108e as led
import time

led.CONTROLLER_IP="192.168.99.54"
led.change_color("#FFFFFF")
time.sleep(0.3)
led.change_mono_color_animation(0xd3)
time.sleep(0.3)
led.change_brightness(255)
time.sleep(0.3)
