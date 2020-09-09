from socket import *

tcpClientSocket = socket(AF_INET, SOCK_STREAM)

def connectToServer(HOST, PORT):
    ADDRESS = (HOST, PORT)
    tcpClientSocket.connect(ADDRESS)
    print("Connected!")


def send(mes):
    BUFSIZ = 1024
    tcpClientSocket.send(mes.encode('utf-8'))
    data = tcpClientSocket.recv(BUFSIZ)
    if data is None:
        print("fail - socket error")
    return str(data)


def noReply(mes):
    tcpClientSocket.send(mes.encode('utf-8'))
    # shutdown(tcpClientSocket, SHUT_WR)


def close():
    tcpClientSocket.close()
    print("Disconnected!")
