import socket, threading, sys


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("Nova conexão adicionada ", clientAddress)

    def run(self):
        print("Conexão de:  ", clientAddress)
        message = ''
        while True:
            data = self.csocket.recv(2048)
            message = data.decode()
            text = message.split(": ", 1)
            if text.find("quit"):
                print("Cliente ", text[0], " desconectado..")
                exit()
            print("messagem do cliente ", message)
            self.csocket.send(bytes(message, 'UTF-8'))
        


LOCALHOST = "localhost"
PORT = 4444
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Servidor online")
while True:
    server.listen()
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()