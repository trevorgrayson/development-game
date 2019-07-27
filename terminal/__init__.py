import socket
import threading
from console import challenge

HOST = '0.0.0.0'  # anyone can playyyyyyyyyyyyyyy
PORT = 1338


class IO:
    def __init__(self, conn):
        self.conn = conn

    def say(self, msg, end="\n"):
        msg = msg + end
        self.conn.sendall(msg.encode('utf-8'))

    def prompt(self, msg):
        self.say(msg, end=' ')
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            try:
                return(data.decode('utf-8')[:-1])
            except UnicodeDecodeError as err:
                print(f"Could not decode {data}")

    def ask(self, msg):
        return self.prompt(msg)

# timeout, reconnect
def accept(sock):
    """Recursive socket opening"""
    thread = threading.Thread(target=accept, args=(sock,))
    conn, addr = sock.accept()
    thread.start()        # catch error?

    with conn:
        io = IO(conn)

        print('Connected by', addr)
        challenge(io)

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()

        print("The server is starting...")
        print('listening on: %s.'%PORT)

        accept(sock)
