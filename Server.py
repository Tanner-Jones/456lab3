import socket

UDP_IP = socket.gethostname()
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
message_list = []

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    message_list.insert(data, 0)
    if len(message_list) > 5:
        message_list.pop(5)
    for message in message_list:
        sock.sendto(message, addr)