# This is script that run when device boot up or wake from sleep.
from netConnect import connect
from machine import Pin
import time

SSID = "TTNET_TP-LINK_AC91"
PASSWORD = "cHZSfxqN"
status_led = Pin(19, Pin.OUT)

status_led.value(0) # initially the status of the connection is 0
wlan = connect(SSID, PASSWORD) # if this line is passed, the connection is GUARANTEED! -inside the connect function-
status_led.value(1) # if the connection is successful, the status is 1

