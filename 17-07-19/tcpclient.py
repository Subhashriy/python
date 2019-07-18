import socket
def main():
    host='127.0.0.1'
    port=5000

    #Creting a socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket Created.")

    #connect to the server
    s.connect((host,port))
    print('Connected to server.')
    
    #send msg to the server

    data=input('Enter the number to find the factorial: ')
    print('Enter q to terminate connection.')
    while data!='q':
        print(data)
        #s.send(str.encode(data,'utf-8'))
        s.send(str.encode(data,'utf-8'))
        data=s.recv(1024).decode('utf-8')
        print(data)
        data=input('Enter the number to find the factorial: ')

    s.close()
        

    

if __name__=='__main__':
    main()




