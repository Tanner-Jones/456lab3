import socket
import sys
import time

UDP_IP = sys.argv[1]
HOSTNAME = socket.gethostname()
UDP_PORT_SEND = 5005
UDP_PORT_RECEIVE = 4444

while True:
    print("Enter Message:")
    mes = raw_input()
    MESSAGE = bytes(mes)


    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT_SEND))

    time.sleep(1)
    sock2 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock2.bind((HOSTNAME, UDP_PORT_RECEIVE))
    sock2.settimeout(10)
    current_time = time.time()
    while True:
        try:
            data, addr = sock2.recvfrom(1024)
        except socket.timeout:
            break
        except socket.error:
            break
        print(data)
        if time.time() > (current_time + 10):
            break