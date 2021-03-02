import socket
import time

UDP_IP = socket.gethostname()
UDP_PORT_RECEIVE = 5005
UDP_PORT_SEND = 5006

print(UDP_IP)
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT_RECEIVE))
message_list = []

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("\nRecent Messages:")
    message_list.insert(0, data)
    sock2 = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    if len(message_list) > 5:
        message_list.pop(5)
    for message in message_list:
        message_send = str(message_list.index(message) + 1) + ": " + message + ", IP: " + addr[0] + " Time: " + \
                  str(time.ctime(time.time()))
        print(message_send)
        time.sleep(1)
        sock2.sendto(bytes(message_send), (addr[0], UDP_PORT_SEND))