import requests

def enviar_arquivo(nome_arquivo, endereco_servidor, porta_servidor):
    url = f"http://{endereco_servidor}:{porta_servidor}/upload"

    with open(nome_arquivo, 'rb') as arquivo:
        response = requests.post(url, files={'arquivo': arquivo})

    if response.status_code == 200:
        print("Arquivo enviado com sucesso.")
    else:
        print("Ocorreu um erro ao enviar o arquivo.")

if __name__ == "__main__":
    nome_arquivo = "chrome"
    endereco_servidor = '192.168.126.125'  # Endereço IP do servidor
    porta_servidor = 5000

    enviar_arquivo(nome_arquivo, endereco_servidor, porta_servidor)
