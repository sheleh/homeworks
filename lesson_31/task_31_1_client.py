import socket

HOST = '127.0.0.1'  # the servers hostname
PORT = 10001
message_to_mars = b"where is a Elon's Mask Car???"
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    try:
        s.connect((HOST, PORT))
        s.sendall(message_to_mars)
        data = s.recv(100)
        print('Received', repr(data))
    except Exception:
        print('OOps, something went wrong')
