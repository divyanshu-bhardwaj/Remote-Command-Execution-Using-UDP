import time
import socket
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__=='__main__':
    print('Client is connected to the Server\n')
    for pings in range(10):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(f"{bcolors.OKGREEN}Ready to send commands to Server{bcolors.ENDC}")
        msg = input("Enter the command that you want to exec : ")
        
        message = bytes(msg,'utf-8')
        addr = ("192.168.1.164", 12000)

        client_socket.sendto(message, addr)
        try:
            data, server = client_socket.recvfrom(1024)
            print('OUTPUT :' + str(data, 'utf-8'))
            # d = data.decode("utf-8")
            # print(f"{bcolors.WARNING}  {bcolors.ENDC}")
            
            
        except socket.timeout:
            print('REQUEST TIMED OUT')