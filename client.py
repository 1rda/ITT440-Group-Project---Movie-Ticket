import socket

ClientSocket = socket.socket()

host = '192.168.56.115'
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

	print("\n\t Choose your desired Movie!\t\n\n")
	func=input("Movie: ")
	#result=input("Seats: ")

	if (func == 'exit'):
		break
	else:
		result=input("Seats: ")

		msg=func+" "+result
		ClientSocket.send(str.encode(msg))
		tot = ClientSocket.recv(1024)
		print(tot.decode('utf-8'))

ClientSocket.close()
