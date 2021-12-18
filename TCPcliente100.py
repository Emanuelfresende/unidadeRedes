import socket
import sys

HOST = '127.0.0.1'
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

file_name = ''
url = ''

while True:
    print('Informe o protocolo HTTP (1 para 1.1 ou t para Tupi): ')
    prot = input()
    if prot == "1":
        print('Informe o nome do arquivo: ')
        file_name = input()
    elif prot == "t":
        print('Informe a URL: ')
        url = input()
    else:
        print('Foi mal')
        sys.exit(1)


    if prot == "1":
        request = 'GET /{} HTTP/1.1\r\n'.format(file_name)
        request += 'Host: ufs.client.br\r\n'
        request += 'Accept-Language: *\r\n'
        print("sending request:\n", request)
        tcp.send(bytes(request, "utf-8"));
        buff_size = int(tcp.recv(1024).decode("utf-8"))
        response = tcp.recv(buff_size).decode("utf-8")
        print("received response:\n", response)

    if prot == "t":
        if url == '':
            url = "https://ccsa.ufs.br/pagina/20168-departamento-de-ciencia-da-informacao"
        request = 'GET / HTTP/Tupi\r\n'
        request += 'Host: ufs.client.br\r\n'
        request += 'Accept-Language: *\r\n'
        elif opt == "c":
            print('Informe o nome a ser buscado')
            pal = input()
            request += 'URL_Busca: {} {}\r\n'.format(url, pal)
     
        print("sending request: \n", request)
        tcp.send(bytes(request, "utf-8"));
        buff_size = int(tcp.recv(1024).decode("utf-8"))
        print('buff_size ', buff_size)
        response = tcp.recv(buff_size).decode("utf-8")
        print("received response: \n", response)

tcp.close()
