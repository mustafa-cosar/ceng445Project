from ceng445 import *
from socket import *
from ApplicationProcess import *

def main():
    HOST = ''
    PORT = 7777

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((HOST, PORT))

    sock.listen(5)
    processes = []

    conn, addr = sock.accept()
    try:
        while(conn):
            p = ApplicationProcess((conn, addr))
            p.start()
            processes.append(p)
            conn, addr = sock.accept()

    except KeyboardInterrupt:
        for p in processes:
            p.join()

if __name__ == '__main__':
    main()
