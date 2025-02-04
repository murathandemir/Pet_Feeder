import network

def connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        pass
    
    print("[NET OK] netconfig > ", wlan.ifconfig())
    return wlan

# connect_with_timeout(SSID, PASSWORD) # USING THE FUNCTION
