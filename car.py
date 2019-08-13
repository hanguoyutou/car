import RPi.GPIO as GPIO
import time

class Car():

	def __init__(self, left_in1, left_in2, left_ena, right_in3, right_in4, right_enb, low_electrical_level, hight_electrical_level):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)

	self.left_in1 = left_in1
	self.left_in2 = left_in2
	self.left_ena = left_ena
	if self.left_ena > 0:
		GPIO.setup(self.left_ena, GPIO.OUT)

	GPIO.setup(self.left_in1, GPIO.OUT)
	GPIO.setup(self.left_in2, GPIO.OUT)

	self.right_in3 = right_in3
	self.right_in4 = right_in4
	self.right_enb = right_enb
	
	
	GPIO.setup(self.right_in3, GPIO.OUT)
	GPIO.setup(self.right_in4, GPIO.OUT)
	if self.right_enb > 0:
		GPIO.setup(self.right_enb, GPIO.OUT)

	self.hight_electrical_level = hight_electrical_level
	self.low_electrical_level = low_electrical_level

	#右边轮子前进
	def rFoward(self):
		GPIO.output(self.right_in3, self.hight_electrical_level)
		GPIO.output(self.right_in4, self.low_electrical_level)
		if self.right_enb > 0:
			GPIO.output(self.right_enb, self.hight_electrical_level)

	#左边轮子前进
	def lFoward(self):
		GPIO.output(self.left_in1, self.hight_electrical_level)
		GPIO.output(self.left_in2, self.low_electrical_level)
		if self.left_ena > 0:
			GPIO.output(self.left_ena, self.hight_electrical_level)

	'''
	右边轮子后退
	'''
	def rBackward(self):
		GPIO.output(self.right_in3, self.low_electrical_level)
		GPIO.output(self.right_in4, self.hight_electrical_level)
		if self.right_enb > 0:
			GPIO.output(self.right_enb, self.hight_electrical_level)
    
	'''
	左边边轮子后退
	'''
	def lBackward(self):
		GPIO.output(self.left_in1, self.low_electrical_level)
		GPIO.output(self.left_in2, self.hight_electrical_level)
		if self.left_ena > 0:
			GPIO.output(self.left_ena, self.hight_electrical_level)
    
	'''
	左边轮子停止
	'''
	def lStop(self):
		if self.left_ena > 0:
			GPIO.output(self.left_ena, self.low_electrical_level)
		else:
			GPIO.output(self.left_in2, self.low_electrical_level)
			GPIO.output(self.left_in1, self.low_electrical_level)
            
	'''
	右边轮子停止
	'''
	def rStop(self):
		if self.right_enb > 0:
			GPIO.output(self.right_enb, self.low_electrical_level)
		else:
			GPIO.output(self.right_in3, self.low_electrical_level)
			GPIO.output(self.right_in4, self.low_electrical_level)
	'''
	小车前进
	'''
	def moveForward(self):
		self.lFoward()
		self.rFoward()
    
	'''
	小车后退
	'''
	def moveBackground(self):
		self.lBackward()
		self.rBackward()

	'''小车右转
	'''
	def spinRight(self):
		self.rFoward()
		self.lBackward()
    
	'''小车左转
	'''
	def spinLeft(self):
		self.rBackward()
		self.lFoward()
    
	'''
	小车停止--左边及右边轮子都停止
	'''
	def stop(self):
		self.lStop()
		self.rStop()

	def cleanup(self):
		GPIO.cleanup()

def instanceCar():
	return Car(11, 13, 15, 38, 40, 36, 0, 1)
