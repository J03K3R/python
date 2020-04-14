#!/usr/bin/python

import SocketServer
import socket

class EchoHandler(SocketServer.BaseRequestHandler) :
    def handle(self) :
	print "Connection from: ", self.client_address
	data = 'dummy'

	while len(data) :
	    data = self.request.recv(1024)
	    print "Client Sent: " + data
	    self.request.send(data)

	print "Client Left"

serverAddr = ("0.0.0.0", 9000)
server = SocketServer.TCPServer(serverAddr, EchoHandler)
server.serve_forever()
