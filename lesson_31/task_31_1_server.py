#  Create a server and client, which will use user datagram protocol (UDP) for communication.

import socket
timeout = 3600  # if U need
# create a UDP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind the socket to the port
server_address = ('localhost', 10001)
print('starting up on {} port {}'. format(*server_address))
# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock
sock.bind(server_address)

while True:
    # Wait for connection
    print('Waiting for connection')
    sock.settimeout(timeout)
    message, client_address = sock.recvfrom(100)
    print('connection from', client_address)
        #Receive data in small chunks and retransmit it
    if message:
        print('sending data back to the client')
        sock.sendto(message.upper(), client_address)
    else:
        print('no data from', client_address)
        break
