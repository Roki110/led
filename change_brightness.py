import sp108e as led
import time
import sys


def main(ip: str, value: str):    
    led.CONTROLLER_IP = ip
    strBright = value
    bright = int(float(strBright))
    if strBright[0] == "+" or strBright[0] == "-":
        bright +=  led.get_device_settings()['current_brightness']
    if bright < 0 :
        bright = 0
    elif bright > 255:
        bright = 255
    led.change_brightness(bright)
    print(f"Brightness changed to {bright} for SP108E at {led.CONTROLLER_IP}")

if __name__ == '__main__':
    if sys.argv.__len__() != 3:
        print("Incorrect number of arguments")
        print("   args: Ip_address brightness(0 lowest to 255 highest)")
        print("   examples:")
        print("      192.168.0.32 +20   : increase 20 brightness")
        print("      192.168.0.32 -20   : decrease 20 brightness")
        print("      192.168.0.32 200   : set brightness to 200")
        exit(1)
    main(sys.argv[1], sys.argv[2])
