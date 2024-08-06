import hashlib


hash_object = hashlib.sha1(b'Hello World')

hash = "0a4d55a8d778e5022fab701977c5d840bbc486d0"

hex_dig = hash_object.hexdigest()

if hash == hex_dig:
    print("\n")
    print("Hash is Valid")
    print("\n")
else:
    print("\n")
    print("Hash is Invalid")
    print("\n")