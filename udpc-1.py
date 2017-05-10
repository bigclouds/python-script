from socket import *
import sys, time

HOST = sys.argv[1]
PORT = int(sys.argv[2])
BUFSIZ = 10
ADDR = (HOST, PORT)
MAX = 1024
MAX1 = 1024 * 1024

udpClient = socket(AF_INET, SOCK_DGRAM)
l = 0
c = 0
while True:
    data = "t" * BUFSIZ

    udpClient.sendto(data,ADDR)
    l = l + len(data)
    c = c + 1

    data, ADDR = udpClient.recvfrom(BUFSIZ)
    print data
    #if not data:
    if l > MAX:
        break
    time.sleep(1)
print "count " , c , "; bytes ", l
udpClient.close()
