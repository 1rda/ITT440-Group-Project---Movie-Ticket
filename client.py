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

	#print("\n\t Choose your desired Movie!\t\n\n")
	func=input("Movie: ")
	ClientSocket.send(str.encode(func))

	#print(seat.decode('utf-8'))

	#result=input("Seats: ")

	if (func == '3'):
		break
	else:
		showtime = ClientSocket.recv(1024)
		print(showtime.decode('utf-8'))
		option = input('\nPick a showtime: ')
		ClientSocket.send(str.encode(option))

ClientSocket.close()
