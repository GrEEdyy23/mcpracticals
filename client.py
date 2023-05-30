import socket

HOST = '127.0.0.1'  # server's IP address
PORT = 65432  # server's port number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open('file_received', 'wb') as f:
        while True:
            data = s.recv(1024)
            if not data:
                break
            f.write(data)
    print('File received successfully')
