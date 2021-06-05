import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1255
s.connect((host, port))
a = True
while a:
    msg = input("Enter your message:- ")
    s.send(msg.encode('UTF-8'))
    # msg = socketclient.recv(1024)
    # msg = msg.decode("UTF-8")
    b = msg.lower()
    if b == 'quit':
        s.close()
        a = False