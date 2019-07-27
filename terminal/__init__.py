import socket
from console import challenge

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 1343        # Port to listen on (non-privileged ports are > 1023)


class IO:
    def __init__(self, conn):
        self.conn = conn

    def say(self, msg):
        self.conn.sendall(msg.encode('utf-8'))

    def prompt(self, msg):
        self.say(msg)
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            return(data.decode('utf-8'))


def server():
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
				s.bind((HOST, PORT))
				s.listen()
				print('listening')
				conn, addr = s.accept()
				with conn:
						io = IO(conn)

						print('Connected by', addr)

						challenge(io)
