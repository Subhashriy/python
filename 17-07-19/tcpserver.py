import socket
def fact(n):
        if n==0 or n==1:
            f=1
        else:
            f=n * fact(n-1)
        return f


def main():
    host='127.0.0.1'
    port=5000
    
    #Creting a socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket Created.")

    #binding host and port to the socket
    s.bind((host,port))
    print("Host and port are binded to the socket")

    #listen to one client
    s.listen(1)

    #accept the connection
    print("Waiting for client")
    conn,addr=s.accept()
    print('Connection accepted from: {}'.format(addr))

    while True:
        data=conn.recv(1024).decode('utf-8')
        if not data:
            break
        data=str(fact(int(data)))
        conn.send(data.encode('utf-8'))

    conn.close()

    


if __name__=='__main__':
    main()
    
    
    


