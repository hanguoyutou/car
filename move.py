from Car import Car
import RPi.GPIO as GPIO
from control import getch
import cv2
import time
from threading import Thread

class myThread(Thread):
	def __init__(self, ID):
		Thread.__init__(self)
		self.id = ID

	def run(self):
		print('Thread ' + str(self.id) + ' starts')
		if self.id == 1:
			run(0.5)
		elif self.id == 2:
			take_pic()

def glo():
	global char
	char = None

def run(sleep):
	global char
	while 1:
		try:
			char = getch()

			if char == 'w':
				Car.init()
				Car.forward(sleep/2)
#				Car.stop()
			elif char == 's':
				Car.init()
				Car.backward(sleep/2)
#				Car.stop()
			elif char == 'q':
				Car.init()
				Car.left(sleep)
#				Car.stop()
			elif char == 'e':
				Car.init()
				Car.right(sleep)
#				Car.stop()
			elif char == 'a':
				Car.init()
				Car.left_(sleep)
#				Car.stop()
			elif char == 'd':
				Car.init()
				Car.right_(sleep)
#				Car.stop()
			elif char == 'x':
				Car.stop(sleep)
			elif char == 'z':
				GPIO.cleanup()
		except KeyboardInterrupt:
			break

#		print(status)
#		time.sleep(0.5)
	return 'run'

def take_pic():
	global char
	cap = cv2.VideoCapture(0)
	i = 1
	j = 1
	k = 1
	while 1:
		ret, frame = cap.read()
		if char == 'w':
			cv2.imwrite('./data/forward/forward%d.png' %i, frame)
#			print('go straight')
#			print(i)
			i += 1
		elif char == 'q':
			cv2.imwrite('./data/left/left%d.png' %j, frame)
#			print('turn left')
#			print(j)
			j += 1
		elif char == 'e':
			cv2.imwrite('./data/right/right%d.png' %k, frame)
#			print('turn right')
#			print(k)
			k += 1
		elif ret == False:
			print('nothing to capture!')
		time.sleep(0.5)
	return 'take_pic'

thread1 = myThread(1)
thread2 = myThread(2)

if __name__ == '__main__':
	glo()
	thread1.start()
	thread2.start()

