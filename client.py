import requests

ESP_IP = "192.168.1.106"  # ESP'nin IP adresi
url = f"http://{ESP_IP}"

response = requests.post(url, data=b'1')

print("Sunucudan Gelen Yanıt:", response.text)