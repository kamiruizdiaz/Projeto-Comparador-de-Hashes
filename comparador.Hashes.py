import hashlib

arquivo1 = 'texto1.txt'
arquivo2 = 'texto2.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f' O arquivo: {arquivo1} e diferente do arquivo: {arquivo2}')
    print('O hash do arquivo texto1.txt e: ', hash1.hexdigest())
    print('O hash do arquivo texto2.txt e: ', hash2.hexdigest())

else:
    print(f' O arquivo: {arquivo1} e igual o arquivo: {arquivo2}')
    print('O hash do arquivo texto1.txt e: ', hash1.hexdigest())
    print('O hash do arquivo texto2.txt e: ', hash2.hexdigest())
