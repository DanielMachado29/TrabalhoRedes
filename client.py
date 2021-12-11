import socket
import sys

if len(sys.argv) <= 2:
  print("Por favor use argumentos <Nome> <ip> ")
  sys.exit()

nomeCliente = sys.argv[1]
SERVER = sys.argv[2]
PORT = 4444
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
message = nomeCliente + "entrou."
client.sendall(bytes(message,'UTF-8'))
while True:
  in_data =  client.recv(1024)
  print("From Server: " ,in_data.decode())
  out_data = input()
  send =  "|| " + nomeCliente + ": " + out_data
  client.sendall(bytes(send,'UTF-8'))
  if out_data== 'quit':
   break
client.close()