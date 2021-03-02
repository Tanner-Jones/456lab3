import socket
import time


def check_to_pad(message):
    # Function to account for odd number of blocks
    # Pads end with a null character to be removed on decryption
    if (len(message) % 2 == 1):
        message.append(0)
        return message
    else:
        return message

def encrypt_block(sixteen,key):
    # Block encryption takes place within this function
    # Encryption protocol based on what lab asks for
    newRight = sixteen[0] ^ ord(key)
    newSixteen = bytearray([sixteen[1]]) + bytearray([newRight])
    return newSixteen

def encrypt(message, iterations):
    # general encryption function. Treats and formats text from message and manages message length by reducing size
    # until message length is zero
    key = "XTGPOITJ"
    # additionally manages iterations and updated message after encryption
    if len(message) % 2 == 1:
        padding = 1
    else:
        padding = 0
    check_to_pad(message)
    for i in range(0, iterations):
        encryptedMessage = bytearray()
        length = len(message)
        while (length > 0):
            sixteen = message[0:2]
            newSixteen = encrypt_block(sixteen,key[i])
            encryptedMessage.append(newSixteen[0])
            encryptedMessage.append(newSixteen[1])
            del message[0]
            del message[0]
            length = len(message)
        message = encryptedMessage
    print(message)
    return message

def main_encrypt(mes):
    message_final = encrypt(bytearray(mes), 8)
    return message_final



UDP_IP = socket.gethostname()
UDP_PORT_RECEIVE = 5005
UDP_PORT_SEND = 4444

print(UDP_IP)
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT_RECEIVE))
message_list = []

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data = main_encrypt(data)
    print("\nRecent Messages:")
    message_list.insert(0, (data, time.time()), addr[0])
    sock2 = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    time.sleep(2)
    sock2.sendto(bytes("\nRecent Messages:"), (addr[0], UDP_PORT_SEND))
    if len(message_list) > 5:
        message_list.pop(5)
    for message in message_list:
        message_send = str(message_list.index(message) + 1) + ": " + message[0] + ", IP: " + message[2] + " Time: " + \
                  str(time.ctime(message[1]))
        print(message_send)
        sock2.sendto(bytes(message_send), (addr[0], UDP_PORT_SEND))