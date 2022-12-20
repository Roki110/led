#!/usr/bin/python3

import os
import sp108e as led
# Manage led by RFXCom Lighting4 message (Chacon) (https://github.com/redcrab2016/RFXtrx)
led.CONTROLLER_IP = '192.168.99.52'
RFXCOM_TYPE_NAME = os.getenv('RFXCOM_TYPE_NAME')

if RFXCOM_TYPE_NAME != 'LIGHTING4':
    exit()
RFXCOM_PACKET_DATA0 = os.getenv('RFXCOM_PACKET_DATA0')
RFXCOM_PACKET_DATA1 = os.getenv('RFXCOM_PACKET_DATA1')
RFXCOM_PACKET_DATA2 = os.getenv('RFXCOM_PACKET_DATA2')

if RFXCOM_PACKET_DATA0 == '21' and RFXCOM_PACKET_DATA1 == '69':
    if RFXCOM_PACKET_DATA2 == '85':
        led.switch_on()
    if RFXCOM_PACKET_DATA2 == '84':
        led.switch_off()