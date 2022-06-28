import socket
import sys
import errno
from multiprocessing import Process

def displayMenu(s_sock):
	s_sock.send(str.encode('This is the menu :D'))

def process_start(s_sock):
	s_sock.send(str.encode('Welcome to Matahari Cinema'))

	while True:
		displayMenu(s_sock)

		if(option == 'exit'):
			break

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
