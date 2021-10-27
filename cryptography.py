import hashlib, binascii

sha3_256_output = hashlib.sha3_256(b"AldeaWiki").digest()

print("SHA3-256('AldeaWiki') =", binascii.hexlify(sha3_256_output))