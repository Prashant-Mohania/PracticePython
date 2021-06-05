import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
host = '192.168.43.227'
port = 1255
# print(socket.getaddrinfo(host, port))
s.bind((host, port))
s.listen(5)
socketclient, address = s.accept()
print("Get", address)
a = True
while a:
    # msg = input("Enter your message:- ")
    # s.send(msg.encode('UTF-8'))
    msg = socketclient.recv(1024)
    msg = msg.decode("UTF-8")
    print(msg)
    b = msg.lower()
    if b == 'quit':
        s.close()
        a = False