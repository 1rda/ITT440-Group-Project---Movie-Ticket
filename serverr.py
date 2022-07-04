#bismillah
import socket
import sys
import errno
from multiprocessing import Process
#seats = [A1, A2, A3, A4, A5, B1, B2, B3, B4, B5, C1, C2, C3, C4, C5, D1, D2, D3, D4, D5, E1, E2, E3, E4, E5]
seatsTaken = []

def seats(s_sock):
	s_sock.send(str.encode('Number of seat(s): '))
	numseats = s_sock.recv(2048)
	s_sock.send(str.encode('----------------[Screen]----------------\n\n\t| A1 | A2 | A3 | A4 | A5 |\n\t| B1 | B2 | B3 | B4 | B5 |\n\t| C1 | C2 | C3 | C4 | C5 |\n\t| D1 | D2 | D3 | D4 | D5 |\n\t| E1 | E2 | E3 | E4 | E5 |\n\n'))
	s_sock.send(str.encode('Choose your seat(s): '))

	for x in range(int(numseats)):
		pickedSeat = s_sock.recv(2048)
		pickedSeat.decode('utf-8')
		#seatsTaken.append(pickedSeat)

		for y in seatsTaken:
			if (pickedSeat != y):
				continue
			else:
				seatsTaken.append(pickedSeat)
				break


	for x in seatsTaken:
		print(x.decode('utf-8'))


def displayMenu(s_sock):
	s_sock.send(str.encode('\t====MAIN MENU====\n\t [1] Thor and Love\n\t [2] Iron Man\n\t [3] Cancel\n\n\n\t Choose your desired Movie!\t\n\n'))

def thor(s_sock):
	s_sock.send(str.encode('\nMovie: Thor and Love\n\nShowtime: (1)12:00\t(2)15:00'))
	option = s_sock.recv(2048)
	return option

def hall(s_sock):
	s_sock.send(str.encode('\nHall: (1)Hall 1\t(2)Hall 2'))
	halls = s_sock.recv(2048)
	return halls

def tony(i):
	s_sock.send(str.encode('\nMovie: Iron Man\n\nShowtime: (1)9:00\t(2)21:00'))
	option = s_sock.recv(2048)
	return option

def process_start(s_sock):
	s_sock.send(str.encode('Welcome to Matahari Cinema\n'))

	while True:
		displayMenu(s_sock)
		func = s_sock.recv(2048)
		func = func.decode('utf-8')

		'''try:
			func, result = data.split(" ",2)
		except:
			print(" no data received \n")
			break
'''
		if (func == '1'):
			showtime = thor(s_sock)
			hall(s_sock)
			seats(s_sock)
			#hall= thor(s_sock)
			#optionn = screen(s_sock)
			#payment(s_sock)
			#ticketGenerator(s_sock)
		elif (func == '2'):
			showtime = tony(s_sock)
			hall(s_sock)
			seats(s_sock)
			#payment(s_sock)
			#ticketGenerator(s_sock)
		elif (func == '3'):
			break


		#equal ="\nTotal is: RM%s\n"% str(ans)
		#s_sock.send(equal.encode())
	s_sock.close()

if __name__ == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', 8888))

	print('[*] Listening...')
	s.listen(5)

	try:
		while True:
			try:
				s_sock, s_addr = s.accept()
				p = Process(target = process_start, args = (s_sock, ))
				p.start()
			except socket.error:
				print('[!] Socket Error!')
	except Exception as e:
		print('[!] An exception occured!')
		print(e)
		sys.exit(1)

	finally:
		s.close()
