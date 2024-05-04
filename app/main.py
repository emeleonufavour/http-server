import socket
import sys
from threading import Thread
from request import handle_request

def main():
    fdir = ""
    if len(sys.argv) == 3 and sys.argv[1] == "--directory":
        fdir = sys.argv[2]
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Server is running on port 4221")
    
    try:
        while True:
            print("Waiting for a connection...")
            client_socket, address = server_socket.accept()
            print(f"Connection from {address} has been created")
            Thread(target=handle_request, args=[client_socket,address,fdir]).start()

    except KeyboardInterrupt:
        print("\nServer is shutting down")
    finally:
        server_socket.close()
        print("Server has shut down")
        
        
if __name__ == "__main__":
    main()
    # a = "GET /user-agent HTTP/1.1 Host: localhost:4221 User-Agent: curl/7.64.1 Accept-Encoding: gzip"
    # b = a.split(" ")
    # c = b[len(b) -3]
    # print(c)