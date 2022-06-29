import socket
import sys
import errno
from multiprocessing import Process

def displayMenu(s_sock):
	s_sock.send(str.encode('This is the menu :D'))

def thor(i):
	print('Movie: Thor and Love for '+i+ ' seats\n')
	i=float(i)
	ans = 8*i
	print("Total: RM ",ans)
	return ans
def tony(i):
	print('Movie: Iron Man for ' +i+' seats\n')
	i=float(i)
	ans = 9*i
	print("Total: RM ", ans)
	return ans

def process_start(s_sock):
	s_sock.send(str.encode('Welcome to Matahari Cinema'))

	while True:
		displayMenu(s_sock)
		data = s_sock.recv(2048)
		data = data.decode('utf-8')

		try:
			func, result = data.split(" ",2)
		except:
			print(" no data received \n")
			break

		if (func == '1'):
			ans=thor(result)
			#s_sock.send(str.encode('Total is ',ans))
		elif (func == '2'):
			ans=tony(result)
		elif (func  == 'exit'):
			break


		equal ="\nTotal is: RM%s\n"% str(ans)
		s_sock.send(equal.encode())
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
