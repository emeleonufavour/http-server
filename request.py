import socket
from header import get_header


def handle_request(client_socket: socket.socket,address, fdir: str):
    """
        A basic HTTP server request handler
    Args:
        client_socket (socket): represents a socket connection to a client
    """
    # This line receives data from the client socket. 
    # It reads up to 1024 bytes of data from the client
    # but doesn't do anything with it
    data = client_socket.recv(4096).decode()
    print(f"Data from Client Socket: {data}")
    
    # HTTP response strings
    ok_response = "HTTP/1.1 200 OK\r\n\r\n"
    not_found_response = "HTTP/1.1 404 Not Found\r\n\r\n"
    path = data.split(" ")[1]
    if path == "/":
        # This line sends the HTTP response back to the client.
        # Before sending, the response string is encoded to 
        # bytes using the encode() method because sockets deal
        # with bytes, not strings.
        client_socket.send(ok_response.encode())
    elif path.startswith("/echo/"):
        message = path[6:]
        # b in the string denotes a bytes literal.
        # Bytes literals are sequence of bytes as opposed to 
        # strings which are sequence of characters
        client_socket.send(b"HTTP/1.1 200 OK\r\n")
        client_socket.send(b"Content-Type: text/plain\r\n")
        client_socket.send(f"Content-Length: {len(message)}\r\n".encode("ascii"))
        client_socket.send(b"\r\n")
        client_socket.send(message.encode("ascii"))
    elif path.startswith("/user-agent"):
        header = get_header(data)
        if header:
            print(f"Header: {header}")
            client_socket.send(b"HTTP/1.1 200 OK\r\n")
            client_socket.send(b"Content-Type: text/plain\r\n")
            client_socket.send(f"Content-Length: {len(header)}\r\n".encode("ascii"))
            client_socket.send(b"\r\n")
            client_socket.send(header.encode("ascii"))
    elif path.startswith("/files/"):
        fname = path.split("/")[2]
        fpath = fdir + fname
        if data.split(" ")[0] == "GET":
            try:
                f = open(fpath, "rb")
                blob = f.read()
                f.close()
                response = bytearray(b"HTTP/1.1 200 OK\r\n")
                response.extend(b"Content-Type: application/octet-stream\r\n")
                response.extend(f"Content-Length: {len(blob)}\r\n\r\n".encode())
                response.extend(blob)
                client_socket.send(response)
            except:
                client_socket.send(b"HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n")
        else:
            file_contents = data.split("\r\n\r\n")[1].encode("ascii")
            with open(fpath, "wb") as file:
                file.write(file_contents)
            # client.send(b"HTTP/1.1 201 Created\r\n")
            response = bytearray("HTTP/1.1 201 Created\r\n\r\n".encode("ascii"))
            response.extend(b"Content-Type: text/plain\r\n")
            response.extend(
                f"Content-Length: {len(file_contents)}\r\n\r\n".encode("ascii")
            )
            client_socket.send(response)
    else:
        client_socket.send(not_found_response.encode())
    client_socket.close()