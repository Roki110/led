import sp108e as led
import time
import sys
import binascii
import os

if sys.argv.__len__() != 3:
    print("Incorrect number of arguments")
    print("   args: Ip_address animation(0-179 multi color anim, 205-219 mono color anim)")
    print("   examples:")
    print("      192.168.0.32 +1   : Set to next animation")
    print("      192.168.0.32 -1   : Set to previous animation")
    print("      192.168.0.32 23   : Set animation to 23")
    exit(1)

led.CONTROLLER_IP = sys.argv[1]
anim = str(sys.argv[2])
current_anim = int(anim)
raw_settings = led.get_device_raw_settings()
if anim[0] == "-" or anim[0] == '+':
    current_anim += int.from_bytes(binascii.unhexlify(raw_settings[4:6]),byteorder='little', signed=False)
    if current_anim < 0:
        current_anim = 0xb3
    if current_anim > 212:
        current_anim = 205
    if 179 < current_anim < 205:
        if anim[0] == "-":
            current_anim = 212
        else:
            current_anim= 0
led.change_mono_color_animation(current_anim)
time.sleep(0.3)

settings = led.get_device_settings()
animation = settings['current_animation']
f = open(os.path.dirname(__file__) + "/set.txt","wt")
print(animation, file=f)
f.close()

