# Echo server with threading
# Create a socket echo server which handles each connection in a separate Thread

import socket
from threading import Thread

SERVER_TCP = '127.0.0.1'
SERVER_PORT = 65432
BUFFER_SIZE = 1024


class incoming_thread(Thread):
    def __init__(self, ip, port, sock):
        super().__init__()
        self.ip = ip
        self.port = port
        self.sock = sock
        print(f'new thread connection started from {ip}, {port}')

    def run(self):
        data = self.sock.recv(BUFFER_SIZE)
        if type(data) == bytes:
            f_data = ":".join("{:02x}".format(c) for c in data)
            print(f_data)
            self.sock.send(f_data.encode())
        else:
            print('Please send me a BYTES')


tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (SERVER_TCP, SERVER_PORT)
try:
    tcp_sock.bind(server_address)
except OSError:
    print('Cant start a server')
else:
    threads = []
    while True:
        tcp_sock.listen(10)
        print('Server waiting for connections')
        (conn, (ip, port)) = tcp_sock.accept()
        print(f'Got connection from {ip}')
        new_thread = incoming_thread(ip, port, conn)
        new_thread.start()
        threads.append(new_thread)
        for t in threads:
            t.join()
