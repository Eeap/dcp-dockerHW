import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect(("server",12345))
    print("client is started")
    msg = "I'm client."
    s.sendall(bytes(msg,'utf-8'))
    data = s.recv(1024)
    print("receive data: ",data.decode('utf-8'))
    print("connection end")

