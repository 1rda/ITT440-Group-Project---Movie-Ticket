#bismillah
import socket
import sys
import errno
from multiprocessing import Process

#def seats(s_sock, i)

def displayMenu(s_sock):
	s_sock.send(str.encode('\t====MAIN MENU====\n\t [1] Thor and Love\n\t [2] Iron Man\n\t [3] Cancel\n\n\n\t Choose your desired Movie!\t\n\n'))

def thor(s_sock):
	s_sock.send(str.encode('\nMovie: Thor and Love\n\nShowtime: (1)12:00\t(2)15:00'))
	option = s_sock.recv(2048)
	return option
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
			#seats(s_sock)
			#payment(s_sock)
		elif (func == '2'):
			showtime = tony(s_sock)
			#seats(s_sock)
			#payment(s_sock)
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
