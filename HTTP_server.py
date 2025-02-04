import socket
body = None
msg = None

# HTTP Sunucusu
def web_server(wlan):
    addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print("[OK] server ip > ", wlan.ifconfig()[0])

    while True:
        conn, addr = s.accept()
        print("new connection accepted:", addr)
        request = conn.recv(1024)
        print("req > ", request)

        # Mesaj içeriğini analiz et
        if b"POST" in request:
            body_start = request.find(b"\r\n\r\n") + 4
            body = request[body_start:]
            msg = body.decode()
            print("received message > ", msg)

        # Yanıt gönder
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\RECIEVED"
        conn.send(response.encode())
        conn.close()

web_server()