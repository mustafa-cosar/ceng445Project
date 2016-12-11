from ceng445 import *
from socket import *
from ApplicationProcess import *
from sys import argv

def main():

    (HOST, PORT) = argv[1], int(argv[2])

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((HOST, PORT))

    sock.listen(5)
    print("Server started listening with ", (HOST,PORT))
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
        sock.close()

if __name__ == '__main__':
    main()
