import socket

tcpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('175.159.198.214',8080)
tcpServerSocket.bind(address)
tcpServerSocket.listen(5)

while 1:
	newServerSocket, destAddr = tcpServerSocket.accept()
	while 1:
		recvData = newServerSock.recv(1024)
		if len(recvData) == 0:
			newServerSocket.send('thanks!')
		elif len(recvData) == 0:
			newServerSocket.close()
			print('---------')
			break

tcpServerSocket.close()
