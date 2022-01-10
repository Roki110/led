import sp108e as led
import time
import sys

def main(ip: str, value: str):
    led.CONTROLLER_IP = ip
    strSpeed = value
    speed = int(float(strSpeed))
    if strSpeed[0] == "+" or strSpeed[0] == "-":
        speed += led.get_device_settings()['animation_speed']
    if speed < 0:
        speed = 0
    elif speed > 255:
        speed = 255
    led.change_speed(speed)
    print(f"Animation speed changed to {speed} for SP108E at {led.CONTROLLER_IP}")


if __name__ == '__main__':
    if sys.argv.__len__() != 3:
        print("Incorrect number of arguments")
        print("   args: Ip_address speed(0 slowest to 255 fastest)")
        print("   examples:")
        print("      192.168.0.32 +20   : increase 20 speed")
        print("      192.168.0.32 -20   : decrease 20 speed")
        print("      192.168.0.32 200   : set speed to 200")
        exit(1)
    main(sys.argv[1], sys.argv[2])

