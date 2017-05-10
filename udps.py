from socket import *
from time import ctime
import time
import signal
import threading
import thread

HOST = '0.0.0.0'
PORT = 65535
BUFSIZ = 4096
ADDR = (HOST, PORT)
MAX = 1024 * 1024 * 1024 * 10
MAX1 = 1024 * 1024


c = c2 = 0
l = l2 = 0


def myHandler(signum, frame):
    print '...received from and returned to:', l , l2, c , c2, l + l2, c + c2
    exit()

# register signal.SIGALRM's handler 
signal.signal(signal.SIGINT, myHandler)

def t1():
    global l ,c
    time.sleep(1)
    udpServer = socket(AF_INET, SOCK_DGRAM)
    udpServer.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
    udpServer.bind(ADDR)
    print 'waiting for message...1', PORT

    while True:
        data, addr = udpServer.recvfrom(BUFSIZ)
        print "t1",data, addr
        l = l + len(data)
        c = c + 1

        udpServer.sendto('[%s] %s' % (ctime(), data), addr)
        if l > MAX1:
            break
    print '...received from and returned to:', addr, l, c	
    udpServer.close()

def t2():
    global l2 ,c2
    udpServer = socket(AF_INET, SOCK_DGRAM)
    udpServer.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
    udpServer.bind(ADDR)
    print 'waiting for message...2', PORT

    while True:
        data, addr = udpServer.recvfrom(BUFSIZ)
        print "t2",data, addr
        l2 = l2 + len(data)
        c2 = c2 + 1

        udpServer.sendto('[%s] %s' % (ctime(), data), addr)
        if l > MAX1:
            break
    print '...received from and returned to2:', addr, l2, c2	
    udpServer.close()

thread.start_new_thread(t1, ())
thread.start_new_thread(t2, ())

while True:
    time.sleep(1)
