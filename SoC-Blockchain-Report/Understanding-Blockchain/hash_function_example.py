import hashlib

def hash_block(data):
    return hashlib.sha256(data.encode()).hexdigest()

print("Hash:", hash_block("example block"))
