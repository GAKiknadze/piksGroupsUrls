from urllib.request import Request, urlopen
import itertools
from threading import Thread

START = 4
STOP = 5
FILE = open('pik_redirect.txt', 'a')
ALPHA = 'abcdefghijklmnopqrstuvwxyz1234567890'


def check(url):
	try:
		req = Request(
			'https://s.pik.ru/{}'.format(url),
			headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(req)
		return webpage.geturl()
	except:
		return None


class MyThread(Thread):
	"""docstring for MyThread"""

	def __init__(self, arg):
		super(MyThread, self).__init__()
		self.arg = arg

	def run(self):
		for k in range(START, STOP):
			for i in itertools.combinations_with_replacement(ALPHA, k):
				password = '' + self.arg
				for letter in i:
					password += letter
				u = check(password)
				if u:
					FILE.write(u + '\n')
					print(password, u, 'УСПЕХ')
				else:
					print(password, 'Не существует')


def createThreds():
	for i in list(ALPHA):
		my_thread = MyThread(i)
		my_thread.start()
		print('Поток', i, 'запущен')


if __name__ == "__main__":
	createThreds()
