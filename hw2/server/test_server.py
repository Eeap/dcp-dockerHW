import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0",12345))
    print("socket bind %s: %d" %("0.0.0.0",12345))
    s.listen()
    print("server is started")
    conn, addr = s.accept()

    with conn:
        print("connected by",addr)
        data = conn.recv(1024)
        conn.sendall(data)
        

