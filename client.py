import socket

ClientSocket = socket.socket()

host = '192.168.56.101'
port = 8888

try:
	ClientSocket.connect((host, port))
except socket.error as e:
	print(str(e))

welcome = ClientSocket.recv(1024)
print(welcome.decode('utf-8'))

while True:
	menu = ClientSocket.recv(1024)
	print(menu.decode('utf-8'))
	break

ClientSocket.close()
