import hashlib
# Leitura dos arquivos.
arquivo1 = 'hash1.txt'
arquivo2 = 'hash2.txt'
# Tipo de hash que vou utilizar.
hash1 = hashlib.new('ripemd160')
hash2 = hashlib.new('ripemd160')
# Transformando as informações do arquivo no formato definido anteriormente.
hash1.update(open(arquivo1, 'rb').read())
hash2.update(open(arquivo2, 'rb').read())
# Comparação e impressão dos hashs das informações dos arquivos.
if hash1.digest() != hash2.digest():
    print(f'\nO arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print('\nO hash do arquivo arquivo1 hash1.txt é: ', hash1.hexdigest())
    print('\nO hash do arquivo arquivo2 hash2.txt é: ', hash2.hexdigest())
else:
    print(f'O arquivo: {arquivo1} é igual do arquivo: {arquivo2}')
    print('\nO hash do arquivo arquivo1 hash1.txt é: ', hash1.hexdigest())
    print('\nO hash do arquivo arquivo2 hash2.txt é: ', hash2.hexdigest())