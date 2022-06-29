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
	func=input("\t [1] Thor and Love\n\t [2] Iron Man\n\t [exit] Cancel\nMenu: ")

	if (func == '1'):
		print("\n\nHow many seats?")
		result=input("[?] Seats: ")
	elif (func == '2'):
		print("\n\nHow many seats?")
		result=input("[?] Seats: ")
	elif (func == 'exit'):
		break

	msg=func+" "+result

	ClientSocket.send(str.encode(msg))
	#menu = ClientSocket.recv(1024)
	#print(menu.decode('utf-8'))
	tot = ClientSocket.recv(1024)
	print(tot.decode('utf-8'))

	#break

ClientSocket.close()
