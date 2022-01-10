import sp108e as led
import sys

def main(ip: str):
    led.CONTROLLER_IP = ip
    led.toggle_off_on()

if __name__ == '__main__':
    main(sys.argv[1])
