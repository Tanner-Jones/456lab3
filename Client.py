import socket
import sys

UDP_IP = sys.argv[1]
UDP_PORT = 5005
MESSAGE = bytes(sys.argv[2])


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))