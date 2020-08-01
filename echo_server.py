import socket
import sys
import argparse

host = '127.0.0.1'
buffer_size = 2048

def echo_server(port):
    # create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # enable reuse addr/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind socket to port
    server_addr = (host, port)
    sock.bind(server_addr)
    # listen for a client
    sock.listen(1)
    while True:
        print("Waiting to receive message from a client")
        # client connection
        client, addr = sock.accept()
        data = client.recv(buffer_size)
        if data:
            print("TCP server received: %s" %data)
            client.send(data)
            print("sent data back to host %s, port %d" %addr)
            # end connection
            client.close()


parser = argparse.ArgumentParser(description='Socket Server')
parser.add_argument('--port', action="store", dest="port", type=int, required=True)
recvd_args = parser.parse_args()
port = recvd_args.port
echo_server(port)



    