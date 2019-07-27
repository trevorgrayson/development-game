import socket
from console import challenge

HOST = '0.0.0.0'  # anyone can playyyyyyyyyyyyyyy
PORT = 1337


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
        while(True):
            conn, addr = s.accept()

            with conn:
                io = IO(conn)

                print('Connected by', addr)

                try:
                    challenge(io)
                except Exception as err:
                    print(err)
