import sp108e as led
import sys

led.CONTROLLER_IP = sys.argv[1]
led.toggle_off_on()