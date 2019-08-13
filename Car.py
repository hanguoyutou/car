import RPi.GPIO as GPIO
import time

class Car():

	def __init__(self, INT1, INT2, INT3, INT4):
		GPIO.setmode(GPIO.BOARD)
		self.INT1 = INT1
		self.INT2 = INT2
		self.INT3 = INT3
		self.INT4 = INT4

	def init(self):
		GPIO.setup(self.INT1,GPIO.OUT)
		GPIO.setup(self.INT2,GPIO.OUT)
		GPIO.setup(self.INT3,GPIO.OUT)
		GPIO.setup(self.INT4,GPIO.OUT)

	def forward(self, sleep_time):
		GPIO.output(self.INT1,GPIO.HIGH)
		GPIO.output(self.INT2,GPIO.LOW)
		GPIO.output(self.INT3,GPIO.HIGH)
		GPIO.output(self.INT4,GPIO.LOW)
		time.sleep(sleep_time)

	def backward(self, sleep_time):
		GPIO.output(self.INT1,GPIO.LOW)
		GPIO.output(self.INT2,GPIO.HIGH)
		GPIO.output(self.INT3,GPIO.LOW)
		GPIO.output(self.INT4,GPIO.HIGH)
		time.sleep(sleep_time)

	def left(self, sleep_time):
		GPIO.output(self.INT1,False)
		GPIO.output(self.INT2,False)
		GPIO.output(self.INT3,GPIO.HIGH)
		GPIO.output(self.INT4,GPIO.LOW)
		time.sleep(sleep_time)

	def right(self, sleep_time):
		GPIO.output(self.INT1,GPIO.HIGH)
		GPIO.output(self.INT2,GPIO.LOW)
		GPIO.output(self.INT3,False)
		GPIO.output(self.INT4,False)
		time.sleep(sleep_time)

	def left_(self, sleep_time):
		GPIO.output(self.INT1,False)
		GPIO.output(self.INT2,False)
		GPIO.output(self.INT3,GPIO.LOW)
		GPIO.output(self.INT4,GPIO.HIGH)
		time.sleep(sleep_time)

	def right_(self, sleep_time):
		GPIO.output(self.INT1,GPIO.LOW)
		GPIO.output(self.INT2,GPIO.HIGH)
		GPIO.output(self.INT3,False)
		GPIO.output(self.INT4,False)
		time.sleep(sleep_time)

	def stop(self, sleep_time):
		GPIO.output(self.INT1,False)
		GPIO.output(self.INT2,False)
		GPIO.output(self.INT3,False)
		GPIO.output(self.INT4,False)
		time.sleep(sleep_time)

Car = Car(11,12,13,15)

if __name__ == '__main__':
	Car.init()
	Car.forward(2)
	Car.init()
	Car.right(0.3)
	Car.init()
	Car.backward(1)
	Car.init()
	Car.forward(3)
	Car.init()
	Car.stop()
