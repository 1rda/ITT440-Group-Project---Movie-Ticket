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

	print("\n\t Choose your desired Movie!\t\n\n")
	func=input("Movie: ")


	#seat = ClientSocket.recv(1024)
	#print(seat.decode('utf-8'))

	#result=input("Seats: ")

	if (func == 'exit'):
		break
	else:
		result=input("Seats: ")
		
		#Row = int (input('Enter row - '))
		#Seats = int(input('Enter seats in a row -'))
		msg=func+" "+result+" "
		#gsm=Row+" "+Seats+" "
		ClientSocket.send(str.encode(msg))
		#ClientSocket.send(str.encode(gsm))
		tot = ClientSocket.recv(1024)
		print(tot.decode('utf-8'))

ClientSocket.close()
