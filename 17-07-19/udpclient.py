import socket
def main():
    host='127.0.0.1'
    port=5000

    server=('127.0.0.1',5001)
    #Creting a socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket Created.")

    s.bind((host,port))

    data=input('Enter the number to find the factorial: ')
    print('Enter q to terminate connection.')
    while data!='q':
        print(data)
        #s.send(str.encode(data,'utf-8'))
        s.sendto(str.encode(data,'utf-8'),server)
        data,addr=s.recvfrom(1024)
        data=data.decode('utf-8')
        print(data)
        data=input('Enter the number to find the factorial: ')

    s.close()
        

    

if __name__=='__main__':
    main()