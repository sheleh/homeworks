import socket

HOST = '127.0.0.1'  # Server IP address
PORT = 65432    # Server port
key = '3'   # Encryption key
text = 'Hello On MARS!'
message = key + '*' + text
data = ''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        s.sendall(message.encode())
        data = s.recv(1024).decode()
    except ConnectionRefusedError:
        print('Connection error')

print('Received', repr(data))

