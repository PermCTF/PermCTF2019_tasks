from hashlib import md5,sha1,sha224,sha256,sha384
import string
alphabet = string.printable

with open("message","r") as hashfile:
    for line in hashfile:
        for char in alphabet:

            hash = md5(str.encode(char))
            if hash.hexdigest() == line.strip():
                print(char,end='')
                break

            hash = sha1(str.encode(char))
            if hash.hexdigest() == line.strip():
                print(char,end='')
                break

            hash = sha224(str.encode(char))
            if hash.hexdigest() == line.strip():
                print(char,end='')
                break

            hash = sha256(str.encode(char))
            if hash.hexdigest() == line.strip():
                print(char,end='')
                break

            hash = sha384(str.encode(char))
            if hash.hexdigest() == line.strip():
                print(char,end='')
                break
