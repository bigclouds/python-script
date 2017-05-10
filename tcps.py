from socket import *
 
ServerUrl = "0.0.0.0:9999"
def SocketServer():
    try:
        Colon = ServerUrl.find(':')
        IP = ServerUrl[0:Colon]
        Port = int(ServerUrl[Colon+1:])
 
        print 'Server start:%s'%ServerUrl
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
 
        sockobj.bind((IP, Port))
        sockobj.listen(5)
 
        while True:
            connection, address = sockobj.accept( )
            print 'connected by client:', address
            while True:
                data = connection.recv(1024)
                if not data: break
                connection.send(data)
                print 'Receive MSG:%s'%data.strip()
            connection.close( )
    except Exception,ex:
        print ex
 
SocketServer()
