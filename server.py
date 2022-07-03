#bismillah
import socket
import sys
import errno
from multiprocessing import Process

def displayMenu(s_sock):
	s_sock.send(str.encode('\t====MAIN MENU====\n\t [1] TopGun\n\t [2] Iron Man\n\t [3] Star Wars\n\t [exit] Cancel\n\n'))

def seatsmenu(s_sock):
	x = 10
	Booked_seat = 0
	tixprice = 0
	Total_Income = 0
	Row = int(input('Enter number of Row - \n'))
	Seats = int(input('Enter number of seats in a Row - \n'))
	seatings = Row*Seats
	Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]


	#nak keluarkan seats |s|s|s|
	class chart:

		@staticmethod
		def chart_maker():
			seats_chart = {}
			for i in range(Row):
				seats_in_row = {}
				for j in range(Seats):
					seats_in_row[str(j+1)] = 'S'
				seats_chart[str(i)] = seats_in_row
			return seats_chart

		@staticmethod
		def find_percentage():
			percentage = (Booked_seat/Total_seat)*100
			return percentage

	class_call = chart
	table_of_chart = class_call.chart_maker()


	#starts to call out for seats
	while x != 0:
		print('1 for Show the seats \n2 for Buy a Ticket \n3 for Statistics ','\n4 for show booking \n0 for Exit')
		x = int(input('Select Option - '))
		if (x == 1):
			if (Seats < 10):
				for seat in range(Seats):
					print(seat, end='  ')
				print(Seats)
			else:
				for seat in range(10):
					print(seat, end='  ')
				for seat in range(10, Seats):
					print(seat, end=' ')
				print(Seats)
			if (Seats < 10):
				for num in table_of_chart.keys():
					print(int(num)+1, end='  ')
					for no in table_of_chart[num].values():
						print(no, end='  ')
					print()
			else:
				count_num = 0 
				for num in table_of_chart.keys():
					if (int(list(table_of_chart.keys())[count_num]) < 9):
						print(int(num)+1, end='  ')
					else:
						print(int(num)+1, end=' ')
					count_key = 0
					for no in table_of_chart[num].values():
						if (int(list(table_of_chart[num].keys())[count_key]) <= 10):
							print(no, end='  ')
						else:
							print(no, end='  ')
						count_key += 1
					count_num += 1
					print()
				print('Vacant Seats = ', Total_seat - Booked_seat)
				print()
		elif( x == 2):
			Row_number = int(input('Enter Row Number - \n'))
			Column_number = int(input('Enter Column Number - \n'))
			if (Row_number in range(1, Row+1) and Column_number in range(1, Seats+1)):
				if (Row_number in range(1, Row+1) and Column_number in range(1, Seats+1)):
					if (Row*Seats <= 60):
						tixprice = 10
					elif (Row_number <= int(Row/2)):
						tixprice = 10
					else:
						tixprice = 8
					print('price of the ticket - ', '$', tixprice)
					confirm = input('yes for booking and no for Stop booking - ')
					person_detail = {}
					if (confirm == 'yes'):
						person_detail['Name'] = input('Enter Name - ')
						person_detail['Phone_No'] = input('Enter Phone number - ')
						person_detail['Ticket_price'] = tixprice
						table_of_chart[str(Row_number-1)][str(Column_number)] = 'B'
						Booked_seat += 1
						Total_Income += tixprice
					else:
						continue
					Booked_ticket_Person[Row_number-1][Column_number-1] = person_detail
					print('Booked Successfully')
				else:
					print('This seat already booked by some one')
			else:
				print()
				print('***  Invalid Input  ***')
			print()
		elif (x == 3):
			print('Number of purchased Ticket - ', Booked_seat)
			print('Percentage - ', class_call.find_percentage())
			print('Current  Income - ', '$', tixprice)
			print('Total Income - ', '$', Total_Income)
			print()

		elif (x == 4):
			Enter_row = int(input('Enter Row number - \n'))
			Enter_column = int(input('Enter Column number - \n'))
			if (Enter_row in range(1, Row+1) and Enter_column in range(1, Seats+1)):
				if table_of_chart[str(Enter_row-1)][str(Enter_column)] == 'B':
					person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
					print('Name - ', person['Name'])
					print('Phone number - ', person['Phone_No'])
					print('Ticket Price - ', '$', person['Ticket_price'])
				else:
					print()
					print('---**---  Vacant seat  ---**---')
			else:
				print()
				print('***  Invalid Input  ***')
			print()
		else:
			print()
			print('***  Invalid Input  ***')
			print() 
def topgun(i):
	print('\nMovie: TopGun for '+i+ ' seats\n')
	i=float(i)
	ans = 8*i
	print("Total: RM ",ans)
	return ans
def tony(i):
	print('\nMovie: Iron Man for ' +i+' seats\n')
	i=float(i)
	ans = 9*i
	print("Total: RM ", ans)
	return ans

def process_start(s_sock):
	s_sock.send(str.encode('Welcome to Matahari Cinema\n'))

	while True:
		displayMenu(s_sock)
		data = s_sock.recv(2048)
		data = data.decode('utf-8')

		#seatsmenu(s_sock)
		#ddata = s_sock.recv(2048)
		#ddata = ddata.decode('utf-8')

		try:
			func, result  = data.split(" ",2)
		except:
			print(" no data received \n")
			break

		if (func == '1'):
			ans=topgun(result)
			while True:
				seatsmenu(s_sock)
				ddata = s_sock.recv(2048)
				ddata = ddata.decode('utf-8')
				try:
					Row, Seats = ddata.split(" ",2)
				except:
					print(" none \n")
					break
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
