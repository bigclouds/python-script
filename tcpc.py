# -*- coding:utf-8 -*-
from socket import *
import sys
 
ServerUrl = "0.0.0.0:9999"
def SocketClient():
    try:
        s=socket(AF_INET,SOCK_STREAM,0)
 
        Colon = ServerUrl.find(':')
        IP = ServerUrl[0:Colon]
        Port = ServerUrl[Colon+1:]
 
        s.connect((IP,int(Port)))
        while True:
            sdata = raw_input('>')
            if not sdata:
                break
            s.send(sdata)
            result = s.recv(1024)
            print "Response:\r\n%s\r\n" % result
        s.close()
    except Exception,ex:
        print ex
 
SocketClient()
