#!/usr/bin/python

import socket
import struct

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

#binds the interface
rawSocket.bind(("eno2", socket.htons(0x0800)))

#Sets the source and destination
packet = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x00')

#sends the packet
rawSocket.send(packet + "Hello there")
