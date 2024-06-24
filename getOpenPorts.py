import socket

target_ip = "127.0.0.1"

for i in range(1000):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.001)
    result = client.connect_ex((target_ip, i))
    if result == 0:
        print(f'Port {i} is open')
    #else:
        #print('Port is closed')
client.close()
