import socket
import sys

UDP_IP = sys.argv[1]
UDP_PORT_SEND = 5005
UDP_PORT_RECEIVE = 5006
MESSAGE = bytes(sys.argv[2])


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT_SEND))

sock.bind(socket.gethostname(), UDP_PORT_RECEIVE)
data, addr = sock.recvfrom(1024)
print(data)