import socket
import sys

UDP_IP = sys.argv[1]
HOSTNAME = socket.gethostname()
UDP_PORT_SEND = 5005
UDP_PORT_RECEIVE = 5006
MESSAGE = bytes(sys.argv[2])


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT_SEND))

sock2 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
print(HOSTNAME, UDP_PORT_RECEIVE)
sock2.bind((HOSTNAME, UDP_PORT_RECEIVE))
data, addr = sock.recvfrom(1024)
print(data)