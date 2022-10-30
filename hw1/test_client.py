import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect(("0.0.0.0",12345))
    print("client is started")

    while True:
        msg = input("input: ")
        s.sendall(bytes(msg,'utf-8'))
        data = s.recv(1024)
        print("receive data: ",data.decode('utf-8'))
        if msg=='quit':
            break
