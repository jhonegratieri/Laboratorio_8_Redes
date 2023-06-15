import socket

HOST = '192.168.126.125'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

with open('chrome', 'rb') as arquivo:
    dados = arquivo.read()
    tcp.sendall(dados)

tcp.close()

