import socket
import sys
import time

UDP_IP = sys.argv[1]
HOSTNAME = socket.gethostname()
UDP_PORT_SEND = 5005
UDP_PORT_RECEIVE = 5006
MESSAGE = bytes(sys.argv[2])


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT_SEND))

time.sleep(1)
sock2 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock2.bind((HOSTNAME, UDP_PORT_RECEIVE))
while True:
    data, addr = sock2.recvfrom(1024)
    print(data)