import socket
import ceaser_crypto

# Create a TCP/IP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind a socket to the part
server_address = ('127.0.0.1', 65432)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listening
sock.listen(1)

while True:
    # Connections Wait
    print('i`m waiting for connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Receive the data
        data = connection.recv(1024)
        print('received {!r}'.format(data))
        if data:
            # decoding data from bytes and split on key and text
            data = data.decode().split('*', 1)
            key = data[0]
            text = data[1]
            if key.startswith('-'):
                key = key[1:]
                result = ceaser_crypto.decrypt(text, key)
            else:
                result = ceaser_crypto.encrypt(text, key)
            print('I do some things and send you back')
            connection.sendall(result.encode())
        else:
            print('no data from', client_address)
            break
    except UnicodeDecodeError:
        print('English Please!')
    except ValueError:
        print('Incorrect Data received')
    finally:
        # close connection
        connection.close()

