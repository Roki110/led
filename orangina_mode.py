import sp108e as led
import time
import sys
import os


def main(ip: str):
    led.CONTROLLER_IP = ip
    led.change_mixed_colors_animation(0x88)
    time.sleep(0.3)
    led.change_speed(0)
    time.sleep(0.3)
    led.change_brightness(200)
    time.sleep(0.3)
    f = open(os.path.dirname(__file__) + "/set.txt", "wt")
    print("orangina", file=f)
    f.close()


if __name__ == '__main__':
    main(sys.argv[1])
