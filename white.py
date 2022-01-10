import sp108e as led
import time
import sys
import os 


def main(ip: str):
    led.CONTROLLER_IP = ip
    led.change_color("#FFFFFF")
    time.sleep(0.3)
    led.change_mono_color_animation(0xd3)
    time.sleep(0.3)
    led.change_brightness(255)
    time.sleep(0.3)
    f = open(os.path.dirname(__file__) + "/set.txt","wt")
    print("white", file=f)
    f.close()

if __name__ == '__main__':
    main(sys.argv[1])
