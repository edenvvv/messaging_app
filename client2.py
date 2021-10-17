from threading import Thread
import socket
import sys

server_addr = ('127.0.0.1', 9999)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
my_name = input('Enter your name: ')
sock.sendto(my_name.encode(), server_addr)
print("enter the name of the person you want to send a message + space and the message")


def output_recvfrom(sock):
    while True:
        data, _ = sock.recvfrom(1024)
        if not data: break
        print(data.decode())


x = Thread(target=output_recvfrom, args=(sock,))
x.start()
for line in sys.stdin:
    line = f"{my_name} " + line
    sock.sendto(line.strip().encode(), server_addr)
sock.close()
x.join()
