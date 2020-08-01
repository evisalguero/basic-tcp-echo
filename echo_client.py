import socket
import argparse

host = '127.0.0.1'

def echo_client(port):
    # create TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect socket to the server
    server_addr = (host, port)
    print("Connecting to %s port %s" %server_addr)
    sock.connect(server_addr)

    # send data
    try:
        message = "Test message. This will be echoed."
        print("Sending: %s" %message)
        sock.sendall(message.encode("utf-8"))
        # Look for response/echo
        amount_recvd = 0
        amount_expected = len(message)
        while amount_recvd < amount_expected:
            data = sock.recv(16)
            amount_recvd += len(data)
            print("Received %s" %data.decode("utf-8"))
    except socket.errno as e:
        print("Socket error: %s" %str(e))
    except Exception as e:
        print("Other exception: %s" %str(e))
    finally:
        print("Closing connection to the server")
        sock.close()

parser = argparse.ArgumentParser(description='Socket Client')
parser.add_argument('--port', action='store', dest='port', type=int, required=True)
recvd_args = parser.parse_args()
port = recvd_args.port
echo_client(port)
