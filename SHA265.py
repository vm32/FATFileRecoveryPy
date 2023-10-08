import hashlib
def sha256_hash(text):
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    hashed_text = sha256.hexdigest()
    return hashed_text
input_text = input("Enter the text to hash: ")
hashed_text = sha256_hash(input_text)
print("SHA-256 Hash:", hashed_text)
