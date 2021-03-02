import socket
import sys
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
    newSixteen = bytes([sixteen[1]]) + bytes([newRight])
    return newSixteen

def encrypt(message, iterations):
    # general encryption function. Treats and formats text from message and manages message length by reducing size
    # until message length is zero
    key = "12345678"
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
            print(type(newSixteen[0]))
            print(newSixteen[0])
            print(newSixteen[1])
            encryptedMessage.append(int(newSixteen[0]))
            encryptedMessage.append(int(newSixteen[1]))
            del message[0]
            del message[0]
            length = len(message)
        message = encryptedMessage
    print(message)
    return message

def main_encrypt(mes):
    message_final = encrypt(bytearray([mes]), 8)
    return message_final


UDP_IP = sys.argv[1]
HOSTNAME = socket.gethostname()
UDP_PORT_SEND = 5005
UDP_PORT_RECEIVE = 4444

while True:
    print("Enter Message:")
    mes = raw_input()
    mes = main_encrypt(mes)
    MESSAGE = bytes(mes)


    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT_SEND))

    time.sleep(1)
    sock2 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock2.bind((HOSTNAME, UDP_PORT_RECEIVE))
    sock2.settimeout(5)
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