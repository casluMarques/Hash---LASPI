import os
import hashlib

local_txt_hashes = input('local para o txt dos hashes: ')

def calcular_hash_arquivo(caminho_arquivo, algoritmo='sha256'):
    # Cria o objeto hash usando o algoritmo especificado
    hash_obj = hashlib.new(algoritmo)
    
    # Lê o arquivo em blocos para evitar usar muita memória
    with open(caminho_arquivo, 'rb') as arquivo:
        for bloco in iter(lambda: arquivo.read(4096), b''):
            hash_obj.update(bloco)
    
    # Retorna o hash no formato hexadecimal
    return hash_obj.hexdigest()

def percorrer_pasta_e_calcular_hashes(caminho_pasta):
    #dicionário para associar cada arquivo a seu respectivo hash
    hashes = {}
    #andando pelo diretório, calculando hashes e salvando no dicionário
    for raiz, _, arquivos in os.walk(caminho_pasta):
        for nome_arquivo in arquivos:
            caminho_arquivo = os.path.join(raiz, nome_arquivo)
            hash_arquivo = calcular_hash_arquivo(caminho_arquivo)
            hashes[caminho_arquivo] = hash_arquivo
            #print(f'{caminho_arquivo}: {hash_arquivo}')
    return hashes

# criando o arquivo de hashes
caminho_da_pasta = input('Path documentação: ')
nome_texto = input('Nome do arquivo de hashes: ')
hashes_dos_arquivos = percorrer_pasta_e_calcular_hashes(caminho_da_pasta)

texto = '{}/{}.txt'.format(local_txt_hashes, nome_texto)
str_hashes = str(hashes_dos_arquivos)

with open(texto, 'w') as escrita:
    escrita.write(str_hashes)

#hash para o relatório

print('Hash para o relatório: {}'.format(calcular_hash_arquivo(texto)))

