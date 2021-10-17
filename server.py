import socket
from datetime import datetime


def log_file(time, message, sender, recipient):
    """
    Write to log file
    @param time: time in format: "Y-M-D H:M:S"
    @param message: the message
    """
    with open('message_log.log', 'a') as log:
        log.write(f"\ntime: {time} ,message: {message} from: {sender} to: {recipient}\n")


UDP_IP = '0.0.0.0'
UDP_PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.bind((UDP_IP, UDP_PORT))
dict_db = {}

while True:
    data, addr = sock.recvfrom(1024)

    if addr in dict_db.values():
        message = (data.decode()).split(" ", 2)
        # message[0] is the sender, message[1] is the recipient, message[2] is the message
        if message[1] in dict_db.keys():
            sock.sendto(f"{message[0]} send: {message[2]}".encode(), dict_db[message[1]])
            log_file(datetime.now(), message[2], message[0], message[1])
        else:
            sock.sendto(f"There is no user named {message[1]}".encode(), addr)
    else:
        # Add to db {name: address}
        dict_db[data.decode()] = addr
