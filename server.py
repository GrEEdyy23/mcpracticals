import socket

HOST = '127.0.0.1'  # server's IP address
PORT = 65432  # server's port number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Server listening on', HOST, 'port', PORT)
    conn, addr = s.accept()
    print('Connected by', addr)
    with open(r'D:\Mobile computing','file_to_send') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            conn.sendall(data)
    print('File sent successfully')
