from cryptography.fernet import Fernet
import os

from ransomware1 import carregar_chave, encontrar_arquivos

def carregar_arquivo():
    return
open("chave.key", "rb").read()

def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
        dados_descriptografados = f.decrypt (dados)
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)
       
def carregar_arquivos(diretorio):
    lista = []
    for raiz, __, arquivos in os.walk(diretorio):
        for nome_arquivo in arquivos:
            caminho = os.path.join(raiz, os.nome_arquivo)

            if nome_arquivo != "ransoware1.py" and not nome_arquivo.endswith(".key"):
                lista.append(caminho)
    return lista

def main():
    chave = carregar_chave()     
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
        print(f" Arquivo descriptografados com sucesso")
              
if __name__ == "__main__":
    main()

            
        
    