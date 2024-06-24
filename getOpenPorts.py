import socket
import pyfiglet
from datetime import datetime
import sys


ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

target_dns = input("Enter an ip address/domain name: ")
target = "".join(socket.gethostbyname_ex(target_dns)[2])

print("_" * 50)
print(f"Scanning Target: {target}")
print("Scanning started at: "+str(datetime.now().strftime("%d-%m-%Y %H:%M")))
print("_" * 50)

try:
    for port in range(1000):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.001)
        result = client.connect_ex((target, port))
        if result == 0:
            print(f'Port {port} is open')
        #else:
            #print('Port is closed')
    client.close()

except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()
