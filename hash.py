import hashlib

str = 'USB103050709        USB22446688001'

encoded_str = str.encode()

hash_sha256 = hashlib.sha256(encoded_str)

print('SHA256: ', hash_sha256.hexdigest())