# This is your main script.
from HTTP_server import web_server, msg
from boot import wlan
from machine import Pin
import socket, time, network

motor = Pin(18, Pin.OUT) # Motor pin
web_server(wlan) # HTTP server is activated


while True:
    if msg == "feed": # new msg received
        #----#
        motor.value(1)
        time.sleep(2)
        motor.value(0)
        ### SEND : THE CAT HAS BEEN FED MESSAGE
        #----#
    else:
        pass
    time.sleep(1) # wait for 1 second