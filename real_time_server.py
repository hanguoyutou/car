import socket
import cv2

cap = cv2.VideoCapture(0)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '175.159.198.214'
port = 12345

server.bind((host,port))
server.listen(5)
while 1:
	conn, addr = server.accept()
	while 1:
		try:
			ret, frame = cap.read()
			if ret == True:
				conn.send(frame)
			else:
				print('can see nothing')
		except ConnectionResetError as e:
			print(e)
			break
	conn.close()
