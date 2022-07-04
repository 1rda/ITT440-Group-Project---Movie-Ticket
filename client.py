import socket

ClientSocket = socket.socket()

host = '192.168.56.101'
port = 8888

try:
	ClientSocket.connect((host, port))
except socket.error as e:
	print(str(e))

welcome = ClientSocket.recv(2048)
print(welcome.decode('utf-8'))

while True:

	menu = ClientSocket.recv(2048)
	print(menu.decode('utf-8'))

	func=input("Movie: ")
	ClientSocket.send(str.encode(func))

	#print(seat.decode('utf-8'))

	#result=input("Seats: ")

	if (func == '3'):
		break
	else:
		showtime = ClientSocket.recv(2048)
		print(showtime.decode('utf-8'))
		option = input('\nPick a showtime: ')
		ClientSocket.send(str.encode(option))

		#ask for number of seats
		numseats = ClientSocket.recv(2048)
		num_seats = input(numseats.decode('utf-8'))
		ClientSocket.send(str.encode(num_seats))

		#display seats
		seatsdisplay = ClientSocket.recv(2048)
		print(seatsdisplay.decode('utf-8'))

		#choose seats
		seats = ClientSocket.recv(2048)

		for x in range(int(num_seats)):
			pickedSeat = input(seats.decode('utf-8'))
			ClientSocket.send(str.encode(pickedSeat))

ClientSocket.close()
