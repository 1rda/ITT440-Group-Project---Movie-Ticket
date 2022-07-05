#hehe
import socket
import time

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


	#Display main menu taken from server
	menu = ClientSocket.recv(2048)
	print(menu.decode('utf-8'))

	#Input movie
	func=input("Movie: ")
	ClientSocket.send(str.encode(func))

	if (func == '3'):
		print('Thank you! Come again.')
		break
	else:

		#ask for showtime
		showtime = ClientSocket.recv(2048)
		print(showtime.decode('utf-8'))
		option = input('Pick a showtime: ')
		ClientSocket.send(str.encode(option))

		#ask for hall
		hallz = ClientSocket.recv(2048)
		print(hallz.decode('utf-8'))
		halls = input('\nPick a Hall: ')
		ClientSocket.send(str.encode(halls))

		#ask for number of seats
		numseats = ClientSocket.recv(2048)
		num_seats = input(numseats.decode('utf-8'))
		ClientSocket.send(str.encode(num_seats))

		#display seats
		seatsdisplay = ClientSocket.recv(2048)
		print(seatsdisplay.decode('utf-8'))

		#unavailable seats
		#cannotSeat = ClientSocket.recv(2048)

		#choose seats
		seats = ClientSocket.recv(2048)

		for x in range(int(num_seats)):
			pickedSeat = input(seats.decode('utf-8'))
			ClientSocket.send(str.encode(pickedSeat))
			msg = ClientSocket.recv(2048)
			#msg.decode('utf-8')
			if(msg.decode('utf-8') != '0'):
				print(msg.decode('utf-8'))
				print('')
				repickSeat = ClientSocket.recv(2048)
				try:
					pickedSeat = input(repickSeat.decode('utf-8'))
				except:
					print('Nope.')
				ClientSocket.send(str.encode(pickedSeat))
			else:
				msg = ''
		pay = ClientSocket.recv(2048)
		print(pay.decode('utf-8'))

		recep = ClientSocket.recv(2048)
		print(recep.decode('utf-8'))

ClientSocket.close()

