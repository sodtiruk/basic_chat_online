import socket
import threading

def handleClient(client: socket.socket, addr):
    while True:
        message = client.recv(1024)
        if message:
            print(message) 


def main():

    IPSERVER = "localhost" 
    PORTSERVER = 3333

    #create server tcp use ipv4
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IPSERVER, PORTSERVER))
    server.listen(5)

    while True:
        print("watting client connect")
        client, addr = server.accept()

        print(addr, "connected")

        #start thread handle client 
        threading.Thread(target=handleClient, args=(client, addr), daemon=True).start()



if __name__ == "__main__":
    main()