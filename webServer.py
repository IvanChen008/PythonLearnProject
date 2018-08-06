import socket

HOST,PORT = '',8888

listen_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
listen_socket.bind((HOST,PORT))
listen_socket.listen(1)

print("Serving HTTP on port %s ..." % PORT)
while True:
    client_connection,client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request)

    http_response = '''\
    HTTP/1.1 200 OK


    Hello,world!
    '''

    client_connection.sendall(str.encode(http_response,encoding='utf-8'))
    client_connection.close()

""" 
网络服务器首先创建一个侦听套接字（listening socket），
并开启一个永续循环接收新连接；客户端启动一个与服务器的TCP连接，
成功建立连接之后，向服务器发送HTTP请求，之后服务器返回HTTP响应。
要建立TCP连接，客户端和服务器都使用了套接字。 
"""