import socket

try:
    while True:
        server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_TCP)

        address = ('127.0.0.1', 50000)
        server_socket.bind(address)
        server_socket.listen(1)
        connection, client_address = server_socket.accept()
        buffersize = 32
        echomsg = connection.recv(buffersize)
        connection.sendall(echomsg)
        connection.shutdown(socket.SHUT_WR)
        connection.close()

except KeyboardInterrupt:
    server_socket.close()
