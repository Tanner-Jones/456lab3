import socket
import time

UDP_IP = socket.gethostname()
UDP_PORT_RECEIVE = 5005
UDP_PORT_SEND = 5006

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
message_list = []

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    message_list.insert(0, data)
    if len(message_list) > 5:
        message_list.pop(5)
    for message in message_list:
        print(message.index(), message, time.time())
        sock.sendto(message, (addr[0], UDP_PORT_SEND))